from threading import Thread

class Map(Thread):

    """Thread which creates a map file from a list of words
    example : {"0": {"epilogue": 1}, "1": {"not": 1, "see": 1, "no": 1, "to": 1, "the": 1, "be": 1, "wine": 1}}"""

    def __init__(self, words_list, nb_reduces, map_index):
        """
        Constructor of a Map object
        :param words_list: a part of the original text in the form of a list of Strings
        :param nb_reduces: number of Reduce threads
        :param map_index: index of the current Map
        """
        Thread.__init__(self)
        self.words_list = words_list
        self.nb_reduces = nb_reduces
        self.map_index = map_index
        self.map_path = ""

    def modulo(self,input_str, dividing_number):
        """
        Gets a pseudo-random number between 0 and a "dividing number", based on the ASCII code of each char of the input String
        :param input_str: the input String
        :param dividing_number: the diving number, which is actually the number of Reduce threads
        :return: An Integer between 0 and the dividing number-1
        """
        sum_ascii = 0
        for char in input_str:
            sum_ascii+=ord(char)
        return sum_ascii%dividing_number

    def map(self):
        """
        Maps the words from a list of words and place them in a dictionary, depending on their "modulo"
        example : ['salutn', 'est', 'salutn', 'a', 'salutn', 'salutn'] -> {'0': {'est': 1}, '1': {'salutn': 4, 'a': 1}}
        :return: the created dictionary
        """
        dict={}
        for i in range(0,self.nb_reduces):
            dict[str(i)]={}
        for word in self.words_list:
            reduce_index = str(self.modulo(word,self.nb_reduces))
            if word in dict[reduce_index]:
                dict[reduce_index][word]+=1
            else:
                dict[reduce_index][word]=1
        return(dict)


    def write_map_json(self,mapped_list):
        """
        Writes the content of a Python dictionary in a JSON file
        :param mapped_list: a dictionary containing the mapped list of words
        """
        with open(self.map_path, 'w') as f:
            f.write(str(mapped_list).replace("'",'"'))
        f.close()


    def run(self):
        """
        Creates a mapped dictionary from a list of words, then put it in a JSON file
        """
        map_dict = self.map()
        self.map_path = "data/maps/map_json_" + str(self.map_index) + ".json"
        self.write_map_json(map_dict)