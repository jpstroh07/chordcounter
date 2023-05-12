from persistence import ProgressHandler

h = ProgressHandler.ProgressHandler()

h.insertProgress("C", "D", 1)

print(h.getProgress())