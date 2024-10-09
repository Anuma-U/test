team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
challenge_result = result
s1 = "В команде Мастера кода участников: %s!" % team1_num
print(s1)
s2 = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
print(s2)
s3 = "Команда Волшебники данных решила задач: {}{}".format(score_2,"!")
print(s3)
s4 = "Волшебники данных решили задачи за {}.c !".format(team1_time)
print(s4)
s5 = f"Команды решили {score_1} и {score_2} задач."
print(s5)
s6 = f"Результат битвы: {challenge_result}"
print(s6)
s7 = f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg)} секунды на задачу!."
print(s7)