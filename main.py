from scheduler import Scheduler
import time
import os
import glob

def mapReduce(nb_maps, nb_reduces):
    """
    Creates a Scheduler object to count the occurrences of each different word of a text
    Also counts the execution time to divide the text in lists of words (t1), and the execution time to run all Maps and
    Reduces (t2)
    :param nb_maps: number of Maps used
    :param nb_reduces: number of Reduces used
    :return: a list composed of t1 and t2
    """
    start_t1 = time.time()

    f = open('data/text2.txt', 'r')
    text = f.read()

    myScheduler = Scheduler(text, nb_maps, nb_reduces)
    myScheduler.words_lists = myScheduler.divide()

    end_t1 = time.time()
    t1 = end_t1-start_t1
    start_t2 = time.time()

    myScheduler.run_maps()
    myScheduler.run_reduces()
    myScheduler.join_reduces()

    end_t2 = time.time()
    t2 = end_t2-start_t2

    return [t1,t2]



def delete_files():
    """
    Deletes all files of the "data/maps" and "data/reduces" directories
    """
    maps = glob.glob('data/maps/*')
    for map in maps:
        os.remove(map)
    reduces = glob.glob('data/reduces/*')
    for reduce in reduces:
        os.remove(reduce)

if __name__ == "__main__":
    delete_files()
    mapReduce(4,2)


