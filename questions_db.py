# questions_db.py

questions_db = [
    {
        "theme": "Variabler og Datatyper",
        "difficulty": "Let",
        "question": "Hvad er en variabel, og hvordan opretter man en variabel i Python?",
        "options": [
            {"text": "En variabel er et sted i hukommelsen, hvor data kan gemmes, og man opretter den ved at bruge def.", "correct": False},
            {"text": "En variabel er et sted i hukommelsen, hvor data kan gemmes, og man opretter den ved at bruge var.", "correct": False},
            {"text": "En variabel er et sted i hukommelsen, hvor data kan gemmes, og man opretter den ved at bruge =.", "correct": True},
        ]
    },
    {
        "theme": "Variabler og Datatyper",
        "difficulty": "Middel",
        "question": "Hvad er forskellen mellem mutable og immutable datatyper i Python?",
        "options": [
            {"text": "Mutable datatyper kan ændres efter de er oprettet, mens immutable datatyper ikke kan ændres.", "correct": True},
            {"text": "Immutable datatyper kan ændres efter de er oprettet, mens mutable datatyper ikke kan ændres.", "correct": False},
            {"text": "Mutable datatyper kan ikke ændres efter de er oprettet, mens immutable datatyper kan ændres.", "correct": False},
        ]
    },
    {
        "theme": "Variabler og Datatyper",
        "difficulty": "Svær",
        "question": "Hvad beskriver hukommelseshåndteringen for mutable og immutable objekter i Python?",
        "options": [
            {"text": "Mutable objekter lagres altid i stacken, og immutable objekter lagres i heapen.", "correct": False},
            {"text": "Immutable objekter lagres altid i stacken, og mutable objekter lagres i heapen.", "correct": False},
            {"text": "Mutable objekter kan ændres in-place og deler hukommelse ved kopiering, mens immutable objekter skaber nye objekter ved ændringer.", "correct": True},
        ]
    },
    {
        "theme": "Kontrolstrukturer",
        "difficulty": "Let",
        "question": "Hvordan skriver man en if-else sætning i Python?",
        "options": [
            {"text": "if condition: # code else: # code", "correct": False},
            {"text": "if condition { # code } else { # code }", "correct": False},
            {"text": "if (condition): # code else: # code", "correct": True},
        ]
    },
    {
        "theme": "Kontrolstrukturer",
        "difficulty": "Middel",
        "question": "Hvordan kan man filtrere lige tal fra en liste i Python?",
        "options": [
            {"text": "Ved at bruge en for-løkke og en if-sætning til at tjekke om hvert tal er lige.", "correct": True},
            {"text": "Ved at bruge en while-løkke og en if-sætning til at tjekke om hvert tal er lige.", "correct": False},
            {"text": "Ved at bruge en rekursiv funktion til at tjekke om hvert tal er lige.", "correct": False},
        ]
    },
    {
        "theme": "Kontrolstrukturer",
        "difficulty": "Svær",
        "question": "Hvordan fungerer undtagelseshåndtering i Python?",
        "options": [
            {"text": "Ved at bruge try, catch, og finally blokke til at håndtere undtagelser.", "correct": False},
            {"text": "Ved at bruge try, except, og finally blokke til at håndtere undtagelser.", "correct": True},
            {"text": "Ved at bruge try, except, else, og finally blokke til at håndtere undtagelser.", "correct": False},
        ]
    },
    {
        "theme": "Loops",
        "difficulty": "Let",
        "question": "Hvordan opretter man en for-løkke, der itererer gennem en liste i Python?",
        "options": [
            {"text": "for item from list: # code", "correct": False},
            {"text": "for item in list: # code", "correct": True},
            {"text": "foreach item in list: # code", "correct": False},
        ]
    },
    {
        "theme": "Loops",
        "difficulty": "Middel",
        "question": "Hvordan kan man beregne fakultetet af et tal n ved brug af en while-løkke?",
        "options": [
            {"text": "Ved at multiplicere tallene fra 1 til n ved hjælp af en while-løkke.", "correct": True},
            {"text": "Ved at summere tallene fra 1 til n ved hjælp af en while-løkke.", "correct": False},
            {"text": "Ved at dividere tallene fra 1 til n ved hjælp af en while-løkke.", "correct": False},
        ]
    },
    {
        "theme": "Loops",
        "difficulty": "Svær",
        "question": "Hvordan kan man generere de første n Fibonacci-tal i Python?",
        "options": [
            {"text": "Ved at bruge en for-løkke og en generator.", "correct": True},
            {"text": "Ved at bruge en while-løkke og en rekursiv funktion.", "correct": False},
            {"text": "Ved at bruge en for-løkke og en rekursiv funktion.", "correct": False},
        ]
    },
    {
        "theme": "Funktioner",
        "difficulty": "Let",
        "question": "Hvordan definerer man en funktion, der tager to parametre og returnerer deres sum i Python?",
        "options": [
            {"text": "def add(a, b): return a + b", "correct": True},
            {"text": "function add(a, b) { return a + b }", "correct": False},
            {"text": "def add(a, b): print(a + b)", "correct": False},
        ]
    },
    {
        "theme": "Funktioner",
        "difficulty": "Middel",
        "question": "Hvordan kan man vende en liste af strenge om i Python?",
        "options": [
            {"text": "Ved at bruge en rekursiv funktion til at vende hver streng om.", "correct": False},
            {"text": "Ved at bruge en for-løkke til at vende hver streng om.", "correct": True},
            {"text": "Ved at bruge en while-løkke til at vende hver streng om.", "correct": False},
        ]
    },
    {
        "theme": "Funktioner",
        "difficulty": "Svær",
        "question": "Hvordan kan man beregne summen af alle cifre i et heltal rekursivt i Python?",
        "options": [
            {"text": "Ved at bruge en for-løkke og en generator.", "correct": False},
            {"text": "Ved at bruge en rekursiv funktion, der adderer det sidste ciffer og kalder sig selv med resten.", "correct": True},
            {"text": "Ved at bruge en while-løkke og en rekursiv funktion.", "correct": False},
        ]
    },
    {
        "theme": "Lister og Tupler",
        "difficulty": "Let",
        "question": "Hvad er forskellen mellem en liste og et tuple i Python?",
        "options": [
            {"text": "Lister er mutable, mens tupler er immutable.", "correct": True},
            {"text": "Tupler er mutable, mens lister er immutable.", "correct": False},
            {"text": "Lister kan indeholde dubletter, mens tupler ikke kan.", "correct": False},
        ]
    },
    {
        "theme": "Lister og Tupler",
        "difficulty": "Middel",
        "question": "Hvordan kan man finde det mindste og største tal i en liste i Python?",
        "options": [
            {"text": "Ved at bruge en tuple og en for-løkke til at finde det mindste og største tal.", "correct": False},
            {"text": "Ved at bruge en rekursiv funktion til at finde det mindste og største tal.", "correct": False},
            {"text": "Ved at bruge en tuple og indbyggede funktioner som min og max.", "correct": True},
        ]
    },
    {
        "theme": "Lister og Tupler",
        "difficulty": "Svær",
        "question": "Hvordan fungerer list comprehension i Python?",
        "options": [
            {"text": "Det tillader skabelsen af lister ved hjælp af en enkelt linje kode med en for-løkke og en betingelse.", "correct": True},
            {"text": "Det tillader skabelsen af lister ved hjælp af en enkelt linje kode med en while-løkke og en betingelse.", "correct": False},
            {"text": "Det tillader skabelsen af lister ved hjælp af en rekursiv funktion og en betingelse.", "correct": False},
        ]
    },
    {
        "theme": "Sæt og Dictionaries",
        "difficulty": "Let",
        "question": "Hvordan opretter man et sæt og et dictionary i Python?",
        "options": [
            {"text": "set = {}; dict = []", "correct": False},
            {"text": "set = []; dict = {}", "correct": False},
            {"text": "set = set(); dict = {}", "correct": True},
        ]
    },
    {
        "theme": "Sæt og Dictionaries",
        "difficulty": "Middel",
        "question": "Hvordan kan man lave et dictionary baseret på strengenes længde i en liste?",
        "options": [
            {"text": "Ved at bruge en for-løkke til at oprette nøgler for hver længde og tilføje de tilsvarende strenge som værdier.", "correct": True},
            {"text": "Ved at bruge en rekursiv funktion til at oprette nøgler for hver længde og tilføje de tilsvarende strenge som værdier.", "correct": False},
            {"text": "Ved at bruge en while-løkke til at oprette nøgler for hver længde og tilføje de tilsvarende strenge som værdier.", "correct": False},
        ]
    },
    {
        "theme": "Sæt og Dictionaries",
        "difficulty": "Svær",
        "question": "Hvordan kan man sammenligne frekvensen af elementer i to lister i Python?",
        "options": [
            {"text": "Ved at bruge dictionaries til at tælle frekvensen af elementer og sammenligne disse.", "correct": True},
            {"text": "Ved at bruge rekursive funktioner til at tælle frekvensen af elementer og sammenligne disse.", "correct": False},
            {"text": "Ved at bruge for-løkker til at tælle frekvensen af elementer og sammenligne disse.", "correct": False},
        ]
    },
    {
        "theme": "Filhåndtering",
        "difficulty": "Let",
        "question": "Hvordan åbner og læser man en tekstfil i Python?",
        "options": [
            {"text": "with open('fil.txt', 'r') as file: data = file.read()", "correct": True},
            {"text": "file = open('fil.txt', 'r'); data = file.read()", "correct": False},
            {"text": "file = open('fil.txt', 'w'); data = file.read()", "correct": False},
        ]
    },
    {
        "theme": "Filhåndtering",
        "difficulty": "Middel",
        "question": "Hvordan kan man skrive data til en fil i Python?",
        "options": [
            {"text": "Ved at bruge with open('fil.txt', 'r') as file: file.write(data).", "correct": False},
            {"text": "Ved at bruge with open('fil.txt', 'w') as file: file.write(data).", "correct": True},
            {"text": "Ved at bruge with open('fil.txt', 'a') as file: file.read(data).", "correct": False},
        ]
    },
    {
        "theme": "Filhåndtering",
        "difficulty": "Svær",
        "question": "Hvad er forskellen mellem binær og tekst filhåndtering i Python?",
        "options": [
            {"text": "Der er ingen forskel mellem binær og tekst filhåndtering i Python.", "correct": False},
            {"text": "Tekst filhåndtering bruges til at læse og skrive binære data, mens binær filhåndtering bruges til at læse og skrive tekstdata.", "correct": False},
            {"text": "Tekst filhåndtering bruges til at læse og skrive tekstdata, mens binær filhåndtering bruges til at læse og skrive binære data.", "correct": True},
        ]
    },
    {
        "theme": "Objektorienteret Programmering (OOP)",
        "difficulty": "Let",
        "question": "Hvad er en klasse og et objekt i Python?",
        "options": [
            {"text": "En klasse er en skabelon for objekter, og et objekt er en instans af en klasse.", "correct": True},
            {"text": "Et objekt er en skabelon for klasser, og en klasse er en instans af et objekt.", "correct": False},
            {"text": "En klasse er en skabelon for funktioner, og et objekt er en instans af en funktion.", "correct": False},
        ]
    },
    {
        "theme": "Objektorienteret Programmering (OOP)",
        "difficulty": "Middel",
        "question": "Hvordan kan man definere en klasse Car i Python?",
        "options": [
            {"text": "Ved at bruge class Car:, definere attributter i __init__ metoden, og skrive en metode til beskrivelsen.", "correct": True},
            {"text": "Ved at bruge def Car:, definere attributter i __init__ metoden, og skrive en funktion til beskrivelsen.", "correct": False},
            {"text": "Ved at bruge class Car:, definere attributter i __main__ metoden, og skrive en metode til beskrivelsen.", "correct": False},
        ]
    },
    {
        "theme": "Objektorienteret Programmering (OOP)",
        "difficulty": "Svær",
        "question": "Hvordan kan man implementere arv i Python med en basisklasse og to underklasser?",
        "options": [
            {"text": "Ved at oprette en basisklasse Animal, og bruge class Dog(Animal) og class Cat(Animal) til underklasser.", "correct": True},
            {"text": "Ved at oprette en basisklasse Animal, og bruge def Dog(Animal) og def Cat(Animal) til underklasser.", "correct": False},
            {"text": "Ved at oprette en basisklasse Animal, og bruge class Dog og class Cat til underklasser.", "correct": False},
        ]
    },
    {
        "theme": "Moduler og Biblioteker",
        "difficulty": "Let",
        "question": "Hvordan importerer man et modul i Python?",
        "options": [
            {"text": "import module", "correct": True},
            {"text": "load module", "correct": False},
            {"text": "require module", "correct": False},
        ]
    },
    {
        "theme": "Moduler og Biblioteker",
        "difficulty": "Middel",
        "question": "Hvordan kan man udskrive den aktuelle dato og tid i Python?",
        "options": [
            {"text": "Ved at bruge import datetime, og print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).", "correct": True},
            {"text": "Ved at bruge import datetime, og print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).", "correct": False},
            {"text": "Ved at bruge import datetime, og print(datetime.datetime.now().format('%Y-%m-%d %H:%M:%S')).", "correct": False},
        ]
    },
    {
        "theme": "Moduler og Biblioteker",
        "difficulty": "Svær",
        "question": "Hvad er forskellen mellem standardmoduler og tredjepartsmoduler i Python?",
        "options": [
            {"text": "Standardmoduler er inkluderet i Python installationen, mens tredjepartsmoduler skal installeres separat.", "correct": True},
            {"text": "Tredjepartsmoduler er inkluderet i Python installationen, mens standardmoduler skal installeres separat.", "correct": False},
            {"text": "Der er ingen forskel mellem standardmoduler og tredjepartsmoduler.", "correct": False},
        ]
    },
    {
        "theme": "Algoritmer og Datastrukturer",
        "difficulty": "Let",
        "question": "Hvad er en algoritme?",
        "options": [
            {"text": "En sekvens af instruktioner til at løse et problem.", "correct": True},
            {"text": "En datastruktur til at gemme data effektivt.", "correct": False},
            {"text": "En metode til at designe software applikationer.", "correct": False},
        ]
    },
    {
        "theme": "Algoritmer og Datastrukturer",
        "difficulty": "Middel",
        "question": "Hvordan kan man sortere en liste ved hjælp af boblesortering i Python?",
        "options": [
            {"text": "Ved at bruge to for-løkker til at iterere gennem listen og bytte elementer, hvis de er ude af orden.", "correct": True},
            {"text": "Ved at bruge en while-løkke og en rekursiv funktion til at sortere listen.", "correct": False},
            {"text": "Ved at bruge en for-løkke og en rekursiv funktion til at sortere listen.", "correct": False},
        ]
    },
    {
        "theme": "Algoritmer og Datastrukturer",
        "difficulty": "Svær",
        "question": "Hvordan kan man implementere en binær søgning i en sorteret liste i Python?",
        "options": [
            {"text": "Ved at bruge en rekursiv funktion, der halverer søgeområdet baseret på mål tallet.", "correct": True},
            {"text": "Ved at bruge en for-løkke, der halverer søgeområdet baseret på mål tallet.", "correct": False},
            {"text": "Ved at bruge en while-løkke, der halverer søgeområdet baseret på mål tallet.", "correct": False},
        ]
    }
]
