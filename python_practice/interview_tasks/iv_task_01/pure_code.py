def tick_count(ticks, turns, time):
    ticks_copy = ticks.copy()
    for i in list(ticks_copy):
        if ticks_copy[i] % time == 0 and i != 0:
            turns.append(turns.pop(0))
        ticks_copy[i] = str(ticks_copy[i]) + turns[0]
    return ticks_copy


head_ticks = [i for i in range(180)]
head_1_workout = tick_count(head_ticks, ['f', 'b', 'l', 'r'], 10)
head_2_workout = tick_count(head_ticks, ['b', 'l', 'r'], 15)
head_3_workout = tick_count(head_ticks, ['r', 'l', 'f'], 20)
minute_list = []
for i in head_ticks:
    if head_1_workout[i] == head_2_workout[i] == head_3_workout[i]:
        minute_list.append(i)
print("Три головы смотрели в одну сторону", len(minute_list), "минут.")
