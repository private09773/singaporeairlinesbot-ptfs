#!/bin/bash
# requirements.sh - cross-platform dependency installer

echo "Detecting package manager..."

if command -v pip >/dev/null 2>&1; then
    echo "Using pip for Python packages..."
    pip install "diseasy"
    pip install "python-dotenv>=1.0,<2.0"
    pip install "aiosqlite>=0.19,<0.20"

elif command -v brew >/dev/null 2>&1; then
    echo "Using Homebrew..."
    brew install diseasy python-dotenv aiosqlite

elif command -v apt-get >/dev/null 2>&1; then
    echo "Using apt-get..."
    sudo apt-get update
    sudo apt-get install -y python3-diseasy python3-dotenv python3-aiosqlite

else
    echo "No supported package manager found!"
    exit 1
fi

echo "Dependencies installed successfully!"