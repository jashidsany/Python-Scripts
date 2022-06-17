import pickle

hackers = {"neut": 1, "geohot": 100, "neo": 1000}

for key, value in hackers.items():
	print(key, value)

serialised = pickle.dumps(hackers)
print(serialised)

hackers2 = pickle.loads(serialised)
print(hackers2)

for key, value in hackers2.items():
	print(key, value)

with open("hackers.pickle", "wb") as handle:
	pickle.dump(hackers, handle)

with open("hackers.pickle", "rb") as handle:
	hackers3 = pickle.load(handle)

print(hackers3)