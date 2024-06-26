# Intrusion-Detection-System
## Introduction
🛡️ Intrusion Detection Systems (IDS) are like vigilant guardians 👀 protecting computer networks from unauthorized access and malicious activities. They act as digital watchdogs 🐾, constantly monitoring network traffic 📡 for suspicious behavior and potential threats. IDS use sophisticated algorithms 🧠 to analyze data packets 📦, detect anomalies 🚨, and raise alerts 🚩 to alert administrators of potential security breaches. With their keen eyes 👁️‍🗨️ and swift actions, IDS play a crucial role in maintaining the integrity and security of modern IT infrastructures. They're the silent defenders 🛡️ in the ever-evolving landscape of cyber threats, ensuring networks remain safe and resilient against intruders.
## Dataset Description
The Intrusion Detection Evaluation Dataset, specifically the CIC-IDS2017 dataset, is a valuable resource in the field of cybersecurity for assessing and benchmarking intrusion detection systems (IDS). Developed by the Canadian Institute for Cybersecurity (CIC), this dataset contains network traffic data collected from a variety of realistic scenarios and network environments.</br>
CIC-IDS2017 offers a diverse range of traffic patterns, including normal activities as well as various types of cyber attacks such as Denial of Service (DoS), Distributed Denial of Service (DDoS), and malware-related activities. It provides labeled data, enabling researchers and practitioners to train and evaluate IDS algorithms effectively.</br>
With its comprehensive collection of network traffic data, CIC-IDS2017 facilitates the development and testing of intrusion detection techniques across different attack scenarios and network conditions. It serves as a crucial tool for improving the accuracy and robustness of IDS solutions, ultimately enhancing cybersecurity measures in the face of evolving threats.
## Proposed Model
### Workflow Diagram
![Flowchat - Frame 1 (1)](https://github.com/Programmerlogic/Intrusion-Detection-System/assets/90715479/9d824993-7389-4d5e-808a-51b1c69b67af)
## Real-Time Test-Bed Implementation
The real-time operation is performed for the verification of the efficiency of our model. This testing was performed by generating synthetic malicious data packets with the help of some tools which contains the algorithm to generate the attack packets like LOIC for DDos attack, Nmap for portscan & bruteforce,hulk.py etc. </br>
**Aim of the project is to process the result of the captured packets on realtime basis with not only the model accuracy but also the testing time it takes to predict. I have done both efficiently by reducing the actual 80 features to 20 features by PSO & TC algorithm which results in faster computation.** 
## Tech Stack
### Programming Languages:
- Python
### Libraries and Frameworks:
- NumPy
- Pandas
- Seaborn
- Matplotlib
- scikit-learn
### Overview:
- **NumPy**: Used for numerical computing, particularly for handling arrays and matrices.
- **Pandas**: Utilized for data manipulation and analysis, especially for handling structured data through DataFrame objects.
- **Seaborn**: Employed for statistical data visualization, providing high-level interfaces for drawing informative and attractive statistical graphics.
- **Matplotlib**: Used for creating static, animated, and interactive visualizations in Python.
- **scikit-learn**: Employed for machine learning tasks such as classification, regression, clustering, and more. It provides efficient tools for data preprocessing, model selection, evaluation, and deployment.
### Machine Learning Models:
- **DecisionTreeClassifier**: Utilized for classification tasks, where it creates a model that predicts the value of a target variable based on several input variables.
- **RandomForestClassifier**: A type of ensemble learning method based on decision trees, used for classification tasks. It constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees.
### Evaluation Metrics:
- **classification_report**: Used to generate a comprehensive report on the classification performance of a model, including precision, recall, F1-score, and support for each class.
- **accuracy_score**: Employed to measure the accuracy of classification models by comparing the predicted labels to the true labels.
## Installation Steps:
**Step 1.** Run requirements.txt</br>
**Step 2.** Keep the CICFlowmeter folder in a proper place</br>
**Step 3.** Run test.py in the terminal</br>
**Step 4.** A Dialog box will open up. Enter  the CICFlowmeter folder location and password</br>
**Step 5.** Click on the start button. A window will pop up showing the incomming packets and their classes wheather it is attack or not in Binary column and their classification in Multiclass column</br>
## Dependencies
To run this project, make sure you have the following dependencies:</br>
1. Python 🐍</br>
2. Linux 🐧</br>
3. RAM: 8GB 💻</br>
4. Internet Connection 🌐</br>

## Realtime Implementation 
An application software made for **Linux**</br>

https://github.com/Programmerlogic/Intrusion-Detection-System/assets/90715479/c79c964e-e6ca-4232-bf1e-7cde58760ea1

Let us now understand this application software</br>
| Column Name                 | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| **Binary**                  | If 0 Then not an attack packet </br> If 1 Then an attack packet |
| **Multiclass**              | If 0 Then not an attack packet </br> Else an attack packet |
| **Timestamp**               | Date & Time at which the packets hitting in NIC(Network Interface Card)|
| **Src IP**                  | Source IP Address |
| **Src Port**                | Source Port Number |
| **Dst IP**                  | Destination IP Address |
| **Dst Port**                | Destination Port Number |


## LINKS
PPT: https://www.slideshare.net/slideshow/intrusiondetectionsystemppt-cupptx/267410402
