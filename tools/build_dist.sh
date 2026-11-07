#!/bin/bash
# Copies ONLY the public site into dist/ (never .env files, tools, previews or backups).
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist/hi dist/assets
cp index.html about.html guides.html collaborate.html privacy.html terms.html refund.html cookies.html legal.css dist/
cp hi/*.html dist/hi/
cp assets/logo.jpg assets/qrcode.min.js dist/assets/ && mkdir -p dist/assets/reach && cp assets/reach/*.jpg dist/assets/reach/
echo "dist ready:"; find dist -type f | sort
