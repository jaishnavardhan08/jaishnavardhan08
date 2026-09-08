
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import random

# ============================================================
# FILES
# ============================================================

HOTEL_FILE = "hotels.csv"
PLACE_FILE = "places.csv"
REGISTRATION_FILE = "hotel_registrations.csv"


# ============================================================
# SAMPLE HOTEL DATA
# ============================================================

hotel_data = [
    {
        "name": "Golden Heritage Hotel",
        "city": "Amritsar",
        "type": "Hotel",
        "price": 2500,
        "purpose": "Religious",
        "hospitality": 5,
        "food": 4,
        "view": 4,
        "cleanliness": 5,
        "location": 5
    },
    {
        "name": "Punjab Palace Resort",
        "city": "Amritsar",
        "type": "Resort",
        "price": 5000,
        "purpose": "Recreation",
        "hospitality": 4,
        "food": 5,
        "view": 5,
        "cleanliness": 5,
        "location": 3
    },
    {
        "name": "Seva Dharamshala",
        "city": "Amritsar",
        "type": "Dharamshala",
        "price": 800,
        "purpose": "Religious",
        "hospitality": 4,
        "food": 3,
        "view": 2,
        "cleanliness": 4,
        "location": 5
    },
    {
        "name": "Amritsar Homestay",
        "city": "Amritsar",
        "type": "Homestay",
        "price": 1500,
        "purpose": "Family",
        "hospitality": 5,
        "food": 4,
        "view": 4,
        "cleanliness": 4,
        "location": 4
    },
    {
        "name": "City Business Inn",
        "city": "Amritsar",
        "type": "Hotel",
        "price": 3200,
        "purpose": "Business",
        "hospitality": 4,
        "food": 5,
        "view": 3,
        "cleanliness": 5,
        "location": 5
    },
    {
        "name": "Backpackers Hub",
        "city": "Amritsar",
        "type": "Hostel",
        "price": 900,
        "purpose": "Recreation",
        "hospitality": 4,
        "food": 3,
        "view": 3,
        "cleanliness": 4,
        "location": 5
    },
    {
        "name": "Heritage View Hotel",
        "city": "Amritsar",
        "type": "Hotel",
        "price": 2200,
        "purpose": "Education",
        "hospitality": 5,
        "food": 4,
        "view": 5,
        "cleanliness": 5,
        "location": 4
    }
]


# ============================================================
# SAMPLE PLACES
# ============================================================

place_data = [
    {
        "name": "Golden Temple",
        "city": "Amritsar",
        "category": "Religious",
        "description": "The famous spiritual centre of Amritsar."
    },
    {
        "name": "Jallianwala Bagh",
        "city": "Amritsar",
        "category": "Education",
        "description": "An important historical site in Indian history."
    },
    {
        "name": "Partition Museum",
        "city": "Amritsar",
        "category": "Education",
        "description": "A museum documenting the history of the Partition."
    },
    {
        "name": "Wagah Border",
        "city": "Amritsar",
        "category": "Recreation",
        "description": "Known for its famous border ceremony."
    },
    {
        "name": "Gobindgarh Fort",
        "city": "Amritsar",
        "category": "Recreation",
        "description": "A historic fort with cultural attractions."
    },
    {
        "name": "Durgiana Temple",
        "city": "Amritsar",
        "category": "Religious",
        "description": "A beautiful Hindu temple in Amritsar."
    },
    {
        "name": "Amritsar Heritage Walk",
        "city": "Amritsar",
        "category": "Family",
        "description": "Explore the historic streets and culture of the city."
    }
]


# ============================================================
# CREATE CSV FILES IF THEY DON'T EXIST
# ============================================================

if not os.path.exists(HOTEL_FILE):
    pd.DataFrame(hotel_data).to_csv(HOTEL_FILE, index=False)

if not os.path.exists(PLACE_FILE):
    pd.DataFrame(place_data).to_csv(PLACE_FILE, index=False)


# ============================================================
# LOAD DATA
# ============================================================

