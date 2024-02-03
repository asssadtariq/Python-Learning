from threading import Lock

mylock = Lock()

def function(number):
    mylock.acquire()

def main():
    mylock.acquire()
    print(mylock)
    mylock.release()
    print(mylock)


if __name__ == "__main__":
    main()
