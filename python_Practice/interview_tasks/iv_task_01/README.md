# Задача
- Три головы Змея Горыныча 3 часа смотрят в разные стороны.
- Первая голова 10 минут вперёд, затем 10 минут назад, потом 10 минут налево и 10 минут направо, снова 10 минут вперёд и так далее по циклу.
- Вторая голова 15 минут смотрит назад, затем 15 минут налево, потом 15 минут направо, снова назад и так далее по циклу.
- Третья голова 20 минут смотрит направо, 20 минут налево, 20 минут вперёд, снова направо и так далее по циклу.
- Сколько минут все три головы смотрели в одну сторону одновременно? Опишите решение.

# Решение
Только код [здесь](https://github.com/v-las/Python/blob/main/Exercises/interview_tasks/iv_task_01/pure_code.py)
```sh
def tick_count(ticks, turns, time):
    """
    Создаётся и итерируется копия списка минут.
    К каждой минуте добавляется направление головы.
    При каждом времени поворота в списке направлений первый элемент
    перемещается в конец, чтобы добавлялся следующий.
    :param ticks: Список минут.
    :param turns: Список направлений головы.
    :param time: Время поворота.
    :return: Список минут с направлением головы в каждую минуту.
    """
    ticks_copy = ticks.copy()
    for i in list(ticks_copy):
        if ticks_copy[i] % time == 0 and i != 0:
            turns.append(turns.pop(0))
        ticks_copy[i] = str(ticks_copy[i]) + turns[0]
    return ticks_copy


head_ticks = [i for i in range(180)]  # Создаётся список минут в трёх часах
# Для каждой головы: время поворота и направления отправляются в функцию
head_1_workout = tick_count(head_ticks, ['f', 'b', 'l', 'r'], 10)
head_2_workout = tick_count(head_ticks, ['b', 'l', 'r'], 15)
head_3_workout = tick_count(head_ticks, ['r', 'l', 'f'], 20)
minute_list = []
for i in head_ticks:  # Итерируется список для поиска совпадений
    if head_1_workout[i] == head_2_workout[i] == head_3_workout[i]:  # Сравниваются между собой списки трёх голов
        minute_list.append(i)  # Совпадения (минуты с одинаковым направлением) добавляются в лист
# Вывод в консоль подсчитанных элементов листа (минут)
print("Три головы смотрели в одну сторону", len(minute_list), "минут.")

```