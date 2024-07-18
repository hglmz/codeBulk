import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class FileMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dosya Birleştirici")
        
        self.label = tk.Label(root, text="Birleştirilecek dosyaların bulunduğu klasörü seçin:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Klasör Seç", command=self.select_folder)
        self.select_button.pack(pady=5)
        
        self.merge_button = tk.Button(root, text="Birleştir ve Kaydet", command=self.merge_files)
        self.merge_button.pack(pady=5)
        
        self.folder_path = ""

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Seçilen Klasör", f"Seçilen klasör: {self.folder_path}")

    def merge_files(self):
        if not self.folder_path:
            messagebox.showwarning("Uyarı", "Önce bir klasör seçmelisiniz.")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not save_path:
            return
        
        try:
            with open(save_path, 'w') as output_file:
                for root_dir, _, files in os.walk(self.folder_path):
                    for file in files:
                        if file.endswith('.cpp') or file.endswith('.h'):
                            file_path = os.path.join(root_dir, file)
                            file_name = os.path.relpath(file_path, self.folder_path)  # Dosya adını klasör yapısı ile birlikte al
                            output_file.write(f"{'='*20} {file_name} {'='*20}\n\n")
                            with open(file_path, 'r') as input_file:
                                output_file.write(input_file.read())
                                output_file.write("\n\n")
            messagebox.showinfo("Başarılı", f"Dosyalar başarıyla {save_path} dosyasına birleştirildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosyalar birleştirilirken bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMergerApp(root)
    root.mainloop()
