# week2　ハッシュテーブルの実装
* dict_test.py - 最初にハッシュテーブルを作ってみようとしたファイル
* hash_table_2.py - class Itemの使い方がよくわからず、連結リストを使わずに途中まで実装した 
* hash_table.py - **連結リストを使って実装した**
* time.txt - 計測した処理速度のログ
---
## 現状
```def functional_test()```はpassしたが<br>
```def performance_test()```が最後の```assert hash_table.size() == 0```で止まっている<br>

```
Traceback (most recent call last):
  File "/home/hirochi/STEP_homework/week2/hash_table_2.py", line 367, in <module>
    performance_test()
  File "/home/hirochi/STEP_homework/week2/hash_table_2.py", line 361, in performance_test
    assert hash_table.size() == 0
           ^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

**```def delete```内の、バケットサイズの縮小と```self.item_count```が上手くいっていなさそう**

ハッシュ関数を変えることで、大幅に処理速度を改善できたが、O(1)にはできていない<br>
再ハッシュ

---
## アルゴリズムについて-hash_table_2.py
<dl>
  <dt>Hash関数</dt>
<dd>keyに含まれる各文字のユニコードにindex足してから乗算することで、連結リストの数を減らすことができた</dd>

  <dt>HashTable : put</dt>
  <dd>
  * ハッシュ値をindexとし、各index内に```class item```で生成したitemを保存。<br>
  * 既にitemが存在した場合は、item内のnextに繋げることで連結リストとして保存。<br>
  * item数がテーブルのbucket数の70％を超えた場合、テーブルを2倍に拡張
 </dd>
 
<dt>HashTable : get</dt>
<dd>
  目的のkeyをハッシュテーブル＆連結リストから探し出し、valueを反す
</dd>

<dt>HashTable : delete</dt>
<dd>
  目的のkeyをテーブル＆連結リストから探し、削除する<br>
  keyが連結リスト内にあった場合は、削除の後、前後のitemをnextで繋げる
</dd>

---



#### 自分用メモ
最初連結リストのことを何も考えずリストの中にリスト作ってた。
self.～の書き方の理解が進んだ

currentに置き換えたところ、current.nextとか.keyとかつけると、元の値＝Itemオブジェクトが書き換わる
