import json
import multiprocessing

class Reduce(multiprocessing.Process):

    """Process which creates a reduce file from a list of map files paths"""

    def __init__(self, map_paths_list, reduce_index):
        """
        Constructor of a Reduce object
        :param map_paths_list: the list of all Maps files paths
        :param reduce_index: index of the current Reduce
        """

        multiprocessing.Process.__init__(self)
        self.map_paths_list = map_paths_list
        self.reduce_index = reduce_index
        self.word_dicts_list = []
        self.reduce_path = ""

    def read_map_files(self):
        """
        Reads each Map file to take only the part which is useful for the current Reduce, creating a "main" dictionary
        """
        for map_path in self.map_paths_list:
            with open(map_path, 'r') as f:
                self.word_dicts_list.append(json.load(f)[str(self.reduce_index)])

    def reduce(self):
        """
        Goes through the words dictionary to count the occurrences of each different word
        :return: a dictionary with each different word as keys and their number of occurrences as values
        """
        res = {}
        for words_dict in self.word_dicts_list:
            for key, value in words_dict.items():
                if key in res.keys():
                    res[key] = res[key] + value
                else:
                    res[key] = value
        return res

    def write_reduce_json(self, small_dic):
        """
        Writes the content of a Python dictionary in a JSON file
        :param small_dic: a dictionary containing the different words and their number of occurrences
        """
        with open(self.reduce_path, 'w') as reduceJson:
            json.dump(small_dic, reduceJson)

    def run(self):
        """
        Executes the different class methods to count the occurrences of some words from a list of Map files paths
        """
        self.read_map_files()
        current_dict = self.reduce()
        self.reduce_path = "data/reduces/reduce_json_" + str(self.reduce_index) + ".json"
        self.write_reduce_json(current_dict)

        print("reduce_json_" + str(self.reduce_index) + ".json has been created.")