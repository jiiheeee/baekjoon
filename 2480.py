triple_dice = list(map(int, input().split()))

if triple_dice[0]==triple_dice[1]==triple_dice[2]:
    print(10000+triple_dice[0]*1000)
elif triple_dice[0]==triple_dice[1] or triple_dice[0]==triple_dice[2] or triple_dice[1]==triple_dice[2]:
    if triple_dice[0]==triple_dice[1]:
        print(1000+triple_dice[0]*100)
    elif triple_dice[0]==triple_dice[2]:
        print(1000+triple_dice[0]*100)
    else:
        print(1000+triple_dice[1]*100)
else:
    print(max(triple_dice)*100)