hotels = pd.read_csv(HOTEL_FILE)
places = pd.read_csv(PLACE_FILE)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Valencia - Smart Travel Assistant")
root.geometry("950x700")
root.minsize(850, 600)

current_language = "English"


# ============================================================
# COLORS / BASIC UI
# ============================================================

BG = "#F5F5F5"
WHITE = "#FFFFFF"

root.configure(bg=BG)


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def heading(text):
    label = tk.Label(
        root,
        text=text,
        font=("Arial", 24, "bold"),
        bg=BG
    )
    label.pack(pady=15)


def button(parent, text, command, width=20):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        font=("Arial", 11, "bold"),
        padx=8,
        pady=8
    )


# ============================================================
# LANGUAGE SCREEN
# ============================================================

def language_screen():

    clear_window()

    tk.Label(
        root,
        text="✈️ Valencia",
        font=("Arial", 30, "bold"),
        bg=BG
    ).pack(pady=(100, 10))

    tk.Label(
        root,
        text="Your smart travel companion",
        font=("Arial", 15),
        bg=BG
    ).pack(pady=5)

    tk.Label(
        root,
        text="Choose your language / भाषा चुनें",
        font=("Arial", 14),
        bg=BG
    ).pack(pady=30)

    button(
        root,
        "🇬🇧 English",
        lambda: choose_language("English"),
        25
    ).pack(pady=10)

    button(
        root,
        "🇮🇳 हिन्दी",
        lambda: choose_language("Hindi"),
        25
    ).pack(pady=10)


def choose_language(language):
    global current_language
    current_language = language
    home_screen()


# ============================================================
# HOME SCREEN
# ============================================================

def home_screen():

    clear_window()

    heading("✈️ Valencia")

    tk.Label(
        root,
        text="Plan your journey according to YOUR preferences.",
        font=("Arial", 13),
        bg=BG
    ).pack(pady=5)

    frame = tk.Frame(root, bg=BG)
    frame.pack(pady=40)

    button(
        frame,
        "🗺️ Plan My Trip",
        preference_screen,
        25
    ).grid(row=0, column=0, padx=15, pady=15)

    button(
        frame,
        "🏨 Register Your Hotel",
        hotel_registration,
        25
    ).grid(row=0, column=1, padx=15, pady=15)

    button(
        frame,
        "🧠 Culture Quiz",
        lambda: culture_quiz("Amritsar"),
        25
    ).grid(row=1, column=0, padx=15, pady=15)

    button(
        frame,
        "ℹ️ About",
        about_screen,
        25
    ).grid(row=1, column=1, padx=15, pady=15)


# ============================================================
# PREFERENCE SCREEN
# ============================================================

