# Electronix-AI---Assignment
Here is your **final `README.md` file**, formatted and ready to upload to your [Electronix AI - Assignment GitHub repository](https://github.com/krishkrishna03/Electronix-AI---Assignment.git):

---

## 📄 **README.md**

```markdown
# 🚀 Electronix AI – Sentiment Analysis Assignment

This project implements a **containerised sentiment analysis application** using:

✅ **FastAPI + GraphQL backend** with Hugging Face Transformers  
✅ **React (TypeScript) frontend** with Apollo Client  
✅ **Fine-tuning CLI script** for custom datasets  
✅ **Docker Compose** to orchestrate backend, frontend, and optional MongoDB

---

## 🗂️ **Folder Structure**

```

Electronix-AI---Assignment/
├── backend/
│   ├── app.py
│   ├── finetune.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── model/
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   └── App.css
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md

````

---

## ⚙️ **Setup & Run Instructions**

### 🐳 **1. Prerequisites**

- **Docker Desktop** installed and running  
- **Node.js** if running frontend locally

---

### 🚀 **2. Running via Docker Compose**

From the project root directory:

```bash
docker compose up --build
````

✔️ **Frontend:** [http://localhost:3000](http://localhost:3000)
✔️ **Backend GraphQL API:** [http://localhost:8000/graphql](http://localhost:8000/graphql)

---

## 📝 **3. Backend API Documentation**

### **GraphQL Endpoint**

```
POST /graphql
```

#### **Sample Query**

```graphql
query {
  predict(text: "I love this product!")
}
```

#### **Sample Response**

```json
{
  "data": {
    "predict": {
      "label": "positive",
      "score": 0.99
    }
  }
}
```

---

## 🔧 **4. Fine-tuning Script**

Fine-tune the model with a labelled dataset:

```bash
python finetune.py -data data.jsonl -epochs 3 -lr 3e-5
```

* **data.jsonl format:**

```
{"text": "Great product!", "label": "positive"}
{"text": "Terrible experience.", "label": "negative"}
```

✔️ Saves updated weights to `./model/` and hot-reloads without API restart.

---

## ✨ **5. Design Decisions**

* **FastAPI + Strawberry GraphQL** for modern API design
* **Hugging Face Transformers** for robust English sentiment analysis
* **Watchdog** for automatic hot-reload of model weights
* **React + TypeScript + Apollo Client** for type-safe frontend
* **Multi-stage Docker build** for optimised image size
* **Optional MongoDB** included for future dataset storage or user auth

---

## ⚡ **6. Approx. CPU vs GPU Fine-tune Times**

| Device   | Dataset Size | Epochs | Time         |
| -------- | ------------ | ------ | ------------ |
| CPU (i5) | 100 samples  | 3      | \~2 minutes  |
| GPU (T4) | 100 samples  | 3      | \~20 seconds |

*Times vary based on dataset size and model architecture.*

---

## 📸 **7. Demo Recording**

🎥 **Watch the demo video here:**
➡️ [Demo Video Link](https://electronix-ai-assignment-98aa.vercel.app/)

*(Replace with your actual unlisted YouTube video URL)*

---

## 🌐 **8. Deployment**

The project can be deployed to:

* **Vercel** (frontend)
* **Render/AWS/GCP** (backend with GPU if needed)

---

## 🤝 **9. Contributing**

1. Fork this repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a pull request

---

## 📜 **10. License**

This project is licensed under the **MIT License**.

---

### 🙏 **Acknowledgements**

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Strawberry GraphQL](https://strawberry.rocks/)
* [Bootstrap](https://getbootstrap.com/)
* [Electronix AI Team](https://github.com/krishkrishna03)

---

> **Team Electronix AI** – Crafted with ❤️ for the assignment submission.

````

