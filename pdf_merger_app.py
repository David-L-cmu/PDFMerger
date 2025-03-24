import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfMerger
from datetime import datetime

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("800x500")
        self.root.minsize(600, 400)
        
        self.selected_files = []
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create and place widgets
        self.create_widgets(main_frame)
    
    def create_widgets(self, parent):
        # Button frame for file operations
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, pady=10)
        
        # Add files button
        add_btn = ttk.Button(btn_frame, text="Add PDFs", command=self.add_files)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Remove selected button
        remove_btn = ttk.Button(btn_frame, text="Remove Selected", command=self.remove_selected)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear all button
        clear_btn = ttk.Button(btn_frame, text="Clear All", command=self.clear_files)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Files list frame
        list_frame = ttk.LabelFrame(parent, text="Selected PDFs (in merge order)")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Scrollbar for the listbox
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox to display selected files
        self.files_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED, yscrollcommand=scrollbar.set)
        self.files_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.files_listbox.yview)
        
        # Order control buttons
        order_frame = ttk.Frame(parent)
        order_frame.pack(fill=tk.X, pady=5)
        
        move_up_btn = ttk.Button(order_frame, text="Move Up", command=self.move_up)
        move_up_btn.pack(side=tk.LEFT, padx=5)
        
        move_down_btn = ttk.Button(order_frame, text="Move Down", command=self.move_down)
        move_down_btn.pack(side=tk.LEFT, padx=5)
        
        # Output options frame
        output_frame = ttk.LabelFrame(parent, text="Output Options")
        output_frame.pack(fill=tk.X, pady=10)
        
        # Output filename
        filename_frame = ttk.Frame(output_frame)
        filename_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(filename_frame, text="Output Filename:").pack(side=tk.LEFT, padx=5)
        self.output_filename = tk.StringVar()
        filename_entry = ttk.Entry(filename_frame, textvariable=self.output_filename)
        filename_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Label(filename_frame, text=".pdf").pack(side=tk.LEFT)
        
        # Merge button
        merge_btn = ttk.Button(parent, text="Merge PDFs", command=self.merge_pdfs)
        merge_btn.pack(pady=10)
    
    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if not files:
            return
            
        for file in files:
            if file not in self.selected_files:
                self.selected_files.append(file)
                self.files_listbox.insert(tk.END, os.path.basename(file))
    
    def remove_selected(self):
        selected_indices = self.files_listbox.curselection()
        if not selected_indices:
            return
            
        # Remove from highest index to lowest to avoid index shifting
        for i in sorted(selected_indices, reverse=True):
            self.files_listbox.delete(i)
            self.selected_files.pop(i)
    
    def clear_files(self):
        self.files_listbox.delete(0, tk.END)
        self.selected_files = []
    
    def move_up(self):
        selected_indices = self.files_listbox.curselection()
        if not selected_indices or 0 in selected_indices:
            return
            
        for i in selected_indices:
            # Swap the items in the list
            self.selected_files[i], self.selected_files[i-1] = self.selected_files[i-1], self.selected_files[i]
            
            # Update the listbox
            file_name = self.files_listbox.get(i)
            self.files_listbox.delete(i)
            self.files_listbox.insert(i-1, file_name)
            self.files_listbox.selection_set(i-1)
    
    def move_down(self):
        selected_indices = list(self.files_listbox.curselection())
        if not selected_indices or len(self.selected_files) - 1 in selected_indices:
            return
            
        # Process in reverse order for moving down
        for i in sorted(selected_indices, reverse=True):
            if i < len(self.selected_files) - 1:
                # Swap the items in the list
                self.selected_files[i], self.selected_files[i+1] = self.selected_files[i+1], self.selected_files[i]
                
                # Update the listbox
                file_name = self.files_listbox.get(i)
                self.files_listbox.delete(i)
                self.files_listbox.insert(i+1, file_name)
                self.files_listbox.selection_set(i+1)
    
    def merge_pdfs(self):
        if not self.selected_files:
            messagebox.showerror("Error", "No PDF files selected")
            return
        
        # Get output filename
        output_name = self.output_filename.get().strip()
        if not output_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"merged_{timestamp}"
        
        # Add .pdf extension if not present
        if not output_name.lower().endswith('.pdf'):
            output_name += '.pdf'
        
        # Ask for output location
        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            initialfile=output_name,
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if not output_path:
            return  # User cancelled
        
        try:
            # Create a PdfMerger object
            merger = PdfMerger()
            
            # Add each PDF to the merger
            for pdf_file in self.selected_files:
                try:
                    merger.append(pdf_file)
                except Exception as e:
                    messagebox.showerror("Error", f"Error adding '{os.path.basename(pdf_file)}': {str(e)}")
                    merger.close()
                    return
            
            # Write to the output file
            merger.write(output_path)
            merger.close()
            
            messagebox.showinfo("Success", f"Successfully merged {len(self.selected_files)} PDF files into '{output_path}'")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error merging PDFs: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop() 