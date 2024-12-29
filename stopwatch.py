import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self,root):
        self.root =root
        self.root.title(Stopwatch)
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta()
        
        self.label = tk.Label(root, text="00:00:00", font=("arial",30))
        self.label.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)
        
        
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        
        
    def update(self):
            if self.running:
                now = datetime.now()
                self.elapsed_time = now - self.start_time
                self.label.config(text=str(self.elapsed_time)[:7])
                self.root.after(1000,self.update)
                
                
    def start(self):
        if not self.running:
            self.running = True
            self.start_time=datetime.now() - self.elapsed_time
            self.update()
            
    def stop(self):
        if self.running:
            self.running = False
            
            
    def reset(self):
        self.running =False
        self.elapsed_time = timedelta()
        self.label.config(text="00:00:00")
        
        
if __name__=="__main__":
    root =tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()        
        
        
        