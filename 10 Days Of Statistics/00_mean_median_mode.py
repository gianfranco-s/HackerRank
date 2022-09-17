# Enter your code here. Read input from STDIN. Print output to STDOUT

N = input()  # Code for Hackerrank
X = input()         # Code for Hackerrank

# N = int(input('Array length: '))
# X = input('Array data: ')

# Test data
# N = 6
# X = '1 2 3 4 5 5'

# N = 10
# X = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'

# N = 8
# X = '64630 11735 14216 99233 51135 67060 51135 67060'

# N = 6
# X = '5 2 3 4 5 1'

# N = 5
# X = '5 2 3 4 5'

def order_data(data):
    data = data.split(' ')
    data = [int(e) for e in data]
    length = len(data)
    ordered_data = []
    for i in range(length):
        if not data:
            break
        min_val = min(data)
        ordered_data.append(int(min_val))
        data.remove(min_val)
    return length, ordered_data


def calculate_mean(length, data):
    total_sum = 0
    for el in data:
        total_sum+=int(el)
    return round(total_sum/length,1)
    

def calculate_median(length, data):
    mid = int(length/2) - 1
    if length % 2 == 0:  # length is an even number
        nxt = mid + 1
        median = (data[mid] + data[nxt])/2
    else:  # length is an odd number
        median = data[int(mid)]
        
    return round(float(median), 1)


def calculate_mode(length, data):
    occurrences_dict = dict.fromkeys(set(data), 0)
    for key, val in occurrences_dict.items():
        for elem in data:
            occurrences_dict[key] = occurrences_dict[key] + (1 if elem == key else 0)

    marklist = sorted(occurrences_dict.items(), key=lambda item: item[1], reverse=True)
    # 'occurrences_dict.items()'  returns list of tuples --> [ (key1, value1), (key2, value2)...]
    # 'key=' takes in a function to sort the elements.
    #        E.G.1: sorted(['b', 'ccc', 'aa']) --> ['aa', 'b', 'ccc']
    #        E.G.2: sorted(['b', 'aa', 'ccc'], key=len) --> ['b', 'aa', 'ccc']
    #        In conclusion: it sorts the following list [len(element1), len(element2), ...]
    # lambda item: item[1]: returns the second element (index=1) of each element, so the list to sort would be:
    # [second_element_of(element1), second_element_of(element2), ...]
    sorted_by_keys = dict(marklist)
    
    items = list(sorted_by_keys.items())
    top_values = [items[0]]
    for i in range(1, len(items)):
        if items[i][1] == items[i-1][1]:
            top_values.append(items[i])
        else:
            break
    top_values_dict = dict(top_values)

    mode = min(top_values_dict.keys())
    return mode
    

def main():
    N, ordered_data = order_data(X)
    print(calculate_mean(N, ordered_data))
    print(calculate_median(N, ordered_data))
    print(calculate_mode(N, ordered_data))


main()