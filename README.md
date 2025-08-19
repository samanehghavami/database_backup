# Database Backup CLI Tool

This is a simple CLI tool for backing up **MySQL** and **PostgreSQL** databases.

---

## Features

- Backup MySQL and PostgreSQL databases
- Save backup files with current date
- Specify custom output directory
- Works on Windows and Linux

---

## Installation

Make sure Git and Python are installed, then install required Python packages:

```bash
pip install click

---
## Usage
python backup.py --type mysql -h localhost -u username -P password -d database_name -p backups
Output: SQL file saved at ./backups/test_db_YYYYMMDD.sql
