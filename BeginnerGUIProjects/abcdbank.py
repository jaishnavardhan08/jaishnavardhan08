import tkinter as tk
from tkinter import messagebox
import pandas as pd
import re
import csv
import os
import hashlib
from datetime import datetime

# ============================================================
# ABCD - BASIC AI-FREE FINANCIAL ASSISTANT
# ============================================================

# -------------------- COLORS --------------------

BG = "#f4f7fb"
BLUE = "#2563eb"
DARK = "#172033"
WHITE = "#ffffff"
GREEN = "#16a34a"
ORANGE = "#f59e0b"
RED = "#dc2626"
GRAY = "#64748b"

# -------------------- FILE SETTINGS --------------------

CSV_FILE = "abcd_data.csv"

# These columns are used for BOTH login information and transactions.
CSV_COLUMNS = [
    "username",
    "password_hash",
    "transaction_amount",
    "record_type",
    "date_time"
]

current_user = None


# ============================================================
# CSV FUNCTIONS
# ============================================================

def create_csv_if_needed():
    """Create the CSV file if it does not already exist."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=CSV_COLUMNS)
        df.to_csv(CSV_FILE, index=False)


def hash_password(password):
    """Convert the password into a hash instead of saving it as plain text."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_data():
    """Load the CSV safely."""
    create_csv_if_needed()

    try:
        return pd.read_csv(CSV_FILE)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        return pd.DataFrame(columns=CSV_COLUMNS)


