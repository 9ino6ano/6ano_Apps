from midiutil import MIDIFile

def create_midi(melody_notes, output_file='relaxing_piano.mid'):
    # Create a MIDI file
    midi = MIDIFile(1)

    # Add a track to the MIDI file
    track = 0
    midi.addTrackName(track, 0, "Relaxing Piano")
    midi.addTempo(track, 0, 60)

    # Add melody notes to the MIDI file
    channel = 0
    volume = 100
    time = 0

    for pitch, duration in melody_notes:
        midi.addNote(track, channel, pitch, time, duration, volume)
        time += duration

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi.writeFile(file)

# Example melody notes (pitch, duration)
melody_notes = [
    (60, 1.0),  # C4 quarter note
    (64, 0.5),  # E4 eighth note
    (62, 0.5),  # D4 eighth note
    # Add more notes as needed
]

create_midi(melody_notes)
