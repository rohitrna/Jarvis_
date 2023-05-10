import psutil    
"run_Jarvis.bat" in (p.name() for p in psutil.process_iter())