import uuid
import time
from datetime import datetime

def main():
    random_hash = str(uuid.uuid4())
    
    while True:
        timestamp = datetime.now()
        timestamp = timestamp.strftime('%Y.%m.%d %H:%m:%S') 
        hashfile = open("./files/hashfile.txt", "a+")   
        hashfile.writelines(timestamp + ' ' + random_hash + '<br>\n')
        hashfile.close()
        print(timestamp + "Running...")
        time.sleep(5)

if __name__ == '__main__':
    main()