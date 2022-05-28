# coding:utf-8
def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    start_idx = 0                # 探索区間の先頭のインデックス
    end_idx = len(sorted_array)  # 探索区間の最後尾のインデックス+1

    while(start_idx != end_idx):
        # 探索区間の中間のインデックスを求める
        idx = start_idx + (end_idx - start_idx) // 2

        if sorted_array[idx] == target_number:  # 中間の値がtarget_numberと一致している
            return idx
        elif sorted_array[idx] > target_number: # 中間の値がtarget_numberより大きいとき
            end_idx = idx
        else:                                   # 中間の値がtarget_number以下のとき
            start_idx = idx + 1                 # 存在しない数字をtarget_numberにされたときに
                                                # 終了条件を満たすようにするためにidx+1にした
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
