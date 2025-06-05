import os
import re
import json
import socket
import subprocess
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import utils as pu
from pyspark.sql import functions as F
from pyspark.sql import types as pt
import sys
from collections import defaultdict

def hdfs_read_lines(hdfs_path):
    process = subprocess.Popen(['hdfs', 'dfs', '-cat', hdfs_path], 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = process.communicate()
    return stdout.decode('utf-8').split('\n')
    
def task3():
    lines = hdfs_read_lines('/jovyan/aggrigation_logs_per_week.csv')
    course_users = defaultdict(set)
    
    for line in lines[1:]:
        if line.strip():
            parts = line.split(',')
            courseid = parts[0]
            userid = parts[1]
            course_users[courseid].add(userid)
    
    with open('task3_result.txt', 'w') as f:
        for course, users in course_users.items():
            f.write(f"{course}\t{len(users)}\n")
    
    print("Готово! Результаты в task3_result.txt")
    return course_users

task3_result = task3()