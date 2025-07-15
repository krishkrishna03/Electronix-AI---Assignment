# Stage 1: Build dependencies
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --upgrade pip && \
    pip install --user -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
