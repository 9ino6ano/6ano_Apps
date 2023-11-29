from midiutil import MIDIFile

def create_midi(scale, output_file, bpm=120, duration=120):
    # Create a MIDI file
    midi = MIDIFile(1)

    # Add a track to the MIDI file
    track = 0
    midi.addTempo(track, 0, bpm)

    # Add melody notes to the MIDI file
    channel = 0
    volume = 100
    time = 0

    for _ in range(duration):
        for pitch in scale:
            midi.addNote(track, channel, pitch, time, 0.5, volume)
            time += 0.5

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi.writeFile(file)

# Example scales
a_major_scale = [57, 59, 61, 62, 64, 66, 68, 69]
b_major_scale = [59, 61, 63, 64, 66, 68, 70, 71]
c_major_scale = [60, 62, 64, 65, 67, 69, 71, 72]
g_major_scale = [55, 57, 59, 60, 62, 64, 66, 67]
f_major_scale = [53, 55, 57, 58, 60, 62, 64, 65]
# Example scale
d_major_scale = [62, 64, 66, 67, 69, 71, 73, 74]


# Create MIDI patterns for different scales
create_midi(a_major_scale, 'A_major_pattern.mid', bpm=120)
create_midi(b_major_scale, 'B_major_pattern.mid', bpm=120)
create_midi(c_major_scale, 'C_major_pattern.mid', bpm=120)
create_midi(g_major_scale, 'G_major_pattern.mid', bpm=120)
create_midi(f_major_scale, 'F_major_pattern.mid', bpm=120)
# Create a MIDI pattern for the D major scale
create_midi(d_major_scale, 'D_major_pattern.mid', bpm=120)

print("MIDI patterns generated successfully.")

