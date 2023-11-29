from midiutil import MIDIFile


def create_midi(scale, output_file, bpm=113, duration=120):
    # Create a MIDI file
    midi = MIDIFile(1)

    # Add a track to the MIDI file
    track = 0
    midi.addTempo(track, 0, bpm)

    # Define the scale notes
    scale_notes = [scale(i) for i in range(8)]

    # Add melody notes to the MIDI file
    channel = 0
    volume = 100
    time = 0

    for _ in range(duration // 2):
        for pitch in scale_notes:
            midi.addNote(track, channel, pitch, time, 0.5, volume)
            time += 0.5

    # Add a transition melody
    transition_scale = [scale(i) for i in range(4)]
    for _ in range(duration // 4):
        for pitch in transition_scale:
            midi.addNote(track, channel, pitch, time, 0.25, volume)
            time += 0.25

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi.writeFile(file)


# Example scales (you can replace these with your preferred scales)
def major_scale(i):
    return 60 + (i % 7) * 2 + (i // 7) * 12


def minor_scale(i):
    return 60 + (i % 7) * 2 + (i // 7) * 12 - 1


# Create MIDI patterns for five different scales
for i in range(1, 6):
    scale_name = f"Scale_{i}"
    output_file = f"{scale_name}_pattern.mid"
    scale_function = major_scale if i % 2 == 0 else minor_scale
    create_midi(scale_function, output_file)

print("MIDI patterns generated successfully.")
