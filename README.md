AI-Powered Crisis Response Chatbot
📌 Project Overview

This project presents the design and development of an AI-powered crisis response chatbot built using the Rasa framework. The chatbot is designed to assist users during emergency situations by providing real-time safety guidance, performing risk assessments, and escalating critical cases to emergency services when necessary.

The system leverages Natural Language Processing (NLP) to understand user inputs and manage multi-turn conversations, enabling effective communication during high-stress scenarios such as floods, fires, and medical emergencies.

🎯 Project Objectives

The primary objectives of this project are:

To develop an intelligent conversational agent capable of supporting crisis communication.

To provide users with immediate safety recommendations.

To implement adaptive questioning for risk evaluation.

To design an escalation mechanism for high-risk emergencies.

To create a user-centered prototype interface for improved accessibility.

⚙️ Technologies Used

Rasa Open Source – Conversational AI framework

Python – Backend development

Natural Language Processing (NLP) – Intent recognition and entity extraction

Figma – High-fidelity interface prototype

VS Code – Development environment

🧠 Key Features

✅ Multi-turn conversational capability
✅ Emergency scenario detection (flood, fire, medical)
✅ Location request for contextual assistance
✅ Safety recommendation engine
✅ Automated emergency escalation
✅ Modular and scalable architecture

🏗️ System Architecture

The chatbot follows a modular architecture consisting of:

User Interface

Natural Language Understanding (NLU)

Dialogue Management

Custom Actions

External Service Integration

This structure ensures scalability, maintainability, and efficient processing of emergency interactions.

🚀 Installation and Setup Guide

Follow these steps to run the chatbot locally:

1️⃣ Clone or Download the Project

Place the project folder on your local machine.

2️⃣ Create Virtual Environment
py -3.10 -m venv venv


Activate:

.\venv\Scripts\activate

3️⃣ Install Dependencies
pip install rasa
pip install rasa-sdk

4️⃣ Train the Model
rasa train

5️⃣ Start the Action Server

(Open a new terminal)

rasa run actions

6️⃣ Run the Chatbot

(Open another terminal)

rasa shell


You can now interact with the chatbot.

💬 Example Test Inputs

Try entering:

My house is flooded
Someone is injured
Where is the nearest shelter?

🧪 Testing

The chatbot was tested using simulated emergency conversations to evaluate:

Intent recognition accuracy

Dialogue flow

Response relevance

Escalation triggers

Results indicated reliable performance within the defined scenarios.

🎨 Prototype Design

A high-fidelity mobile interface was developed using Figma to demonstrate how the chatbot could be deployed in a real-world emergency application.

The prototype emphasizes:

Accessibility

High-contrast emergency colors

Cognitive load reduction

User-centered design

⚠️ Limitations

Despite its capabilities, the system has several limitations:

No real-time GPS integration

Dependent on training dataset quality

Limited multilingual support

Not connected to live emergency services

Future work could address these areas to enhance system effectiveness.

🔮 Future Enhancements

Potential improvements include:

Integration with live emergency APIs

Real-time location tracking

Voice-enabled interaction

Multilingual capabilities

Cloud deployment for scalability
