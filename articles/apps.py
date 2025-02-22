import threading
import time
import traceback
from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    fetch_thread_started = False  # Class-level attribute

    def ready(self):
        if not self.fetch_thread_started:  # Ensure only one thread starts
            self.fetch_thread_started = True

            def run_fetcher():
                # ✅ Import inside function to prevent circular import
                from fetch_news import fetch_latest_news  

                while True:
                    try:
                        print("🔄 Running fetch_news.py...")
                        fetch_latest_news()
                    except Exception as e:
                        print(f"🚨 Error in fetcher: {e}")
                        traceback.print_exc()
                    time.sleep(300)  # Sleep for 5 minutes

            thread = threading.Thread(target=run_fetcher, daemon=True)
            thread.start()
