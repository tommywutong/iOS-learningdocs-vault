---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitInstrumentExample_ReadMe_md.html
archived_at: '2026-07-26T19:54:11.897814Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitInstrumentExample-SinSynthWithMidi.cpp.md)[Previous](AudioUnitInstrumentExample-SinSynth.h.md)

# AudioUnitInstrumentExample/ReadMe.md

```
ReadMe for SinSynth & SinSynthWithMidi
-------------------

SinSynth is a test implementation of a sin wave synth using AUInstrumentBase classes.
It artificially limits the number of notes at one time to 12, by using note-stealing algorithm.
Most of the work you need to do is defining a Note class (see TestNote). AUInstrumentBase manages the creation and destruction of notes, the various stages of a note's lifetime.

A lot of printfs have been left in (but are if'def out)
These can be useful as you figure out how this all fits together. This is true in the AUInstrumentBase class as well; To view the debug messages simply define DEBUG_PRINT to 1.

The project also defines CA_AUTO_MIDI_MAP (in OTHER_C_FLAGS). This adds all the code that is needed to map MIDI messages to specific parameter changes. This can be seen in AU Lab's MIDI Editor window. CA_AUTO_MIDI_MAP is implemented in AUMIDIBase.cpp/.h

SinSynthWithMIDI is a subclass of SinSynth that demonstrates how to use the midi output properties kAudioUnitProperty_MIDIOutputCallbackInfo,and kAudioUnitProperty_MIDIOutputCallback defined in AudioUnitProperties.h.

Using these properties, the SinSynthWithMidi simply passes through the midi data it receives. Use of these properties requires host support.

To build a version of the SinSynth with this functionality, activate the "SinSynth with MIDI Output" target in Xcode.
```

[Next](AudioUnitInstrumentExample-SinSynthWithMidi.cpp.md)[Previous](AudioUnitInstrumentExample-SinSynth.h.md)

