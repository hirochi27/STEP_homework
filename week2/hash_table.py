import random, sys, time

###########################################################################
#                                                                         #
# Implement a hash table from scratch!                                    #
#                                                                         #
# Please do not use Python's dictionary or Python's collections library.  #
# The goal is to implement the data structure yourself.                   #
#                                                                         #
###########################################################################

# Hash function.
#
# 'key': string
# Return value: a hash value
def calculate_hash(key):
    assert type(key) == str
    # Note: This is not a good hash function. Make it better!
    # hash = 0
    # for i in key:
    #     hash += ord(i)
    # return hash
    hash_number = 1
    for char in key:
        hash_number = hash_number * ord(char)
        #print(hash_number)
    return hash_number


# An item object that represents one key - value pair in the hash table.
class Item:
    # 'key': The key of the item. The key must be a string.
    # 'value': The value of the item.
    # 'next': The next item in the linked list. If this is the last item in the
    #         linked list, 'next' is None.
    def __init__(self, key, value, next):
        assert type(key) == str
        self.key = key
        self.value = value
        self.next = next
        self.backets = []


# The main data structure of the hash table that stores key - value pairs.
# The key must be a string. The value can be any type.
#
# 'self.bucket_size': The bucket size.
# 'self.buckets': An array of the buckets. self.buckets[hash % self.bucket_size]
#                 stores a linked list of items whose hash value is 'hash'.
# 'self.item_count': The total number of items in the hash table.
class HashTable:

    # Initialize the hash table.
    def __init__(self):
        # Set the initial bucket size to 97. A prime number is chosen to reduce
        # hash conflicts.
        self.bucket_size = 97
        self.buckets = [None] * self.bucket_size
        self.item_count = 0
        #self.hash_table_list = []
        
    # Put an item to the hash table. If the key already exists, the
    # corresponding value is updated to a new value.
    #
    # 'key': The key of the item.
    # 'value': The value of the item.
    # Return value: True if a new item is added. False if the key already exists
    #               and the value is updated.
    def put(self, key, value):
        assert type(key) == str
        check_size(self.size(), self.bucket_size)  # Don't remove this code.
        #------------------------#
        # Write your code here!  #

        element = (key, value)

        hash_number = calculate_hash(key)
        hash = hash_number % self.bucket_size

        if self.buckets[hash] == None: #初めて値を入れるとき＝elementを入れる
            # print("None")
            self.buckets[hash] = element
            # print(self.buckets)
        elif self.buckets[hash][0] == key: #同じkeyが既に入っていた時＝valueを書き換える
            self.buckets[hash] = list(self.buckets[hash])
            self.buckets[hash][1] = value
            return False
        elif not isinstance(self.buckets[hash],list): 
            #同じハッシュ値に複数の値を入れたいので、リストを作る
            #ここを連結リストにする
            # print("elif")
            self.hash_table_list = []
            now_word = self.buckets[hash]
            self.hash_table_list.append(now_word)
            self.hash_table_list.append(element)
            self.buckets[hash] = self.hash_table_list
        else:#同じハッシュ値のリストの最後、に値を追加
            # print("else")
            self.buckets[hash].append(element) 

        self.item_count = self.item_count + 1
        #print(f"self.buckets = {self.buckets}")
        print(f"put True {key}")
        print(self.buckets)
        #------------------------#
        return True

    # Get an item from the hash table.
    #
    # 'key': The key.
    # Return value: If the item is found, return (the value of the item, True).
    #               Otherwise, return (None, False).
    def get(self, key):
        assert type(key) == str
        check_size(self.size(), self.bucket_size)  # Don't remove this code.
        #------------------------#
        # Write your code here!  #

        hash_number = calculate_hash(key)
        hash = hash_number % self.bucket_size

        if self.buckets[hash] != None:
            if self.buckets[hash][0] == key: #ハッシュ値が同じ＆keyも同じ時の処理

                #print(f"値がある＝Trueのとき　{self.buckets[hash][1]}")
                print(self.buckets)
                print(f"1 get True {self.buckets[hash][1]}")
                return (self.buckets[hash][1], True)
            
            elif self.buckets[hash] == self.hash_table_list:
                for element in self.buckets[hash] :
                    if element[0] == key:

                        print(self.buckets)
                        print(f"2 get True {element[1]}")
                        return (element[1], True)
                    
            else:#ハッシュ値が同じ＆違うkeyが入ってた時
                print(self.buckets)
                print(" get None 1")
                return (None, False)
        else:
            print("get None 2")

        #------------------------#
            return (None, False)

    # Delete an item from the hash table.
    #
    # 'key': The key.
    # Return value: True if the item is found and deleted successfully. False
    #               otherwise.
    def delete(self, key):
        assert type(key) == str
        #------------------------#
        # Write your code here!  
        
        hash_number = calculate_hash(key)
        hash = hash_number % self.bucket_size

        if self.buckets[hash] != None: #対応する位置に値が入っている時
            if self.buckets[hash][0] == key:
                self.buckets[hash] = None
                self.item_count = self.item_count - 1

                print(f"Delete{self.buckets[hash]} and {key}")
                
                return True
            elif self.buckets[hash] == self.hash_table_list:#複数のkey:valueペアが入っている時
                for i, element in enumerate(self.buckets[hash]):
                    #今ただのリストになってるからハッシュテーブルに直したい
                    if element is not None and element[0] == key: 
                        self.buckets[hash].pop(i)
                        self.item_count -= self.item_count
                        return True
            else:
                return False
        else:
            return False

        #------------------------#

    # Return the total number of items in the hash table.
    def size(self):
        return self.item_count


