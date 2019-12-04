import map
import reduce

if __name__ == "__main__":
    maps_number = 11
    reduces_number = 4
    text = "salutn a c'Est évan jahaz@salutn @dç sfd!a!quoh dsf !salutn!!:: aa!a salutn"
    divided_text = map.divide(text,maps_number)
    for i in range(0,maps_number):
        # map each part of the divided text in a seperate file
        mapped_list = map.map(divided_text[i],reduces_number)
        map.write_map_json(mapped_list,"data/map_test_"+str(i)+".json")




    # print(list_dics)
    # map.map("salutn a c'Est évan jahaz@salutn @dç sfd!a!quoh dsf !salutn!!:: aa!a")

def modulo(input_str, dividing_number):
    sum_ascii = 0
    for char in input_str:
        sum_ascii+=ord(char)
    return sum_ascii%dividing_number


my_str = "hello worlda"
print(modulo(my_str,2))
# print(ord(""))
# my_str_as_bytes = str.encode(my_str)
# print(my_str_as_bytes) # ensure it is byte representation
# my_decoded_str = my_str_as_bytes.decode()
# print(type(my_decoded_str)) # ensure it is string representation