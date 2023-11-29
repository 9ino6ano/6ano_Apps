from midiutil import MIDIFile


def create_custom_midi(notes, output_file, bpm=120, duration=120):
    # Create a MIDI file
    midi = MIDIFile(1)

    # Add a track to the MIDI file
    track = 0
    midi.addTempo(track, 0, bpm)

    # Add melody and chords to the MIDI file
    channel = 0
    volume = 100
    time = 0

    for _ in range(duration):
        for pitch in notes:
            midi.addNote(track, channel, pitch, time, 0.5, volume)
            time += 0.5

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi.writeFile(file)

# Jazz-inspired MIDI pattern
jazz_notes = [60, 62, 64, 65, 67, 69, 71, 72]
create_custom_midi(jazz_notes, 'jazz_inspired_pattern.mid', bpm=120)

# R&B-inspired MIDI pattern
rnb_notes = [56, 58, 60, 61, 63, 65, 67, 68]
create_custom_midi(rnb_notes, 'rnb_inspired_pattern.mid', bpm=120)

# Reggae-inspired MIDI pattern
reggae_notes = [48, 50, 52, 53, 55, 57, 59, 60]
create_custom_midi(reggae_notes, 'reggae_inspired_pattern.mid', bpm=120)

# Additional patterns for variety
create_custom_midi(jazz_notes[::-1], 'jazz_variation_pattern.mid', bpm=120)
create_custom_midi(rnb_notes[::-1], 'rnb_variation_pattern.mid', bpm=120)

print("Custom MIDI patterns inspired by jazz, R&B, and reggae generated successfully.")
