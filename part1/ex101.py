import uuid
import time
from datetime import datetime

def main():
    random_hash = str(uuid.uuid4())
    while True:
        timestamp = datetime.now()
        timestamp = timestamp.strftime('%Y.%m.%d %H:%m:%S')    
        print(timestamp + ' ' + random_hash)
        time.sleep(5)

if __name__ == '__main__':
    main()