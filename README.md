# Complaint Management System — Desktop App (Python + Tkinter)

**Complaint Management System** is a simple, local desktop application built with **Python**, **Tkinter** and **SQLite3**.  
It provides a clean GUI for users to submit complaints and a secured admin interface to view all submitted complaints.

---

## Table of contents

- [Project overview](#project-overview)  
- [Features](#features)  
- [Tech stack](#tech-stack)  
- [Folder structure](#folder-structure)  
- [Getting started](#getting-started)  
  - [Requirements](#requirements)  
  - [Install & Run](#install--run)  
- [Usage](#usage)  
- [Database schema](#database-schema)  
- [Admin credentials](#admin-credentials)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)

---

## Project overview

This project implements a desktop Complaint Management System intended for learning and small-scale/local use.  
Users can submit complaints through a friendly form (firstname, lastname, address, gender, comment). Submitted complaints are stored locally in an SQLite database (`complaintDB.db`). An admin can log in to view all complaints in a table (Tkinter `Treeview`).

This is ideal for:
- Students practicing GUI + database integration with Python.  
- Small offices or departments that want a simple local complaint tracker without a full backend.

---

## Features

- Simple and responsive **Tkinter** GUI  
- Submit new complaints (Firstname, Lastname, Address, Gender, Comment)  
- Admin login page to view complaints in a table (Treeview)  
- Back button navigation to return to the home screen  
- Local storage using **SQLite3** (`complaintDB.db`)  
- Easy to extend (add edit/delete, export, or authentication)

---

## Tech stack

- Python 3.10+ (tested with Python 3.11 / 3.13)  
- Tkinter (GUI) — built-in with Python distributions  
- SQLite3 (local DB) — Python standard library `sqlite3`  
- Pillow (`PIL`) — optional, for showing images (`book.png`)

---

## Folder structure

