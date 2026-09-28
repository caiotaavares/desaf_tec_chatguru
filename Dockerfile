ARG PYTHON_VERSION=3.11-slim-bookworm

FROM python:${PYTHON_VERSION}

# Cria usuário não-root
RUN useradd --create-home appuser && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

USER appuser
WORKDIR /app

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY --chown=appuser:appuser . .

EXPOSE 8080
CMD ["python", "main.py"]