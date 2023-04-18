lvls = input("Введите уровни, раздляя их с помощью '^': ")
lvls = lvls.split("^")

all_amount = 0
all_old_amount = 0
all_stacks = 0
all_shulkers = 0
all_double_chests = 0
        
i = 0
for lvl in lvls:
    i = i + 1
    
    lvl = int(lvl)
    
    amount = (4.5 * (lvl * lvl) - 162.5 * lvl + 2220) // 149720
    old_amount = amount

    stacks = 0
    shulkers = 0
    double_chests = 0

    if amount >= 93_312:
        double_chests = amount // 93_312
        amount = amount % 93_312
    if amount >= 1_728:
        shulkers = amount // 1_728
        amount = amount % 1_728 
    if amount >= 64:
        stacks = amount // 64
        amount = amount % 64

    price = old_amount * 500_000
    print(f"{i}. Губки: {old_amount} ({double_chests} дбч., {shulkers} шк., {stacks} стаков и {amount} шт.). Цена: {price}")

    all_amount = all_amount + amount
    all_old_amount = all_old_amount + old_amount
    all_stacks = all_stacks + stacks
    all_shulkers = all_shulkers + shulkers
    all_double_chests = all_double_chests + double_chests

    all_amount = all_stacks * 64 + all_shulkers * 27 * 64 + all_double_chests * 54 * 27 * 64 + all_amount
    
    if all_amount >= 93_312:
        all_double_chests = all_amount // 93_312
        all_amount = all_amount % 93_312
    if all_amount >= 1_728:
        all_shulkers = all_amount // 1_728
        all_amount = all_amount % 1_728 
    if all_amount >= 64:
        all_stacks = all_amount // 64
        all_amount = all_amount % 64


    price = all_old_amount * 500_000
    print(
        f"> Все губки: {all_old_amount} ({all_double_chests} дбч., {all_shulkers} шк., {all_stacks} стаков и {all_amount} шт.). Цена: {price}")