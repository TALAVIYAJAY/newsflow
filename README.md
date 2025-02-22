
# **Super Bowl Article Aggregation - Container-Based Web Application**  

## **Overview**  
This project is a containerized web application that fetches and displays the latest 2025 Super Bowl articles. It consists of three main services:  

- **Backend:** Django REST API to fetch and store news articles.  
- **Frontend:** A simple UI to display news articles.  
- **Database:** PostgreSQL for storing articles.  

---

## **Features**  
✅ REST API to serve the latest news.  
✅ Scheduled background job to fetch articles periodically.  
✅ Database storage for articles (title, source, URL, timestamp, summary).  
✅ Docker-based deployment using `docker-compose`.  

---

## **Setup Instructions**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/TALAVIYAJAY/newsflow.git
cd newsflow
```

### **2️⃣ Build and Run Containers**  
```sh
docker-compose up --build -d
```

### **3️⃣ Verify Running Containers**  
```sh
docker ps
```

### **4️⃣ Access the Application**  
- **Backend API:** [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)  
---

## **Stopping & Restarting**  

### **🛑 Stop the Project**  
```sh
docker-compose down
```

### **🚀 Restart the Project**  
```sh
docker-compose up -d
```

---

## **Project Structure**  
```
📦 newsflow
 ┣ 📂 articles           # Django app for handling news articles
 ┣ 📂 newsflow           # Django project directory
 ┣ 📂 __pycache__        # Python cache files (ignored in Git)
 ┣ 📜 .env               # Environment variables file
 ┣ 📜 .gitignore         # Git ignore file
 ┣ 📜 db_initialized     # (Possibly a marker file for DB setup)
 ┣ 📜 docker-compose.yml # Docker orchestration
 ┣ 📜 Dockerfile         # Backend containerization
 ┣ 📜 fetch_news.py      # Script to fetch news articles
 ┣ 📜 manage.py          # Django management script
 ┣ 📜 README.md          # Project documentation
 ┣ 📜 requirements.txt   # Python dependencies
```

---

## **Video Explanation**  
A detailed walkthrough of the project can be found here: [Loom Video Link](https://drive.google.com/drive/folders/1SttEyAltCFNUqH5EWBviiDyY7LU0_nhm?usp=sharing)


