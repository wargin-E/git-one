import time
sec=0
minute=0

while True:
    if sec==60:
        minute=minute+1
        sec=0
    print(minute,"min",sec,"sec passed")
    time.sleep(1)
    sec=sec+1
