# 📦 CUI Lost & Found Manager

## 🎯 Overview

The **CUI Lost & Found Manager** is a modern, user-friendly system built with **Flask**, **HTML/CSS**, and a clean **Model-View-Controller (MVC)** architecture.

Designed specifically for universities and large organizations, this application provides an efficient, centralized platform to manage, track, and automatically match lost and found items.

## ✨ Features

### 🔐 Authentication & Security

* **Secure Login System:** Protects administrative and staff access.
* **Role-Based Access:** Distinct access levels for Admins and general Users/Staff.
* **Session-Based Authentication:** Ensures a secure and persistent user experience.

### 🏠 User Dashboard

* **Live Statistics:** Displays real-time data on active, matched, and resolved reports.
* **Quick Navigation:** Intuitive links for immediate access to key functions.
* **Clean UI Layout:** A modern and responsive interface for ease of use.
* **Graph Widgets (Optional):** Supports visual representation of data trends (e.g., reports per month).

### 📝 Reporting System

* **Report Lost Items:** Dedicated form for students or staff to report items they have lost.
* **Report Found Items:** Dedicated form for students or staff to report items they have found.
* **Image Upload Support:** Allows users to upload clear pictures of the item for better identification.
* **Auto-Generated Report IDs:** Unique, traceable identifiers for every report.

### 🔍 Smart Matching Engine

* **Keyword Matching:** Intelligent algorithm suggests potential matches based on item description, category, and location.
* **Auto-Suggest Paired Items:** Proactively links new reports to existing ones that are likely candidates.
* **Match Viewer Page:** A dedicated interface for staff to review, confirm, or reject auto-suggested matches.

### 🛠 Admin Panel

* **Entry Moderation:** Ability to **Approve / Reject** new lost or found entries after review.
* **Comprehensive Reporting View:** Centralized table to view, filter, and sort all lost and found reports.
* **User Management:** Tools to add, modify, or deactivate user accounts.

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.8+** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abdullah-819/Comsats-Lost-Found-item-Manager
    cd cui-lost-found-manager
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup (Assumes SQLite for simplicity, adjust for others):**
    * Initialize the database and create necessary tables. (You will need to run your specific database migration commands, e.g., Flask-Migrate).

5.  **Environment Variables:**
    * Create a `.env` file in the root directory and define essential variables:
        ```env
        SECRET_KEY='your_strong_secret_key'
        FLASK_ENV='development'
        # ... other configurations like DB URI
        ```

6.  **Run the application:**
    ```bash
    flask run
    ```

The application will typically be accessible at `http://127.0.0.1:5000/`.

---

## 📁 Project Structure

The application adheres to a clear Flask project structure, emphasizing the MVC pattern:
