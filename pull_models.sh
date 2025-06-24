#!/bin/bash

# ==================================================
# pull_models.sh
# Version: 1.0
# Author: YourName (optional)
# Purpose: Pull all required Ollama models INSIDE the ollama container
# Usage:
#   docker-compose exec ollama bash
#   ./pull_models.sh
# ==================================================

# List of models to pull — update as you add new models
MODELS=(
  "mistral"
  "llama3"
  "deepseek-coder"
  "llama4"
)

echo "📦 Starting model pulls inside container..."

# Loop through models and pull each one
for MODEL in "${MODELS[@]}"; do
  echo "🔹 Pulling: $MODEL ..."
  ollama pull "$MODEL"
  echo "✅ Done: $MODEL"
done

echo "🎉 All models pulled and ready in /root/.ollama"

# Optional: show what models are now available
echo "📋 Available models:"
ollama list
