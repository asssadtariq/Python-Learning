import multiprocessing
import time

def count_word(text, word, return_queue):
    text = text.replace(",", "")
    time.sleep(10)
    print("Word = ", text.split(" ").count(word))
    return_queue.put(text.split(" ").count(word) + 10)

def count_character(text, char, return_queue):
    time.sleep(5)
    print("Character Count = ", text.count(char))
    return_queue.put(text.count(char) + 10)

def main():
    text = '''
    In the bustling city, neon lights flickered above the crowded streets, casting an energetic glow that mirrored the vibrant pulse of the city. People hurriedly hurried along the sidewalks, their faces absorbed in the hurried rhythm of their daily lives. Amidst the hurried pace, a sense of urgency lingered in the air, as if time itself were in a hurry, pushing everyone to move at a hurried speed
    '''
    word_to_count = "streets"
    chr_to_count = "c"

    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=count_word, args=(text, word_to_count, q1))
    p2 = multiprocessing.Process(target=count_character, args=(text, chr_to_count, q2))

    p1.start()
    p2.start()
    
    ''' If p1 completes then q1 exectes and then q2 '''
#    print(q1.get())

#    print(q2.get())

    ''' q2.get() will be executed as p2 completes - then q1 waits for p1 to completes '''
    print(q2.get())

    print(q1.get())

    p1.join()
    p2.join()

    print("FINISH")

if __name__ == "__main__":
    main()
    