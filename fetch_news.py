import requests
from bs4 import BeautifulSoup
import django
import os
import time
import re

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsflow.settings")
django.setup()

from articles.models import NewsArticle

SUPER_BOWL_CATEGORIES = [
    "https://www.espn.com/nfl/",
    "https://www.espn.com/nfl/super-bowl/",
    "https://www.espn.com/nfl/injuries",
    "https://www.espn.com/nfl/transactions",
    "https://www.espn.com/nfl/stats",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Function to clean title (remove timestamps, author names, and extra spaces)
def clean_title(title):
    title = re.sub(r"\d+h.*", "", title)  # Remove time-based metadata (e.g., "3hBen Solak")
    title = re.sub(r"\|.*", "", title)  # Remove anything after "|"
    return title.strip()

def fetch_latest_news():
    existing_urls = set(NewsArticle.objects.values_list('url', flat=True))  # Track existing URLs
    new_articles = []
    seen_titles = set()  # Track seen article titles

    for category_url in SUPER_BOWL_CATEGORIES:
        print(f"🔍 Fetching news from: {category_url}")

        try:
            response = requests.get(category_url, headers=HEADERS, timeout=10)
            if response.status_code != 200:
                print(f"❌ Failed to fetch news from {category_url}. HTTP Status: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            # ✅ Select the main content area for news articles
            articles = soup.select("article a[href], section a[href]")  # Get all links in <article> or <section>

            for item in articles:
                title = item.get_text(strip=True)
                link = item["href"]

                # ✅ Convert relative URLs to absolute
                if link.startswith("/") and not link.startswith("//"):
                    link = "https://www.espn.com" + link

                # ✅ Skip invalid links
                if not title or title.lower() in ["menu", "espn", "home", "watch"]:
                    continue

                # ✅ Ensure the URL is a valid article (must contain "/story/")
                if "/story/" not in link:
                    continue

                # ✅ Clean title (remove unnecessary metadata)
                cleaned_title = clean_title(title)

                # ✅ Skip if title has already been seen (prevent duplicates across categories)
                if cleaned_title in seen_titles:
                    continue

                # ✅ Skip duplicate URLs (ensure database uniqueness)
                if link in existing_urls:
                    continue

                # ✅ Extract summary (Find first paragraph in the article section)
                summary_tag = item.find_next("p")
                summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."

                # ✅ Print debugging info before insert
                print(f"📝 New Article: {cleaned_title} | {link}")

                new_articles.append(NewsArticle(
                    title=cleaned_title,
                    source="ESPN",
                    url=link,
                    summary=summary
                ))

                seen_titles.add(cleaned_title)  # Mark title as seen
                existing_urls.add(link)  # Prevent duplicate URLs

                break  # Stop after finding one article per category

        except requests.exceptions.RequestException as e:
            print(f"🚨 Error fetching news from {category_url}: {e}")
            continue

        time.sleep(2)  # Respectful crawling delay

    if not new_articles:
        print("⚠️ No new unique articles found across all categories.")
        return

    # Bulk insert only if new articles exist
    inserted_articles = NewsArticle.objects.bulk_create(new_articles, ignore_conflicts=True)

    print(f"✅ Successfully attempted to add {len(new_articles)} articles.")
    print(f"✅ Actual new records inserted: {len(inserted_articles)}")

if __name__ == "__main__":
    fetch_latest_news()
