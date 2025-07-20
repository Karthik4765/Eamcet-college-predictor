import tkinter as tk
from tkinter import messagebox, scrolledtext


def load_college_data(filename):
    colleges = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 5:
                    college_name, branch, category, gender, cutoff_rank = data
                    try:
                        colleges.append((college_name, branch, category, gender, int(cutoff_rank)))
                    except ValueError:
                        continue  # Skip header or invalid lines
    except FileNotFoundError:
        messagebox.showerror("Error", f"Data file '{filename}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return colleges


def predict_colleges(rank, gender, branch, category, colleges):
    eligible_colleges = []
    for college in colleges:
        name, c_branch, c_category, c_gender, cutoff = college
        if (
            rank <= cutoff and
            c_gender.lower() == gender.lower() and
            c_category.lower() == category.lower() and
            (branch == "" or c_branch.lower() == branch.lower())
        ):
            eligible_colleges.append(college)
    return eligible_colleges


def display_results(results, text_widget):
    text_widget.delete(1.0, tk.END)
    if not results:
        text_widget.insert(tk.END, "No colleges found for your criteria.\n")
        return
    text_widget.insert(tk.END, "Eligible Colleges for your Criteria:\n\n")
    for college in results:
        name, branch, category, gender, cutoff = college
        text_widget.insert(tk.END, f"{name} | {branch} | {category} | {gender} | Cutoff Rank: {cutoff}\n")


def on_predict():
    try:
        rank = int(rank_entry.get())
        gender = gender_var.get()
        category = category_var.get()
        branch = branch_entry.get().strip()
        if not gender or not category:
            messagebox.showwarning("Missing Input", "Please select both gender and caste/category.")
            return
        results = predict_colleges(rank, gender, branch, category, colleges)
        display_results(results, result_text)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid numeric rank.")


# --- GUI Setup ---
filename = 'colleges_full.txt'
colleges = load_college_data(filename)

root = tk.Tk()
root.title("EAMCET College Predictor")

tk.Label(root, text="Enter your EAMCET rank:").pack(pady=5)
rank_entry = tk.Entry(root)
rank_entry.pack(pady=5)

tk.Label(root, text="Select Gender:").pack(pady=5)
gender_var = tk.StringVar(value="")
gender_frame = tk.Frame(root)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="M").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="F").pack(side=tk.LEFT)
gender_frame.pack(pady=5)

tk.Label(root, text="Select Caste/Category:").pack(pady=5)
category_var = tk.StringVar(value="")
category_options = ["OC", "BC-A", "BC-B", "BC-C", "BC-D", "BC-E", "SC", "ST", "EWS"]
category_menu = tk.OptionMenu(root, category_var, *category_options)
category_menu.pack(pady=5)

tk.Label(root, text="Enter Branch (e.g., CSE, ECE) or leave blank for any:").pack(pady=5)
branch_entry = tk.Entry(root)
branch_entry.pack(pady=5)

predict_btn = tk.Button(root, text="Predict Colleges", command=on_predict)
predict_btn.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.pack(padx=10, pady=10)

root.mainloop()
