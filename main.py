import phrases
from cost import money_curd_price, money_scrambl_price, money_omelette_price

restaurant_name = 'Дача'
total_cost = 0

hello_client = input(phrases.hi.format(rest=restaurant_name))
name = input('Як до Вас можна звертатись?')
name = name.title()
name = name.strip()

curd_quantity = input(phrases.MSG_DISH.format(dish='Cир зі сметаною', price=money_curd_price))
curd_quantity = int(curd_quantity)
curd_price = money_curd_price * curd_quantity
total_cost = total_cost + curd_price

scrambl_quantity = input(phrases.MSG_DISH.format(dish='Яєшня "Шакшука"', price=money_scrambl_price))
scrambl_quantity = int(scrambl_quantity)
scrambl_price = money_scrambl_price * scrambl_quantity
total_cost = total_cost + scrambl_price

omelette_quantity = input(phrases.MSG_DISH.format(dish='Oмлет з сиром з молока одеських кіз',
                                                  price=money_omelette_price))
omelette_quantity = int(omelette_quantity)
omelette_price = money_omelette_price * omelette_quantity
total_cost = total_cost + omelette_price

discount_t = input(phrases.discount_p.format(name=name))
print(f'Сума без знижки: {round(total_cost, 2)} грн')
discount = total_cost * 0.15
print(f'Сума знижки: {round(discount, 2)} грн')
total_cost = total_cost - discount
print(f'Сума зі знижкою: {round(total_cost, 2)} грн')
thank_you_client = input(phrases.thank_you.format(name=name))

print('ЧЕК:')
print("-" * 50)
print(f'Сир зі сметаною x{curd_quantity} = {curd_price} грн')
print(f'Яєшня "Шакшука"  x{scrambl_quantity} = {scrambl_price} грн')
print(f'Oмлет з сиром з молока одеських кіз x{omelette_quantity} =  {scrambl_price} грн')
print("-" * 50)
print(f'Сума: {round(total_cost, 2)} грн')
print(f'Знижка: {round(discount, 2)} грн')
print(f'До сплати: {round(total_cost, 2)} грн')
print("-" * 50)