def save_record(username, password_hash="", transaction_amount="",
                record_type="login"):
    """Add one login or transaction record to the same CSV file."""

    create_csv_if_needed()

    new_record = pd.DataFrame([{
        "username": username,
        "password_hash": password_hash,
        "transaction_amount": transaction_amount,
        "record_type": record_type,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    new_record.to_csv(
        CSV_FILE,
        mode="a",
        header=False,
        index=False
    )


def find_user(username):
    """Find the first saved account for a username."""

    df = load_data()

    if df.empty:
        return None

    matches = df[
        (df["username"].astype(str).str.lower() == username.lower())
        & (df["password_hash"].fillna("").astype(str) != "")
    ]

    if matches.empty:
        return None

    return matches.iloc[0]


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("ABCD BANK - Financial Assistant")
root.geometry("900x600")
root.configure(bg=BG)
root.resizable(False, False)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="🤝 ABCD BANK",
    font=("Arial", 28, "bold"),
    bg=BG,
    fg=DARK
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Simple tools for safer and smarter financial decisions",
    font=("Arial", 12),
    bg=BG,
    fg=GRAY
)

subtitle.pack(pady=(0, 20))


# ============================================================
# FUNCTIONS
# ============================================================

def clear_screen():
    """Remove everything from the main content area."""
    for widget in content_frame.winfo_children():
        widget.destroy()


# ============================================================
# LOGIN
# ============================================================

def show_login_popup():
    """Open the login/register popup."""

    login_window = tk.Toplevel(root)
    login_window.title("Login - ABCD BANK")
    login_window.geometry("400x330")
    login_window.configure(bg=WHITE)
    login_window.resizable(False, False)

    login_window.transient(root)
    login_window.grab_set()

    tk.Label(
        login_window,
        text="🔐 Login to ABCD BANK",
        font=("Arial", 20, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack(pady=(25, 20))

    tk.Label(
        login_window,
        text="Username",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack()

    username_entry = tk.Entry(
        login_window,
        width=30,
        font=("Arial", 12)
    )
    username_entry.pack(pady=(5, 15))

    tk.Label(
        login_window,
        text="Password",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack()

    password_entry = tk.Entry(
        login_window,
        width=30,
        font=("Arial", 12),
        show="*"
    )
    password_entry.pack(pady=(5, 15))

    def login():

        global current_user

        username = username_entry.get().strip()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Details",
                "Please enter both username and password.",
                parent=login_window
            )
            return

        # Allow only simple usernames for this beginner prototype.
        if not re.match(r"^[A-Za-z0-9_]+$", username):
            messagebox.showwarning(
                "Invalid Username",
                "Username can contain only letters, numbers and underscores.",
                parent=login_window
            )
            return

        existing_user = find_user(username)
        password_hash = hash_password(password)

        # ----------------------------------------------------
        # NEW USER
        # ----------------------------------------------------
        if existing_user is None:

            save_record(
                username=username,
                password_hash=password_hash,
                record_type="login"
            )

            current_user = username

            messagebox.showinfo(
                "Account Created",
                f"Welcome, {username}!\n\n"
                "Your account has been saved.",
                parent=login_window
            )

            update_login_button()
            login_window.destroy()
            show_home()

        # ----------------------------------------------------
        # EXISTING USER
        # ----------------------------------------------------
        else:

            saved_hash = str(existing_user["password_hash"])

            if password_hash == saved_hash:

                current_user = username

                # Save a separate login event to the same CSV.
                save_record(
                    username=username,
                    password_hash="",
                    record_type="login"
                )

                messagebox.showinfo(
                    "Login Successful",
                    f"Welcome back, {username}!",
                    parent=login_window
                )

                update_login_button()
                login_window.destroy()
                show_home()

            else:
                messagebox.showerror(
                    "Login Failed",
                    "Incorrect username or password.",
                    parent=login_window
                )

    tk.Button(
        login_window,
        text="🔐 Login",
        command=login,
        bg=BLUE,
        fg=WHITE,
        font=("Arial", 12, "bold"),
        padx=35,
        pady=8,
        relief="flat"
    ).pack(pady=10)

    tk.Label(
        login_window,
        text="New username = new account",
        font=("Arial", 9),
        bg=WHITE,
        fg=GRAY
    ).pack(pady=5)

    username_entry.focus()
    login_window.bind("<Return>", lambda event: login())


def logout():
    """Log the current user out."""

    global current_user

    current_user = None
    update_login_button()
    show_home()

    messagebox.showinfo(
        "Logged Out",
        "You have been logged out."
    )


def update_login_button():
    """Update the top-right login/logout button."""

    if current_user:
        login_button.config(
            text=f"👤 {current_user} | Logout",
            command=logout
        )
    else:
        login_button.config(
            text="🔐 Login",
            command=show_login_popup
        )


# ============================================================
# HOME
# ============================================================

def show_home():

    clear_screen()

    if current_user:
        welcome_text = f"Welcome, {current_user}! 👋"
        account_text = "You are currently logged in."
    else:
        welcome_text = "Welcome to ABCD 👋"
        account_text = "Please login to save your spending transactions."

    heading = tk.Label(
        content_frame,
        text=welcome_text,
        font=("Arial", 22, "bold"),
        bg=WHITE,
        fg=DARK
    )

    heading.pack(pady=25)

    description = tk.Label(
        content_frame,
        text=(
            "ABCD helps users understand their spending,\n"
            "identify suspicious financial messages,\n"
            "and learn basic financial concepts."
        ),
        font=("Arial", 13),
        bg=WHITE,
        fg=DARK,
        justify="center"
    )

    description.pack(pady=10)

    tk.Label(
        content_frame,
        text=account_text,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=GREEN if current_user else ORANGE
    ).pack(pady=20)


# ============================================================
# SCAM DETECTOR
# ============================================================

def show_scam_detector():

    clear_screen()

    tk.Label(
        content_frame,
        text="🚨 Scam Detector",
        font=("Arial", 22, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack(pady=20)

    tk.Label(
        content_frame,
        text="Paste a suspicious SMS, email or WhatsApp message:",
        font=("Arial", 11),
        bg=WHITE,
        fg=DARK
    ).pack()

    message_box = tk.Text(
        content_frame,
        height=8,
        width=80,
        font=("Arial", 11)
    )

    message_box.pack(pady=15)

    result_label = tk.Label(
        content_frame,
        text="",
        font=("Arial", 14, "bold"),
        bg=WHITE
    )

    result_label.pack(pady=10)

    scam_words = [
        "urgent",
        "immediately",
        "otp",
        "pin",
        "password",
        "blocked",
        "verify now",
        "click here",
        "send money",
        "prize",
        "lottery",
        "refund",
        "cashback",
        "guaranteed",
        "investment"
    ]

    def check_message():

        message = message_box.get("1.0", tk.END).lower()

        if not message.strip():
            messagebox.showwarning(
                "Empty Message",
                "Please enter a message."
            )
            return

        found = []

        for word in scam_words:
            if word in message:
                found.append(word)

        money_found = re.search(
            r"(₹|rs\.?|rupees)\s?\d+",
            message
        )

        risk_score = len(found) * 10

        if money_found:
            risk_score += 15

        risk_score = min(risk_score, 100)

        if risk_score >= 60:

            result_label.config(
                text=f"🔴 HIGH RISK — Score: {risk_score}/100",
                fg=RED
            )

        elif risk_score >= 30:

            result_label.config(
                text=f"🟠 MEDIUM RISK — Score: {risk_score}/100",
                fg=ORANGE
            )

        else:

            result_label.config(
                text=f"🟢 LOW RISK — Score: {risk_score}/100",
                fg=GREEN
            )

        if found:

            details = (
                "Warning signs detected:\n\n"
                + ", ".join(found)
                + "\n\nNever share OTPs, PINs or passwords."
            )

        else:

            details = (
                "No obvious warning keywords were detected.\n\n"
                "However, this does not guarantee that "
                "the message is safe."
            )

        messagebox.showinfo(
            "ABCD Analysis",
            details
        )

    tk.Button(
        content_frame,
        text="🔍 Analyze Message",
        command=check_message,
        bg=BLUE,
        fg=WHITE,
        font=("Arial", 12, "bold"),
        padx=20,
        pady=10,
        relief="flat"
    ).pack()


# ============================================================
# SPENDING ANALYZER
# ============================================================

def show_spending_analyzer():

    clear_screen()

    tk.Label(
        content_frame,
        text="📊 Spending Analyzer",
        font=("Arial", 22, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack(pady=20)

    if not current_user:

        tk.Label(
            content_frame,
            text="🔐 Please login before saving transactions.",
            font=("Arial", 11, "bold"),
            bg=WHITE,
            fg=ORANGE
        ).pack(pady=5)

    tk.Label(
        content_frame,
        text=(
            "Enter transaction amounts separated by commas.\n"
            "Example: 500, 1200, 300, 4500"
        ),
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY
    ).pack()

    amount_entry = tk.Entry(
        content_frame,
        width=60,
        font=("Arial", 12)
    )

    amount_entry.pack(pady=15)

    result_label = tk.Label(
        content_frame,
        text="",
        font=("Arial", 12),
        bg=WHITE,
        fg=DARK,
        justify="left"
    )

    result_label.pack(pady=20)

    def analyze():

        text = amount_entry.get()

        if not current_user:
            messagebox.showwarning(
                "Login Required",
                "Please login first so your transactions can be saved."
            )
            return

        try:

            amounts = [
                float(x.strip())
                for x in text.split(",")
                if x.strip()
            ]

            if not amounts:
                raise ValueError

            if any(amount <= 0 for amount in amounts):
                raise ValueError

            # Pandas DataFrame
            df = pd.DataFrame({
                "amount": amounts
            })

            total = df["amount"].sum()
            average = df["amount"].mean()
            largest = df["amount"].max()

            result_label.config(
                text=(
                    f"💰 Total Spending: ₹{total:,.2f}\n\n"
                    f"📌 Average Transaction: ₹{average:,.2f}\n\n"
                    f"🔝 Largest Transaction: ₹{largest:,.2f}\n\n"
                    f"🧾 Number of Transactions: {len(df)}"
                )
            )

            # ------------------------------------------------
            # SAVE EVERY TRANSACTION TO THE SAME CSV FILE
            # ------------------------------------------------

            for amount in amounts:

                save_record(
                    username=current_user,
                    password_hash="",
                    transaction_amount=amount,
                    record_type="transaction"
                )

            messagebox.showinfo(
                "Saved",
                f"{len(amounts)} transaction(s) saved for {current_user}."
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter positive numbers separated by commas."
            )

    tk.Button(
        content_frame,
        text="📊 Analyze & Save Spending",
        command=analyze,
        bg=BLUE,
        fg=WHITE,
        font=("Arial", 12, "bold"),
        padx=20,
        pady=10,
        relief="flat"
    ).pack()


# ============================================================
# FINANCIAL LITERACY
# ============================================================

def show_financial_literacy():

    clear_screen()

    tk.Label(
        content_frame,
        text="💡 Financial Literacy",
        font=("Arial", 22, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack(pady=20)

    tk.Label(
        content_frame,
        text="Choose a topic to learn:",
        font=("Arial", 12),
        bg=WHITE,
        fg=DARK
    ).pack(pady=10)

    explanation = tk.Label(
        content_frame,
        text="",
        font=("Arial", 12),
        bg=WHITE,
        fg=DARK,
        wraplength=700,
        justify="left"
    )

    explanation.pack(pady=30)

    topics = {

        "Compound Interest": (
            "Compound interest means you earn interest not only "
            "on your original money, but also on the interest "
            "that has already been added.\n\n"
            "Example: If your savings grow over time, the growth "
            "can itself start generating more growth."
        ),

        "Budgeting": (
            "A budget is a plan for how you will use your money.\n\n"
            "A simple approach is to track your income, necessary "
            "expenses, savings and optional spending."
        ),

        "Loans": (
            "A loan is money borrowed that usually has to be "
            "repaid with interest.\n\n"
            "Before taking a loan, compare the interest rate, "
            "fees, repayment period and total amount you will repay."
        ),

        "Overdraft": (
            "Spending more money than you have in your account."
        ),

        "Digital Payments": (
            "Digital payments allow you to transfer money "
            "electronically.\n\n"
            "Always verify the recipient before paying and "
            "never share your OTP, PIN or password."
        )
    }

    for topic in topics:

        tk.Button(
            content_frame,
            text=topic,
            command=lambda t=topic:
            explanation.config(text=topics[t]),
            bg="#e8eefc",
            fg=DARK,
            font=("Arial", 11),
            width=25,
            pady=7,
            relief="flat"
        ).pack(pady=4)


# ============================================================
# TOP NAVIGATION
# ============================================================

nav_frame = tk.Frame(
    root,
    bg=DARK
)

nav_frame.pack(
    fill="x",
    padx=25
)


def nav_button(text, command):

    return tk.Button(
        nav_frame,
        text=text,
        command=command,
        bg=DARK,
        fg=WHITE,
        activebackground=BLUE,
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=10
    )


nav_button("🏠 Home", show_home).pack(
    side="left"
)

nav_button("🚨 Scam Detector", show_scam_detector).pack(
    side="left"
)

nav_button("📊 Spending", show_spending_analyzer).pack(
    side="left"
)

nav_button("💡 Learn", show_financial_literacy).pack(
    side="left"
)

# Login button on the right
login_button = tk.Button(
    nav_frame,
    text="🔐 Login",
    command=show_login_popup,
    bg=BLUE,
    fg=WHITE,
    activebackground=BLUE,
    activeforeground=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=15,
    pady=10
)

login_button.pack(side="right")


# ============================================================
# MAIN CONTENT
# ============================================================

content_frame = tk.Frame(
    root,
    bg=WHITE,
    width=850,
    height=400
)

content_frame.pack(
    padx=25,
    pady=20,
    fill="both",
    expand=True
)

content_frame.pack_propagate(False)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="ABCD • Financial awareness & safety prototype",
    font=("Arial", 9),
    bg=BG,
    fg=GRAY
)

footer.pack(pady=8)


# ============================================================
# START APPLICATION
# ============================================================

create_csv_if_needed()
show_home()
root.mainloop()