# Check that the hash table has a "reasonable" bucket size.
# The bucket size is judged "reasonable" if it is smaller than 100 or
# the buckets are 30% or more used.
#
# Note: Don't change this function.
def check_size(item_count, bucket_size):
    assert (bucket_size < 100 or item_count >= bucket_size * 0.3)


# Test the functional behavior of the hash table.
def functional_test():
    hash_table = HashTable()

    assert hash_table.put("aaa", 1) == True
    assert hash_table.get("aaa") == (1, True)
    assert hash_table.size() == 1

    assert hash_table.put("bbb", 2) == True
    assert hash_table.put("ccc", 3) == True
    assert hash_table.put("ddd", 4) == True
    assert hash_table.get("aaa") == (1, True)
    assert hash_table.get("bbb") == (2, True)
    assert hash_table.get("ccc") == (3, True)
    assert hash_table.get("ddd") == (4, True)
    assert hash_table.get("a") == (None, False)
    assert hash_table.get("aa") == (None, False)
    assert hash_table.get("aaaa") == (None, False)
    assert hash_table.size() == 4

    assert hash_table.put("aaa", 11) == False
    assert hash_table.get("aaa") == (11, True)
    assert hash_table.size() == 4

    assert hash_table.delete("aaa") == True
    assert hash_table.get("aaa") == (None, False)
    assert hash_table.size() == 3

    assert hash_table.delete("a") == False
    assert hash_table.delete("aa") == False
    assert hash_table.delete("aaa") == False
    assert hash_table.delete("aaaa") == False

    assert hash_table.delete("ddd") == True
    assert hash_table.delete("ccc") == True
    assert hash_table.delete("bbb") == True
    assert hash_table.get("aaa") == (None, False)
    assert hash_table.get("bbb") == (None, False)
    assert hash_table.get("ccc") == (None, False)
    assert hash_table.get("ddd") == (None, False)
    assert hash_table.size() == 0

    assert hash_table.put("abc", 1) == True
    assert hash_table.put("acb", 2) == True
    assert hash_table.put("bac", 3) == True
    assert hash_table.put("bca", 4) == True
    assert hash_table.put("cab", 5) == True
    assert hash_table.put("cba", 6) == True
    assert hash_table.get("abc") == (1, True)
    assert hash_table.get("acb") == (2, True)
    assert hash_table.get("bac") == (3, True)
    assert hash_table.get("bca") == (4, True)
    assert hash_table.get("cab") == (5, True)
    assert hash_table.get("cba") == (6, True)
    assert hash_table.size() == 6

    assert hash_table.delete("abc") == True
    assert hash_table.delete("cba") == True
    assert hash_table.delete("bac") == True
    assert hash_table.delete("bca") == True
    assert hash_table.delete("acb") == True
    assert hash_table.delete("cab") == True
    assert hash_table.size() == 0

    # Test the rehashing.
    for i in range(100):
        hash_table.put(str(i), str(i))
    for i in range(100):
        assert hash_table.get(str(i)) == (str(i), True)
    for i in range(100):
        assert hash_table.delete(str(i)) == True
    hash_table.put("abc", 1)
    hash_table.put("acb", 2)
    assert hash_table.get("abc") == (1, True)
    assert hash_table.get("acb") == (2, True)
    print("Functional tests passed!")


# Test the performance of the hash table.
#
# Your goal is to make the hash table work with mostly O(1).
# If the hash table works with mostly O(1), the execution time of each iteration
# should not depend on the number of items in the hash table. To achieve the
# goal, you will need to 1) implement rehashing (Hint: expand / shrink the hash
# table when the number of items in the hash table hits some threshold) and
# 2) tweak the hash function (Hint: think about ways to reduce hash conflicts).
def performance_test():
    hash_table = HashTable()

    for iteration in range(100):
        begin = time.time()
        random.seed(iteration)
        for i in range(10000):
            rand = random.randint(0, 100000000)
            hash_table.put(str(rand), str(rand))
        random.seed(iteration)
        for i in range(10000):
            rand = random.randint(0, 100000000)
            hash_table.get(str(rand))
        end = time.time()
        print("%d %.6f" % (iteration, end - begin))

    for iteration in range(100):
        random.seed(iteration)
        for i in range(10000):
            rand = random.randint(0, 100000000)
            hash_table.delete(str(rand))

    assert hash_table.size() == 0
    print("Performance tests passed!")


if __name__ == "__main__":
    functional_test()
    performance_test()