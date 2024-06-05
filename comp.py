import os

# compare ids between 2 files and 1 file:
# File 1: last.txt
# 822483727846690818
# 853130355884171266
# 857515782942597120
# 871906969409290241
# 873107944421838849
# 885406944936079360
# 885763838112550913
# 900242398466326528
# 912024602091630599
# 912555216750485504
# 930846111526457344
# 938325763245215744
# 947255767454777344
# 954568650366660608
# 965850517984501760
# 981649471263031296
# 985416117022871552
# 995510809047351296
# ...
#
# File 2: current.txt
# 1029169393828339712
# 1045095227415912448
# 1064679200
# 1067697301466996736
# 1068336010554044416
# 1081768523905417216
# 109186648
# 1112515788676583424
# 1116362854901305347
# 1124861281695965184
# 1133743755696189443
# 1136289349
# 1143456188438208513
# 1143589957744787456
# 1148511765396770816
# 115714330
# ...

def main():
    with open('last.txt', 'r') as f:
        last_arr = f.readlines()
    with open('current.txt', 'r') as f:
        curr_arr = f.readlines()

    last_arr = [x.strip() for x in last_arr]
    curr_arr = [x.strip() for x in curr_arr]

    last_arr = set(last_arr)
    curr_arr = set(curr_arr)

    # find the difference between 2 sets
    plus_arr = curr_arr.difference(last_arr)
    minus_arr = last_arr.difference(curr_arr)
    
    # Output difference to diff.txt

    # destroy and create the file
    if os.path.exists('diff.txt'):
        os.remove('diff.txt')

    with open('diff.txt', 'w') as f:
        # output '++++++++++++++++++++++++++' line to separate the 2 sets
        f.write('+++++++++++++++++++++++++++++++++++++++++++\n')
        f.write('+++++++++++++++++++++++++++++++++++++++++++\n')
        for id in plus_arr:
            f.write('+' + id + '\n')
        # output '--------------------------' line to separate the 2 sets
        f.write('-------------------------------------------\n')
        f.write('-------------------------------------------\n')
        for id in minus_arr:
            f.write('-' + id + '\n')

# Run the main function
if __name__ == "__main__":
    main()
