import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from core.file_handler import extract_text
from core.analyzer import analyze_resume
from core.formatter import clean_output
from utils.helpers import clean_resume_text, limit_text_length


class SkillLensApp:

    def __init__(self, root):
        self.root = root
        self.root.title("SkillLens - AI Resume Feedback Tool")
        self.root.geometry("800x600")

        self.file_path = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="SkillLens", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Button(self.root, text="Upload Resume", command=self.upload_file).pack(pady=5)

        tk.Button(self.root, text="Analyze", command=self.analyze).pack(pady=5)

        self.output_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=90, height=25)
        self.output_box.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("Success", "File uploaded successfully!")

    def analyze(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a resume first.")
            return

        try:
            text = extract_text(self.file_path)
            result = analyze_resume(text)
            clean = clean_output(result)

            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, clean)

        except Exception as e:
            messagebox.showerror("Error", str(e))