def preference_screen():

    clear_window()

    heading("🧳 Tell Us About Your Trip")

    main_frame = tk.Frame(root, bg=BG)
    main_frame.pack(fill="both", expand=True, padx=50)

    # Destination
    tk.Label(
        main_frame,
        text="📍 Where do you want to visit?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=0, column=0, sticky="w", pady=8)

    destination = ttk.Combobox(
        main_frame,
        values=["Amritsar"],
        width=30,
        state="readonly"
    )
    destination.current(0)
    destination.grid(row=0, column=1, pady=8)

    # Budget
    tk.Label(
        main_frame,
        text="💰 Your hotel budget per night?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=1, column=0, sticky="w", pady=8)

    budget = tk.Entry(main_frame, width=33)
    budget.grid(row=1, column=1, pady=8)

    # Stay
    tk.Label(
        main_frame,
        text="🏠 Preferred type of stay?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=2, column=0, sticky="w", pady=8)

    stay = ttk.Combobox(
        main_frame,
        values=[
            "Hotel",
            "Resort",
            "Homestay",
            "Dharamshala",
            "Hostel"
        ],
        width=30,
        state="readonly"
    )
    stay.current(0)
    stay.grid(row=2, column=1, pady=8)

    # Purpose
    tk.Label(
        main_frame,
        text="🎯 Purpose of your trip?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=3, column=0, sticky="w", pady=8)

    purpose = ttk.Combobox(
        main_frame,
        values=[
            "Religious",
            "Education",
            "Recreation",
            "Business",
            "Family"
        ],
        width=30,
        state="readonly"
    )
    purpose.current(0)
    purpose.grid(row=3, column=1, pady=8)

    # Priority
    tk.Label(
        main_frame,
        text="⭐ What matters MOST in your hotel?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=4, column=0, sticky="w", pady=8)

    priority = ttk.Combobox(
        main_frame,
        values=[
            "Hospitality",
            "Food",
            "View",
            "Cleanliness",
            "Location",
            "Price"
        ],
        width=30,
        state="readonly"
    )
    priority.current(0)
    priority.grid(row=4, column=1, pady=8)

    # Travelling with
    tk.Label(
        main_frame,
        text="👨‍👩‍👧 Travelling with?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=5, column=0, sticky="w", pady=8)

    travellers = ttk.Combobox(
        main_frame,
        values=[
            "Solo",
            "Friends",
            "Family"
        ],
        width=30,
        state="readonly"
    )
    travellers.current(0)
    travellers.grid(row=5, column=1, pady=8)

    # Duration
    tk.Label(
        main_frame,
        text="🗓️ Number of days?",
        font=("Arial", 12, "bold"),
        bg=BG
    ).grid(row=6, column=0, sticky="w", pady=8)

    duration = ttk.Combobox(
        main_frame,
        values=[
            "1-2 days",
            "3-5 days",
            "6-10 days",
            "10+ days"
        ],
        width=30,
        state="readonly"
    )
    duration.current(1)
    duration.grid(row=6, column=1, pady=8)

    button(
        root,
        "✨ PLAN MY TRIP",
        lambda: generate_recommendations(
            destination.get(),
            budget.get(),
            stay.get(),
            purpose.get(),
            priority.get(),
            travellers.get(),
            duration.get()
        ),
        25
    ).pack(pady=15)

    button(
        root,
        "← Back",
        home_screen,
        15
    ).pack(pady=5)


# ============================================================
# RECOMMENDATION ENGINE
# ============================================================

def generate_recommendations(
    destination,
    budget_text,
    stay_type,
    purpose,
    priority,
    travellers,
    duration
):

    try:
        budget_value = float(budget_text)
    except ValueError:
        messagebox.showerror(
            "Budget",
            "Please enter a valid budget."
        )
        return

    filtered = hotels[
        hotels["city"].str.lower() ==
        destination.lower()
    ].copy()

    if filtered.empty:
        messagebox.showinfo(
            "No Results",
            "We currently don't have hotels for this destination."
        )
        return

    scores = []

    for index, hotel in filtered.iterrows():

        score = 0

        # Budget
        if hotel["price"] <= budget_value:
            score += 30
        elif hotel["price"] <= budget_value * 1.2:
            score += 15

        # Stay type
        if hotel["type"] == stay_type:
            score += 20

        # Purpose
        if hotel["purpose"] == purpose:
            score += 20

        # Main priority
        if priority == "Hospitality":
            score += hotel["hospitality"] * 5

        elif priority == "Food":
            score += hotel["food"] * 5

        elif priority == "View":
            score += hotel["view"] * 5

        elif priority == "Cleanliness":
            score += hotel["cleanliness"] * 5

        elif priority == "Location":
            score += hotel["location"] * 5

        elif priority == "Price":
            if hotel["price"] <= budget_value:
                score += 25

        scores.append((index, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    show_recommendations(
        filtered,
        scores,
        destination,
        purpose,
        budget_value
    )


# ============================================================
# RECOMMENDATION DISPLAY
# ============================================================

def show_recommendations(
    filtered,
    scores,
    destination,
    purpose,
    budget
):

    clear_window()

    heading("✨ Your Personalized Trip")

    tk.Label(
        root,
        text=f"📍 {destination}   |   🎯 {purpose}   |   💰 ₹{budget:.0f}/night",
        font=("Arial", 12, "bold"),
        bg=BG
    ).pack(pady=5)

    # Hotel section
    tk.Label(
        root,
        text="🏨 RECOMMENDED STAYS",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=10)

    hotel_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid")
    hotel_frame.pack(fill="x", padx=60, pady=5)

    for rank, (index, score) in enumerate(scores[:3], start=1):

        hotel = filtered.loc[index]

        percentage = min(int(score), 100)

        text = (
            f"{rank}. {hotel['name']}     "
            f"{percentage}% Match\n"
            f"   🏠 {hotel['type']}    "
            f"💰 ₹{hotel['price']}/night    "
            f"📍 {hotel['location']}/5 location\n"
            f"   ⭐ Hospitality {hotel['hospitality']}/5   "
            f"🍴 Food {hotel['food']}/5"
        )

        tk.Label(
            hotel_frame,
            text=text,
            font=("Arial", 11),
            justify="left",
            anchor="w",
            bg=WHITE
        ).pack(fill="x", padx=15, pady=10)

    # Places section
    tk.Label(
        root,
        text="📍 PLACES YOU MAY LIKE",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=10)

    matching_places = places[
        (places["city"].str.lower() == destination.lower()) &
        (
            (places["category"] == purpose) |
            (places["category"] == "Family")
        )
    ]

    if matching_places.empty:
        matching_places = places[
            places["city"].str.lower() == destination.lower()
        ]

    place_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid")
    place_frame.pack(fill="x", padx=60, pady=5)

    for _, place in matching_places.head(4).iterrows():

        text = (
            f"📍 {place['name']}\n"
            f"   {place['description']}"
        )

        tk.Label(
            place_frame,
            text=text,
            font=("Arial", 10),
            justify="left",
            anchor="w",
            bg=WHITE
        ).pack(fill="x", padx=15, pady=7)

    # Bottom buttons
    bottom = tk.Frame(root, bg=BG)
    bottom.pack(pady=15)

    button(
        bottom,
        "💡 Culture Quiz",
        lambda: culture_quiz(destination),
        18
    ).grid(row=0, column=0, padx=5)

    button(
        bottom,
        "🏠 Home",
        home_screen,
        18
    ).grid(row=0, column=1, padx=5)


# ============================================================
# HOTEL REGISTRATION
# ============================================================

def hotel_registration():

    clear_window()

    heading("🏨 Register Your Property")

    frame = tk.Frame(root, bg=BG)
    frame.pack(pady=10)

    fields = [
        "Hotel Name",
        "City",
        "Type",
        "Price per Night",
        "Speciality",
        "Food",
        "Facilities"
    ]

    entries = {}

    for i, field in enumerate(fields):

        tk.Label(
            frame,
            text=field + ":",
            font=("Arial", 11, "bold"),
            bg=BG
        ).grid(row=i, column=0, sticky="w", padx=10, pady=7)

        entry = tk.Entry(frame, width=35)
        entry.grid(row=i, column=1, padx=10, pady=7)

        entries[field] = entry

    def save_hotel():

        data = {
            "hotel_name": entries["Hotel Name"].get(),
            "city": entries["City"].get(),
            "type": entries["Type"].get(),
            "price": entries["Price per Night"].get(),
            "speciality": entries["Speciality"].get(),
            "food": entries["Food"].get(),
            "facilities": entries["Facilities"].get()
        }

        df = pd.DataFrame([data])

        if os.path.exists(REGISTRATION_FILE):
            df.to_csv(
                REGISTRATION_FILE,
                mode="a",
                header=False,
                index=False
            )
        else:
            df.to_csv(
                REGISTRATION_FILE,
                index=False
            )

        messagebox.showinfo(
            "Success",
            "Your hotel has been registered successfully!"
        )

        for entry in entries.values():
            entry.delete(0, tk.END)

    button(
        root,
        "💾 Register Hotel",
        save_hotel,
        25
    ).pack(pady=15)

    button(
        root,
        "← Back",
        home_screen,
        15
    ).pack()


# ============================================================
# CULTURE QUIZ
# ============================================================

quiz_questions = {
    "Amritsar": [
        {
            "question": "What is another name for the Golden Temple?",
            "options": [
                "Harmandir Sahib",
                "India Gate",
                "Charminar",
                "Red Fort"
            ],
            "answer": "Harmandir Sahib"
        },
        {
            "question": "Amritsar is located in which Indian state?",
            "options": [
                "Punjab",
                "Rajasthan",
                "Gujarat",
                "Kerala"
            ],
            "answer": "Punjab"
        },
        {
            "question": "Which famous border ceremony takes place near Amritsar?",
            "options": [
                "Wagah Border Ceremony",
                "Republic Day Parade",
                "Boat Festival",
                "Desert Festival"
            ],
            "answer": "Wagah Border Ceremony"
        },
        {
            "question": "Which food is strongly associated with Punjabi cuisine?",
            "options": [
                "Chole Bhature",
                "Dhokla",
                "Idli",
                "Appam"
            ],
            "answer": "Chole Bhature"
        },
        {
            "question": "Which drink is popular in Punjab?",
            "options": [
                "Sweet Lassi",
                "Kahwa",
                "Filter Coffee",
                "Sol Kadhi"
            ],
            "answer": "Sweet Lassi"
        }
    ]
}


def culture_quiz(city):

    clear_window()

    heading(f"🧠 {city} Culture Quiz")

    questions = quiz_questions.get(
        city,
        quiz_questions["Amritsar"]
    )

    random.shuffle(questions)

    score = [0]
    question_number = [0]

    question_label = tk.Label(
        root,
        text="",
        font=("Arial", 15, "bold"),
        wraplength=700,
        bg=BG
    )
    question_label.pack(pady=30)

    selected_answer = tk.StringVar()

    option_buttons = []

    for _ in range(4):

        rb = tk.Radiobutton(
            root,
            text="",
            variable=selected_answer,
            value="",
            font=("Arial", 12),
            bg=BG
        )

        rb.pack(anchor="w", padx=200, pady=5)

        option_buttons.append(rb)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 12, "bold"),
        bg=BG
    )
    result_label.pack(pady=15)

    def load_question():

        selected_answer.set("")
        result_label.config(text="")

        q = questions[question_number[0]]

        question_label.config(
            text=f"Q{question_number[0] + 1}. {q['question']}"
        )

        for i, option in enumerate(q["options"]):

            option_buttons[i].config(
                text=option,
                value=option
            )

    def next_question():

        answer = selected_answer.get()

        if answer == "":
            messagebox.showwarning(
                "Choose an answer",
                "Please select an answer."
            )
            return

        correct = questions[question_number[0]]["answer"]

        if answer == correct:
            score[0] += 1
            result_label.config(text="✅ Correct!")
        else:
            result_label.config(
                text=f"❌ Correct answer: {correct}"
            )

        question_number[0] += 1

        if question_number[0] >= len(questions):

            messagebox.showinfo(
                "Quiz Complete",
                f"You scored {score[0]}/{len(questions)}!"
            )

            home_screen()

        else:
            root.after(1000, load_question)

    button(
        root,
        "Next Question →",
        next_question,
        20
    ).pack(pady=15)

    button(
        root,
        "← Home",
        home_screen,
        15
    ).pack()

    load_question()


# ============================================================
# ABOUT SCREEN
# ============================================================

def about_screen():

    clear_window()

    heading("ℹ️ About Valencia")

    text = """
Valencia is a smart travel assistant designed
to make travelling more personal and meaningful.

It considers:

• Your budget
• Your preferred stay
• Purpose of your trip
• Your hotel priorities
• Your travel group

It then recommends suitable hotels and
places according to your preferences.

The app also allows new hotels to register
their properties and includes interactive
culture quizzes to help travellers learn
about the places they visit.
"""

    tk.Label(
        root,
        text=text,
        font=("Arial", 12),
        justify="left",
        bg=BG
    ).pack(pady=30)

    button(
        root,
        "← Home",
        home_screen,
        15
    ).pack()


# ============================================================
# START APP
# ============================================================

language_screen()

root.mainloop()

