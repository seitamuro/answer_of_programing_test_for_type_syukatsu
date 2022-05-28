# coding:utf-8
def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    # SyntaxErrorが出たので表示方法を変えました
    #[print(i) for i in sortedArray]

    for i in sortedArray:
        print(i)

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    start_idx = 0
    end_idx = len(array)
    while end_idx - start_idx > 1:
        while pivot > array[start_idx]:
            start_idx += 1
        while pivot < array[end_idx-1]:
            end_idx -= 1
        if end_idx - start_idx > 1:
            tmp = array[start_idx]
            array[start_idx] = array[end_idx-1]
            array[end_idx-1] = tmp

    # pivotが一番先頭にあるときのみpivotとそれ以外のグループに分類する
    if start_idx == 0:
        return [array[0]] + sort(array[1:])
    else:
        return sort(array[0:start_idx]) + sort(array[start_idx:])
    # ここまで記述

if __name__ == '__main__':
    main()
