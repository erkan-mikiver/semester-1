# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music_db = {
    "Future": ['Codeine Crazy', 'Throwaway', 'Stick to the Models', 'Serve the Base'],
    "The Weeknd": [{'Twenty Eight': 258}, {'Adaptation': 283}, {'Wicked Games': 323}, {'Often': 249}]}

# Pretty-print the data structure
pprint(music_db)
print()
# Display details of one album recorded by a specific artist
pprint(music_db['The Weeknd'][0].keys())
