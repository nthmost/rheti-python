#!/bin/bash
# Deploy latest code to zephyr
# Usage: ./deploy.sh

set -e

echo "→ Pushing to GitHub..."
git push origin master

echo "→ Pulling on zephyr..."
ssh zephyr "cd ~/apps/rheti-python && git pull && venv/bin/pip install -r requirements.txt -q"

echo "→ Restarting service..."
ssh zephyr "sudo systemctl restart rheti"

echo "→ Checking status..."
ssh zephyr "sudo systemctl is-active rheti"

echo "✓ Deployed to https://rheti.nthmost.com"
