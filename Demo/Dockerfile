# ===================================================
# Dockerfile for CS420G Distributed Demo Application
# ===================================================
FROM python:3.11-slim

WORKDIR /app

# Non-root user for security best practices
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY src/ /app/src/

USER appuser

ENV PORT=8080
ENV NODE_ID="Docker-Container-Worker"
ENV APP_VERSION="1.0.0"

EXPOSE 8080

CMD ["python", "src/app.py"]

