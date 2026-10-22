# Finy

Finy is a terminal-based personal finance tracker with a lightweight static web frontend.

## Run the web frontend

Open `public/index.html` in a browser, or serve the `public` folder with any static file server. No package installation or build step is needed.

## Deploy to Vercel

Import this repository into Vercel. The included `vercel.json` publishes the `public` directory, so no framework preset, build command, or dependency installation is required.

## Data storage

The web frontend stores accounts and transactions in the current browser's local storage. It does not read or write the Python app's SQLite database in `data/finy.db`, and data is not shared between devices or browsers. A hosted database and API are needed for shared, durable online accounts.
