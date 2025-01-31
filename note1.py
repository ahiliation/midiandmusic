import mingus.core.intervals as itv
from mingus.containers import Note

melody = []
note1 = Note("A", 4)
melody.append(note1)

for i in range(3):
    next_note = itv.interval("A", melody[i], 1)    
    melody.append(next_note)

print(melody) 

