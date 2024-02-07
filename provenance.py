#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json, ast, sys
import datetime, time, copy
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import networkx as nx

#--------------------------------------------------------------------------#  
arg = ["0406", "0411", "0412"]
ath = '/media/enb213/dataset/DARPA/TC3/cadets/parsing/'
dirPath = [f"{ath}{arg[0]}/output/", 
            f"{ath}{arg[1]}/output/", 
            f"{ath}{arg[2]}/output/"]
IDStree = nx.DiGraph()

#--------------------------------------------------------------------------#  
# num = 0
# for i in range(3):
# 	for j in range(len(os.listdir(f"{dirPath[i]}Event"))):
# 		print(f"Reading {dirPath[i]}Event/Event-{j}.txt ......")
# 		rfile = open(f"{dirPath[i]}Event/Event-{j}.txt", 'r', encoding="UTF-8")
# 		for log in rfile.readlines():
# 			log = ast.literal_eval(log)

# 			if not log["subjectId"]:
# 				continue

# 			ent = log["type"]
# 			sub = log["subjectId"]
# 			obj = log["predicateObjectId"]
# 			ob2 = log["predicateObject2"]
# 			fname = log["predicateObjectPath"]
# 			sname = log["predicateObject2Path"]

# 			if sub not in IDStree:
# 				IDStree.add_node(sub)

# 			if ent == "EVENT_FORK":
# 				if obj not in IDStree:
# 					IDStree.add_node(obj)
# 				IDStree.add_edge(sub, obj)

# 			if ent == "EVENT_WRITE":
# 				if not obj:
# 					continue
# 				# file = fname["string"]
# 				# if file not in IDStree:
# 				# 	IDStree.add_node(file)
# 				# IDStree.add_edge(sub, file)
# 				if obj not in IDStree:
# 					IDStree.add_node(obj)
# 					num += 1
# 				IDStree.add_edge(sub, obj)

# 			if ent in ["EVENT_READ", "EVENT_OPEN"]:
# 				if not obj:
# 					continue
# 				# file = fname["string"]
# 				# if file not in IDStree:
# 				# 	IDStree.add_node(file)
# 				# IDStree.add_edge(file, sub)
# 				if obj not in IDStree:
# 					num += 1
# 					IDStree.add_node(obj)
# 				IDStree.add_edge(obj, sub)

# 			if ent == ["EVENT_RENAME", "EVENT_LINK"]:
# 				if not obj or not ob2:
# 					continue
# 				# file = fname["string"]
# 				# if file not in IDStree:
# 				# 	IDStree.add_node(file)
# 				# IDStree.add_edge(file, sub)
# 				# file = sname["string"]
# 				# if file not in IDStree:
# 				# 	IDStree.add_node(file)
# 				# IDStree.add_edge(sub, file)
# 				if obj not in IDStree:
# 					num += 1
# 					IDStree.add_node(obj)
# 				IDStree.add_edge(obj, sub)
# 				if ob2 not in IDStree:
# 					num += 1
# 					IDStree.add_node(ob2)
# 				IDStree.add_edge(sub, ob2)

# print(num)
# data = json_graph.node_link_data(IDStree)
# with open(f"{ath}tradition.json", "w") as FILE:
#     json.dump(data, FILE, indent=4)
# FILE.close()

cnt = 0
for i in range(3):
	print(f"Reading {dirPath[i]}info/fork.txt ......")
	rfile = open(f"{dirPath[i]}info/fork.txt", 'r', encoding="UTF-8")
	for log in rfile.readlines():
		log = ast.literal_eval(log)
		ent = log["type"]
		if ent == "EVENT_EXECUTE":
			cnt += 1
print(cnt)
# fileset = dict()
# for i in range(3):
	# for j in range(len(os.listdir(f"{dirPath[i]}info"))):
		# print(f"Reading {dirPath[i]}info/fork.txt ......")
		# rfile = open(f"{dirPath[i]}info/fork.txt", 'r', encoding="UTF-8")
		# for log in rfile.readlines():
		# 	log = ast.literal_eval(log)
		# 	uuid = log["uuid"]
		# 	if uuid not in fileset:
		# 		fileset[uuid] = set()

# for i in range(3):
# 	for j in range(len(os.listdir(f"{dirPath[i]}Event"))):
# 		print(f"Reading {dirPath[i]}Event/Event-{j}.txt ......")
# 		rfile = open(f"{dirPath[i]}Event/Event-{j}.txt", 'r', encoding="UTF-8")
# 		for log in rfile.readlines():
# 			log = ast.literal_eval(log)

# 			if not log["subjectId"]:
# 				continue

# 			ent = log["type"]
# 			sub = log["subjectId"]
# 			obj = log["predicateObjectId"]
# 			fname = log["predicateObjectPath"]
# 			sname = log["predicateObject2Path"]

# 			if obj in fileset and fname:
# 				fname = fname["string"]
# 				# print(fileset[obj])
# 				fileset[obj].add(fname)

# cnt = [0, 0, 0]
# for key in fileset:
# 	if len(fileset[key]) == 0:
# 		cnt[0] += 1
# 	if len(fileset[key]) == 1:
# 		cnt[1] += 1
# 	if len(fileset[key]) > 1:
# 		cnt[2] += 1

# print(len(fileset), cnt)