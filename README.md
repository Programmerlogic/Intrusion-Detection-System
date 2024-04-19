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

![Untitled video - Made with Clipchamp](https://github.com/Programmerlogic/Intrusion-Detection-System/assets/90715479/454bf556-b612-41da-8aa4-d4637e4cb62f)

