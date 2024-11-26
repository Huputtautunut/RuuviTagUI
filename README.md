# How to Run the RuuviTag Data Script

This guide explains how to set up and run the provided Python script for retrieving and displaying RuuviTag data using Quart.

---

## 1. Install Required Packages

Ensure you have Python 3.7 or later installed, then install the necessary Python packages by running the following command:

```bash
pip install quart ruuvitag-sensor bleak
```

## 2. Access the Application

1. Navigate to your project directory in the terminal

2. Run from terminal 
```bash
python server.py 
 ```

## 4. Access the Application
Once the server starts, open a web browser and visit the following URLs:

http://localhost:5000/ Main page.  
http://localhost:5000/basic Basic view page.  
http://localhost:5000/data JSON endpoint to retrieve RuuviTag data.  