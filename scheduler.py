import re
import json
from map import Map
from reduce import Reduce


class Scheduler():

    """The Scheduler class allows the user to create a multi-processes Map-Reduce program"""

    def __init__(self, text, nb_maps, nb_reduces):
        """
        Constructor of a Scheduler object
        :param text: the original text (String)
        :param nb_maps: number of Maps used (processes)
        :param nb_reduces: number of Reduces used (processes)
        """
        self.text = text
        self.nb_maps = nb_maps
        self.nb_reduces = nb_reduces
        self.words_lists = []
        self.map_paths_list = []
        self.reduce_paths_list = []


    def divide(self):
        """
        Divides a string in multiple lists of words of approximately equal sizes
        :return: a list of N list of words (N = number of Maps, each Map using one list of words)
        """
        main_words_list = [word.casefold() for word in re.findall(r'\w+', self.text)]
        return [main_words_list[i::self.nb_maps] for i in range(self.nb_maps)]

    def set_map_paths_list(self):
        """
        Sets the map paths list, which will be later used by the Reduces
        """
        self.map_paths_list = ["data/maps/map_json_" + str(i) + ".json" for i in range(self.nb_maps)]

    def set_reduce_paths_list(self):
        """
        Sets the reduce paths list, which will be later used to concatenate the content of each reduce
        """
        self.reduce_paths_list = ["data/reduces/reduce_json_" + str(i) + ".json" for i in range(self.nb_reduces)]

    def run_maps(self):
        """
        Creates multiple Maps and executes the run() method of each Map in parallel with the Process methods
        Also adds each Map file path in a list of Map file paths
        """
        maps = [Map(self.words_lists[i], self.nb_reduces, i) for i in range(self.nb_maps)]
        for map in maps:
            # executes the run() method of each Map
            map.start()
        for map in maps:
            # waits until the run() method of each Map has been fully executed
            map.join()


    def run_reduces(self):
        """
        Creates multiple Reduces and executes the run() method of each Reduce in parallel with the Process methods
        Also adds each Reduce file path in a list of Reduce file paths
        """
        reduces = [Reduce(self.map_paths_list, i) for i in range(self.nb_reduces)]
        for reduce in reduces:
            # executes the run() method of each Reduce
            reduce.start()
        for reduce in reduces:
            # waits until the run() method of each Reduce has been fully executed
            reduce.join()

    def join_reduces(self):
        """
        Concatenates the content of every Reduce file into one main JSON file
        """
        final_reduce = {}
        for reduce_path in self.reduce_paths_list:
            with open(reduce_path, 'r') as f:
                final_reduce.update(json.load(f))
        # the parameter 'reverse' of the 'sorted' method is set at True to display the most used words first
        final_reduce = {k: v for k, v in sorted(final_reduce.items(), key=lambda item: item[1], reverse=True)}

        with open('data/final_reduce.json', 'w') as f:
            f.write(str(final_reduce).replace("'",'"'))
        f.close()