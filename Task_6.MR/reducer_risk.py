#!/usr/bin/env python3
import sys
from collections import defaultdict

def reducer():
    user_activity = defaultdict(list)
    
    for line in sys.stdin:
        userid, s_all = line.strip().split('\t')
        user_activity[userid].append(float(s_all))
    
    # Вычисляем среднюю активность для каждого студента
    avg_activity = []
    for userid, activities in user_activity.items():
        avg = sum(activities) / len(activities)
        avg_activity.append((avg, userid))
    
    # Сортируем по возрастанию активности и берем топ-10 самых неактивных
    avg_activity.sort()
    for avg, userid in avg_activity[:10]:
        print(f"{userid}\t{avg:.2f}")

if __name__ == '__main__':
    reducer()