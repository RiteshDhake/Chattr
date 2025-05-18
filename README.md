# Chattr
Chattr is a lightweight Python chat app that enables real-time messaging over a local network using TCP sockets. Built with Python’s socket module, it supports peer-to-peer or client-server communication and is ideal for learning the basics of network programming and socket communication.


---

## 🚀 Features

- Real-time messaging over TCP
- Peer-to-peer or client-server communication
- Simple terminal-based UI
- No external dependencies — 100% pure Python

---

## 📦 Requirements

- Python 3.x
- Runs on Linux, macOS, and Windows

---

## 🛠️ How It Works

Chattr uses Python’s built-in `socket` module to establish a reliable TCP connection between clients. One machine acts as the server and listens for incoming connections; others connect as clients to send and receive messages.

---

## ⚙️ Setup & Usage

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/chattr.git
cd chattr
