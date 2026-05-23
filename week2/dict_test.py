d = {}
d["Apple"] = 5
d["banana"] = 3
d["Apple"] = 10
print(d)
print(d.values())
print(d.keys())

# ori_dict = ()
# ori_key = [][0]
# ori_value = [][1]

hash_table = [0] * 9
print(hash_table)


while True :
    number_key = input("入力して")
    if number_key == "end":
        print("終了")
        break

    number_value = input("value入力して")
    element = (number_key, number_value)

    ##ハッシュ関数を計算
    hash_number = 1
    for char in number_key:
        hash_number = hash_number * ord(char)
    print(hash_number)

    hash = hash_number % 10

    #ハッシュテーブルに既に値が入っていた場合の処理
    if hash_table[hash] == 0:
       hash_table[hash] = element
    elif not isinstance(hash_table[hash],list): #テーブルの要素がリストじゃない時　＝
        hash_table_list = []
        now_word = hash_table[hash]
        hash_table_list.append(now_word)
        hash_table_list.append(element)
        hash_table[hash] = hash_table_list
        print(hash_table)
    else:
        hash_table_list.append(element)


    print(f"hash table = {hash_table}")


