import os

# merge ids from 2 files into 1 file:
# File 1: full_old.txt
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
# File 2: bird-shield-blocking\share\blacklist\profanity.txt
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
        full_old = f.readlines()
    with open('current.txt', 'r') as f:
        profanity = f.readlines()

    full_old = [x.strip() for x in full_old]
    profanity = [x.strip() for x in profanity]

    full_old = set(full_old)
    profanity = set(profanity)

    full_old = full_old.union(profanity)

    # destroy and create the file
    if os.path.exists('merge.txt'):
        os.remove('merge.txt')

    with open('merged.txt', 'w') as f:
        for id in full_old:
            f.write(id + '\n')

# Run the main function
if __name__ == "__main__":
    main()
