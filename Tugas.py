import tkinter as tk
from tkinter import messagebox, ttk

# --- DATA (Tetap sama sesuai studi kasus THT Anda) ---
DATABASE_PENYAKIT = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nasofaring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postural": ["G24"],
}

GEJALA_LIST = [
    ("G1", "Nafas abnormal"), ("G2", "Suara serak"), ("G3", "Perubahan kulit"),
    ("G4", "Telinga penuh"), ("G5", "Nyeri bicara menelan"), ("G6", "Nyeri tenggorokan"),
    ("G7", "Nyeri leher"), ("G8", "Pendarahan hidung"), ("G9", "Telinga berdenging"),
    ("G10", "Air liur menetes"), ("G11", "Perubahan suara"), ("G12", "Sakit kepala"),
    ("G13", "Nyeri pinggir hidung"), ("G14", "Serangan vertigo"), ("G15", "Getah bening"),
    ("G16", "Leher bengkak"), ("G17", "Hidung tersumbat"), ("G18", "Infeksi sinus"),
    ("G19", "Berat badan turun"), ("G20", "Nyeri telinga"), ("G21", "Selaput lendir merah"),
    ("G22", "Benjolan leher"), ("G23", "Tubuh tak seimbang"), ("G24", "Bola mata bergerak"),
    ("G25", "Nyeri wajah"), ("G26", "Dahi sakit"), ("G27", "Batuk"),
    ("G28", "Tumbuh di mulut"), ("G29", "Benjolan di leher"), ("G30", "Nyeri antara mata"),
    ("G31", "Radang gendang telinga"), ("G32", "Tenggorokan gatal"), ("G33", "Hidung meler"),
    ("G34", "Tuli"), ("G35", "Mual muntah"), ("G36", "Letih lesu"), ("G37", "Demam")
]

class ExpertSystemTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("THT Health Assist v3.0")
        self.root.geometry("700x500")
        self.root.configure(bg="#EBEDF0")

        self.gejala_terpilih = []
        self.current_idx = 0
        
        # Colors & Fonts
        self.primary = "#2563EB"
        self.bg_white = "#FFFFFF"
        self.text_dark = "#1E293B"
        
        self.setup_styles()
        self.main_container = tk.Frame(self.root, bg="#EBEDF0")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        self.show_welcome_screen()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TProgressbar", thickness=8, troughcolor='#E2E8F0', background=self.primary, borderwidth=0)

    def clear_frame(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_frame()
        
        # Welcome Card
        card = tk.Frame(self.main_container, bg=self.bg_white, padx=40, pady=40, 
                        highlightthickness=1, highlightbackground="#CBD5E1")
        card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
        
        tk.Label(card, text="🩺", font=("Arial", 50), bg=self.bg_white).pack(pady=(10, 0))
        tk.Label(card, text="THT Health Assist", font=("Helvetica", 20, "bold"), 
                 bg=self.bg_white, fg=self.text_dark).pack(pady=10)
        tk.Label(card, text="Sistem pakar diagnosa awal gejala THT.\nProses ini memakan waktu sekitar 2 menit.", 
                 font=("Helvetica", 10), bg=self.bg_white, fg="#64748B", justify="center").pack()
        
        btn = tk.Button(card, text="Mulai Konsultasi →", font=("Helvetica", 11, "bold"), 
                        bg=self.primary, fg="white", relief=tk.FLAT, padx=20, pady=10,
                        cursor="hand2", command=self.start_diagnosis)
        btn.pack(pady=30)
        # Hover effects
        btn.bind("<Enter>", lambda e: btn.config(bg="#1D4ED8"))
        btn.bind("<Leave>", lambda e: btn.config(bg=self.primary))

    def start_diagnosis(self):
        self.gejala_terpilih = []
        self.current_idx = 0
        self.show_question_screen()

    def show_question_screen(self):
        self.clear_frame()
        
        # Question Header
        header_frame = tk.Frame(self.main_container, bg="#EBEDF0")
        header_frame.pack(fill=tk.X)
        
        self.prog_label = tk.Label(header_frame, text=f"Pertanyaan {self.current_idx + 1} dari {len(GEJALA_LIST)}", 
                                   font=("Helvetica", 9, "bold"), fg=self.primary, bg="#EBEDF0")
        self.prog_label.pack(side=tk.LEFT)
        
        self.progress = ttk.Progressbar(self.main_container, orient=tk.HORIZONTAL, mode='determinate')
        self.progress.pack(fill=tk.X, pady=(5, 25))
        self.progress['value'] = (self.current_idx / len(GEJALA_LIST)) * 100

        # Question Card
        self.q_card = tk.Frame(self.main_container, bg=self.bg_white, padx=30, pady=50,
                               highlightthickness=1, highlightbackground="#CBD5E1")
        self.q_card.pack(fill=tk.BOTH, expand=True)
        
        self.q_text = tk.Label(self.q_card, text="", font=("Helvetica", 14), 
                               bg=self.bg_white, fg=self.text_dark, wraplength=500)
        self.q_text.pack(expand=True)

        # Action Buttons
        btn_frame = tk.Frame(self.q_card, bg=self.bg_white)
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.create_action_btn(btn_frame, "YA, SAYA MERASAKAN", "#10B981", "y", tk.LEFT)
        self.create_action_btn(btn_frame, "TIDAK ADA", "#EF4444", "t", tk.RIGHT)

        self.update_question()

    def create_action_btn(self, parent, txt, color, val, side):
        btn = tk.Button(parent, text=txt, font=("Helvetica", 10, "bold"), bg=color, 
                        fg="white", relief=tk.FLAT, width=22, pady=12, cursor="hand2",
                        command=lambda: self.handle_answer(val))
        btn.pack(side=side, padx=10)

    def update_question(self):
        if self.current_idx < len(GEJALA_LIST):
            kode, teks = GEJALA_LIST[self.current_idx]
            self.q_text.config(text=f"Apakah anda mengalami gejala\n\"{teks}\"?")
            self.progress['value'] = (self.current_idx / len(GEJALA_LIST)) * 100
            self.prog_label.config(text=f"Pertanyaan {self.current_idx + 1} dari {len(GEJALA_LIST)}")
        else:
            self.show_results()

    def handle_answer(self, ans):
        if ans == 'y':
            self.gejala_terpilih.append(GEJALA_LIST[self.current_idx][0])
        
        self.current_idx += 1
        self.update_question()

    def show_results(self):
        self.clear_frame()
        
        results = self.calculate_diagnosis()
        
        card = tk.Frame(self.main_container, bg=self.bg_white, padx=30, pady=30,
                        highlightthickness=1, highlightbackground="#CBD5E1")
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="Analisa Selesai", font=("Helvetica", 16, "bold"), 
                 bg=self.bg_white, fg=self.text_dark).pack(pady=(0, 20))
        
        if results:
            # Result List
            scroll_frame = tk.Frame(card, bg=self.bg_white)
            scroll_frame.pack(fill=tk.BOTH, expand=True)
            
            for name, score in results[:3]: # Top 3
                row = tk.Frame(scroll_frame, bg="#F8FAFC", pady=10, padx=15)
                row.pack(fill=tk.X, pady=5)
                tk.Label(row, text=name, font=("Helvetica", 11, "bold"), bg="#F8FAFC").pack(side=tk.LEFT)
                tk.Label(row, text=f"{score:.1f}% Match", font=("Helvetica", 10), 
                         bg="#F8FAFC", fg=self.primary).pack(side=tk.RIGHT)
        else:
            tk.Label(card, text="Tidak ditemukan kecocokan pola penyakit.", 
                     bg=self.bg_white, font=("Helvetica", 11)).pack(pady=40)

        tk.Button(card, text="Ulangi Diagnosa", command=self.show_welcome_screen,
                  bg="#94A3B8", fg="white", relief=tk.FLAT, padx=15, pady=8).pack(side=tk.BOTTOM)

    def calculate_diagnosis(self):
        res = []
        for p, g_list in DATABASE_PENYAKIT.items():
            matches = len(set(self.gejala_terpilih) & set(g_list))
            if matches > 0:
                score = (matches / len(g_list)) * 100
                res.append((p, score))
        return sorted(res, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemTHT(root)
    root.mainloop()