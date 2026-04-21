FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY main.py .

ENV PATH=/root/.local/bin:$PATH

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3  \
  CMD curl -f http://localhost:5000/health || exit 1

EXPOSE 5000

CMD ["python", "main.py"]

