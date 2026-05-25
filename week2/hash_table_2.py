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

    # #素数を計算する
    # number = []
    # for i in range(2, 11):
    #     flag = False
    #     for j in range(2, i): #i 未満
    #         if i % j == 0:
    #             flag = False
    #         else:
    #             flag = True
    #     if flag == False:
            
    #indexとハッシュ値を足してから、かけてみる
    hash_number = 1
    for ind, char in enumerate(key):
        hash_number = hash_number * (ord(char) + ind)
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
        hash_number = calculate_hash(key)
        hash = hash_number % self.bucket_size
        #print(len(self.buckets))
        new_item = Item(key,value,None)
        

        #if : テーブルにkeyがない時、新しく追加
        #elif : 既にkeyがある時、valueを上書き
        #else :　異なるkeyがあるとき、連結部分に同じkeyがないか探す。ない場合は最後尾に連結させる
        if self.buckets[hash] == None:
            self.buckets[hash] = new_item
            self.item_count += 1
            # print(self.buckets)
            return True
        elif self.buckets[hash].key == new_item.key:
            self.buckets[hash].value = new_item.value
            return False
        else: 
            current = self.buckets[hash] #current: 元のテーブルを壊さないように、currentに避難させて確認
            while current != None:
                if current.key == new_item.key:
                    current.value = new_item.value
                    return False
                prev = current
                current = current.next
            prev.next = new_item
            self.item_count += 1
            # print(self.buckets)


            #要素数/テーブルサイズが70%を上回ったら、テーブルサイズを2倍にする
            #old_buckets : 再ハッシュ前のテーブルを退避してから、self.bucketsを書き換える
                #その後2倍にしたハッシュテーブルに値を入れ直す
            if self.item_count  > self.bucket_size * 0.7:
                self.bucket_size = self.bucket_size * 2  
                if self.bucket_size % 2 == 0: #バケット数が偶数になった場合、奇数にする
                    self.bucket_size += 1        
                
                old_buckets = self.buckets   
                self.buckets = self.bucket_size * [None]
                #self.item_count = 0                   
                for item in old_buckets:
                    while item != None:
                        put_item = item
                        item = item.next
                        self.put(put_item.key, put_item.value)
                print(f"2倍　現在のサイズ{self.bucket_size}")
                print(self.item_count)


                    
            # current = 
            # if self.buckets[hash].next == None:#ハッシュテーブルに値が1つの時,新しくnextに繋げる
            #     self.buckets[hash].next = new_item
            #     last_item = self.buckets[hash].next
            # else:#ハッシュテーブルに２つ以上値が繋がってた時
            #     #繰り返し最後にitemを繋げられるようにする
            #     last_item.next = new_item
            #     last_item = last_item.next


        
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
        
        #if : 目的の位置のテーブルにitemがないとき、Noneを反す
            #if : itemを見つけたらTrueを反す
            #else : 同じハッシュ値の中に異なるkeyが入ってた時、nextをたどって探す
        if self.buckets[hash] != None: 
            #print("return None")
            if self.buckets[hash].key == key: 
                return (self.buckets[hash].value, True)
            else: 
                #current : 元のテーブル＝self.buketsを壊さないために、複製しておくための関数
                current = self.buckets[hash]
                while current != None:
                    #print(f"カレントはこれ！！{current.key}")
                    if current.key == key:   
                        return (current.value, True)
                    current = current.next
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
        # Write your code here!  #
        hash_number = calculate_hash(key)
        hash = hash_number % self.bucket_size

        #if : hashの位置に値が入ってない時はすぐFalseを返す
        if self.buckets[hash] != None: 
            current = self.buckets[hash]

            #while : 現在見てるitemがNoneになるまで,deleteしたいkeyがあるか確かめる : 無かったらFalse
            while current is not None:
                if current.key == key:#消したいkeyを見つけたらcurrentの1つ前のnextと次のitemを繋げる
                    if current == self.buckets[hash]:
                        self.buckets[hash] = self.buckets[hash].next
                        self.item_count -= 1
                        
                        #もしitem数がバケットサイズの30％未満になったら、バケットサイズを半分にする
                        if self.bucket_size > 97:
                            if self.item_count < self.bucket_size * 0.3:
                                self.bucket_size = self.bucket_size // 2
                                #self.item_count = 0
                                #再ハッシュのための値を保存するため、現在のテーブルをolr_bucketに退避
                                old_buckets = self.buckets
                                self.buckets = self.bucket_size * [None]
                                #新しいテーブルに値を入れ直す
                                for item in old_buckets:
                                    while item != None:
                                        self.put(item.key, item.value)              
                                        item = item.next
                                        
                                print(f"1/2倍　現在のサイズ{self.bucket_size}")
                                print(self.item_count)
                        return(True)
                    else:
                        prev.next = current.next
                        self.item_count -= 1

                        if self.bucket_size > 97:
                            if self.item_count < self.bucket_size * 0.3:
                                self.bucket_size = self.bucket_size // 2
                                #self.item_count = 0
                                #再ハッシュのための値を保存するため、現在のテーブルをolr_bucketに退避
                                old_buckets = self.buckets
                                self.buckets = self.bucket_size * [None]
                                #新しいテーブルに値を入れ直す
                                for item in old_buckets:
                                    while item != None:
                                        self.put(item.key, item.value)  
                                        item = item.next           
                                print(f"1/2倍　現在のサイズ{self.bucket_size}")
                                print(self.item_count)

                        return (True)
                prev = current
                current = current.next
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