import os
import json
file_name = 'planner.json'
def show_event():
    if not os.path.exists(file_name):
        return {},1
    with open('planner.json','r',encoding='utf-8') as file:
        planner = json.load(file)
    if planner:
        next_id = max(map(int , planner.keys())) + 1
    return planner, next_id
def save_events(planner):
    with open(file_name,'w',encoding='utf-8') as file:
        json.dump(planner,file,ensure_ascii=False,indent=4)
def show_menu():
    print('\nПерсональний планувальник')
    print('1.Додати подію')
    print('2. Переглянути події')
    print('3. Видалити подію')
    print('4. Знайти подію за датою')
    print('5. Вийти')
def add_event(planner,event_id):
    name = input('Назва події: ')
    date = input('Число(YYYY:MM:DD):')
    time = input('Час(HH:MM):')
    description = input('Опис вашої події: ')
    planner[str(event_id)] = {
        'title': name,
        'date': date,
        'time':time,
        'description':description
    }
    save_events(planner)
    print('Подію додано')
    return event_id+1
def show_events(planner):
    if not planner:
        print('Подій немає')
        return
    for event_id,event in planner.items():
        print(f'\nID: {event_id}')
        print(f'Назва: {event['title']}')
        print(f'Дата: {event['date']}')
        print(f'Час: {event['time']}')
        print(f'Опис: {event['description']}')
def delete_event(planner):
    event_id = input('Виберіть ID події, яку хочете видалити')
    if event_id in planner:
        del planner[event_id]
        save_events(planner)
        print('Подію видалено')
    else:
        print('Події не знайдено, або не існує')
def find_by_date(planner):
    date = input('Введіть дату(YYYY-MM-DD): ')
    found = False
    for event_id,event in planner.items():
        if event['date'] == date:
            print(f'ID: {event_id}')
            print(f'Назва: {event['title']}')
            print(f'Дата: {event['date']}')
            print(f'Час: {event['time']}')
            print(f'Опис: {event['description']}')
            found = True
    if not found:
        print('Подій на цю дату немає')
   
def main():
    planner, event_id = show_event()
    while True:
        show_menu()
        choise = input('Виберіть дію')
        if choise == '1':
            event_id = add_event(planner,event_id)
        if choise == '2':
            show_events(planner)
        if choise == '3':
            delete_event(planner)
        if choise == '4':
            find_by_date(planner)
        if choise == '5':
            print('До побачення')
            break
        else:
            print('Невірний вибір')
            continue
if __name__ == '__main__':
    main()