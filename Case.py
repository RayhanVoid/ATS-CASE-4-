import tkinter as tk
from tkinter import ttk, messagebox

def kirim_formulir():
    nama = entry_nama.get().strip()
    kota_lahir = entry_kota_lahir.get().strip()
    status = status_var.get()
    agama = agama_var.get()
    alamat = entry_alamat.get("1.0", "end-1c").strip()

    if not nama or not kota_lahir or not status or not agama or not alamat:
        messagebox.showerror("Error", "Harap lengkapi semua kolom.")
        return

    pesan = (
        f"Formulir Identitas Diri\n\n"
        f"Nama: {nama}\n"
        f"Kota Lahir: {kota_lahir}\n"
        f"Status Pernikahan: {status}\n"
        f"Agama: {agama}\n"
        f"Alamat: {alamat}"
    )

    messagebox.showinfo("Data Identitas", pesan)

    # reset form
    entry_nama.delete(0, tk.END)
    entry_kota_lahir.delete(0, tk.END)
    status_var.set("")
    agama_var.set("Islam")
    entry_alamat.delete("1.0", tk.END)


root = tk.Tk()
root.title("Formulir Identitas Diri")
root.geometry("420x420")
root.resizable(False, False)

# CENTER WINDOW
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 210
y = (root.winfo_screenheight() // 2) - 210
root.geometry(f"420x420+{x}+{y}")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"))

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

# Nama
ttk.Label(frame, text="Nama").grid(row=0, column=0, sticky="w", pady=5)
entry_nama = ttk.Entry(frame, width=30)
entry_nama.grid(row=0, column=1, pady=5)

# Kota Lahir
ttk.Label(frame, text="Kota Lahir").grid(row=1, column=0, sticky="w", pady=5)
entry_kota_lahir = ttk.Entry(frame, width=30)
entry_kota_lahir.grid(row=1, column=1, pady=5)

# Status
ttk.Label(frame, text="Status").grid(row=2, column=0, sticky="w", pady=5)
status_var = tk.StringVar()

status_frame = ttk.Frame(frame)
status_frame.grid(row=2, column=1, sticky="w")

ttk.Radiobutton(status_frame, text="Belum Menikah", variable=status_var, value="Belum Menikah").pack(side="left")
ttk.Radiobutton(status_frame, text="Menikah", variable=status_var, value="Menikah").pack(side="left")

# Agama
ttk.Label(frame, text="Agama").grid(row=3, column=0, sticky="w", pady=5)
agama_var = tk.StringVar(value="Islam")
agama_menu = ttk.Combobox(frame, textvariable=agama_var, values=[
    "Islam", "Kristen", "Hindu", "Buddha", "Konghucu"
], state="readonly")
agama_menu.grid(row=3, column=1, pady=5)

# Alamat
ttk.Label(frame, text="Alamat").grid(row=4, column=0, sticky="nw", pady=5)
entry_alamat = tk.Text(frame, width=25, height=4)
entry_alamat.grid(row=4, column=1, pady=5)

# Button
ttk.Button(frame, text="Kirim", command=kirim_formulir).grid(row=5, column=1, sticky="e", pady=15)

root.mainloop()
