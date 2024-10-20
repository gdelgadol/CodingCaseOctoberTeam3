# Coding Case (Chatbot)

This is the result of a 24-hour challenge, the Coding Case:

Your task is to assist a technology e-commerce company named 'Makers Tech' in creating a ChatBot that responds to and informs users through a graphical interface about the inventory, features, and prices of the products currently available. This is based on the question asked, for example:

- Client: How many computers are currently available?
- ChatBot: At the moment, we have 4 computers; we have 2 HP, 1 Dell, and the other one is Apple. Which one would you like to purchase?
- Client: Tell me more about the Dell computer?

# Installation

## 1. Clone the repository:

```bash
git clone https://github.com/gdelgadol/CodingCaseOctoberTeam3.git
cd CodingCaseOctoberTeam3
```

## 2. **Create a virtual environment (optional)**

### Start it with Python:

```bash
python -m venv venv
```

### Execute or start using it:

- Linux/Mac

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install the LLM model (Llama 3.2 META)

Go to https://ollama.com/ and download the version of Ollama that suits your system. Once installed, use the console to run `ollama run llama3.2`. The model (2.0 GB) will be downloaded automatically.