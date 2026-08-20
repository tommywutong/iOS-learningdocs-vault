---
title: AudioUnitInstrumentExample
apple_id: DTS40008641
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/SinSynth/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:24:37.675063Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitInstrumentExample](AudioUnitInstrumentExample.md)


[Next](AUPublic-AUBase-AUBase.cpp.md)[Previous](AudioUnitInstrumentExample.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# ReadMe.txt

```
### SinSynth ###

===========================================================================
DESCRIPTION:

This is a test implementation of a sin wave synth using AUInstrumentBase classes

It illustrates a basic usage of these classes

It artificially limits the number of notes at one time to 12, so the note-stealing algorithm is used - you should know how this works!

Most of the work you need to do is defining a Note class (see TestNote). AUInstrument manages the creation and destruction of notes, the various stages of a note's lifetime.

Alot of printfs have been left in (but are if'def out)

These can be useful as you figure out how this all fits together. This is true in the AUInstrumentBase classes as well; simply define DEBUG_PRINT to 1 and this turns all this on

The project also defines CA_AUTO_MIDI_MAP (OTHER_C_FLAGS). This adds all the code that is needed to map MIDI messages to specific parameter changes. This can be seen in AU Lab's MIDI Editor window CA_AUTO_MIDI_MAP is implemented in AUMIDIBase.cpp/.h

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.7 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.7 or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2012 Apple Inc. All rights reserved.
```

[Next](AUPublic-AUBase-AUBase.cpp.md)[Previous](AudioUnitInstrumentExample.md)

