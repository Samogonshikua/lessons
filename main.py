#   # 1# value = int(input("баланс в  тугриках: "))# if value <= 0:#     print("початківець")# elif value <= 100:#     print("нормис") # нормис# elif value <= 1000:#     print("деген")  # деген# elif value <= 10000:#     print("кит")  # кит# else:#     print("Ілон Маск")  # Илон Маск# 2# Условие:# Напишите программу, которая генерирует цену на газ (от 10 до 100) и начальный баланс кошелька (от 2000 до 10000) при помощи random.randint()## Стоимость операций:## мост стоит = цена газа * 75# свап стоит = цена газа * 40# минт домена стоит = цена газа * 100# Если на кошельке недостаточно средств для операций, программа должна имитировать вывод недостающей суммы с биржи:## посчитать сумму вывода# вывести сообщение о выводе# прибавить сумму вывода к балансу# Дальнейшая логика программы:## Если цена на газ ниже 25, то программа запускает мост Scroll, расходы должны вычитаться с баланса.# Если цена на газ ниже 15, то после запуска моста программа должна еще сминтить домен, расходы должны вычитаться с баланса.# Если цена на газ выше 25, то программа запускает свап, расходы должны вычитаться с баланса.# Если цена на газ выше 50, то программа ничего не делает и рекомендует поработать в другой раз. В конце программа выводит сообщение о завершении работы, указывает выполненные операции и оставшийся баланс кошелька.# import random### gas_price = random.randint(10, 100)# print(f"Gas {gas_price}")# balance_wallet = random.randint(2000, 10000)# print(f"вивів  суму {balance_wallet}")## bridget = gas_price * 75# swap = gas_price * 40# mint = gas_price * 100## chec_balance = balance_wallet < 2600## if chec_balance:#     wizard_okx = random.randint(200, 500)#     print(f"вивів  суму з OKX {wizard_okx}")#     balance_wallet += wizard_okx#     print(f"новий  баланс {balance_wallet}")## if gas_price < 15:#     mint_domein = balance_wallet - mint#     print(f"залишок балансу {mint_domein}")#     last_operation = "mint_domein"## elif gas_price < 25:#     bridget_srcoll = balance_wallet - bridget#     print(f"залишок балансу {bridget_srcoll}")#     last_operation = "bridget"## elif gas_price > 25:#     swap_izumi = balance_wallet - swap#     print(f"залишок балансу {swap_izumi}")#     last_operation =  "swap"## elif gas_price > 50:#     print(f"газ {gas_price}, високий пропустить усе ")### print(f"Роботу завершив, баланс гаманця {balance_wallet}, зробив {last_operation}")# 3# У вас есть 2 переменные с балансами кошелька в токене ETH и USDT. Еще одна переменная описывает стоимость ETH в USDT.## Напишите программу, которая будет делать обмен из ETH в USDT если баланс USDT нулевой, при этом оставляя 5% токенов ETH на комиссии.## Если баланс USDT не нулевой, то программа должна делать обмен всех токенов USDT в ETH.## Во время обмена должно печататься в терминале какой токен меняется на какой и какая сумма обмена. По результату обмена программа балансы должны меняться.## Продублируйте логику, чтобы программа делала 5 обменов из ETH в USDT и обратно, сама выбирая когда и какой обмен делать.## В конце работы программа должна выводить сообщение актуальный баланс токенов ETH и USDC.import randomETH_bal = random.uniform(0.1, 1)print(f"ETH_bal {ETH_bal:.5f}")USDT_bal = random.randint(0, 1)print(f"USDT_bal {USDT_bal}")swap_balance_ETH = 0.95 # %ETH = 2600for i in range(5):    if USDT_bal == 0:        swap_procent = ETH_bal * swap_balance_ETH        swap = round(swap_procent * ETH, 2)        print(f"swap ETH to USDT value: {swap}")        ETH_bal = ETH_bal - swap_procent        USDT_bal = swap + USDT_bal    else:        swap = USDT_bal / ETH + ETH_bal        ETH_bal = round(swap, 5)        USDT_bal = USDT_bal - USDT_bal  # USDT_bal = 0        print(f"swap USDT to ETH value: {ETH_bal}")print("---------------------------------")print(f"ETH_bal {ETH_bal:.5f}")print(f"USDT_bal {USDT_bal}")