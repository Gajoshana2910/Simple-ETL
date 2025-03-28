# 📌 Simple ETL Pipeline using Python

## 📖 Overview  
This project demonstrates a **basic ETL (Extract, Transform, Load) pipeline** using **Python and Pandas**.  

- **Extract**: Read data from a CSV file.  
- **Transform**: Handle missing values and format data.  
- **Load**: Save the cleaned data into a new CSV file.  

---
## 🏗️ Project Structure  

**Folder Structure:**
- `data/` → Contains input and output CSV files  
  - `data.csv` → Raw dataset  
  - `cleaned_data.csv` → Processed dataset  
- `scripts/` → Contains ETL scripts  
  - `extract.py` → Extract data from CSV  
  - `transform.py` → Clean and process data  
  - `load.py` → Save cleaned data to CSV  
- `etl.py` → Main script to run the ETL pipeline  
- `requirements.txt` → Python dependencies  
- `.gitignore` → Ignore unnecessary files  
- `README.md` → Project documentation  
---

## 🔧 Technologies Used  
- **Python** 🐍  
- **Pandas** 📊  


## 📜 Installation & Setup  

1️⃣ Clone the Repository  
```
git clone https://github.com/Gajoshana2910/Simple-ETL.git
cd Simple-ETL
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the ETL Script
```
python etl.py
```
4️⃣ Check the Output

The cleaned data will be saved in:
```
data/cleaned_data.csv
```
📄 Sample Input (data/data.csv)
```
id,name,age,salary
1,Alice,25,50000
2,Bob,30,
3,Charlie,,70000
4,David,40,80000
```
✅ Sample Output (data/cleaned_data.csv)
```
id,name,age,salary
1,ALICE,25.0,50000.0
2,BOB,30.0,70000.0
3,CHARLIE,32.5,70000.0  <-- Age filled with median (32.5)
4,DAVID,40.0,80000.0
```
## 🛠 How the ETL Works
```
🔹 Extract → Reads data.csv into a Pandas DataFrame.
🔹 Transform → Cleans data by:
    - Filling missing age and salary values with the median.
    - Converting name values to uppercase.
🔹 Load → Saves the cleaned data into a new CSV file.
```
## 📌 Contributing

Want to improve this project? Feel free to fork, modify, and create a pull request!

## 📜 License

This project is licensed under the MIT License 
👉 see the [LICENSE](https://github.com/Gajoshana2910/Simple-ETL/blob/main/LICENSE) file for details.  

## 👨‍💻 Developed by

👉 [Gajalakshmi A K](https://github.com/Gajoshana2910)
