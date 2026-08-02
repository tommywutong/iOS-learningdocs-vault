---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Introduction/Intro.html
archived_at: '2026-07-26T19:54:11.107544Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AudioUnitGeneratorExample-AUPinkNoiseVersion.h.md)

# Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2016-02-19 Updated for Xcode 7.2 and 10.11 SDK, removed deprecation warnings and updated Public Utility files and Base Classes, added MIDI Processor AU. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgojwhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.11.2 or later, Xcode 7.2 or later |
| __Runtime Requirements:__ | Mac OS X 10.8 or later |

AudioUnitExamples is a collection of Audio Unit Version 2 sample code. Each project demonstrates how to create an AudioUnit of a specific type (i.e. Effect, Generator, Instrument, MIDI Processor and Offline Effect).

AudioUnitEffectExample - Builds a simple low pass filter as an Effect AudioUnit with custom view.

AudioUnitGeneratorExample - Builds a pink noise generator as a Generator AudioUnit.

AudioUnitInstrumentExample - Builds a basic sin wave synth as an Instrument AudioUnit.

AudioUnitOfflineEffectExample - Builds a simple Offline Effect AudioUnit.

AudioUnitMidiProcessorExample - Builds a pass through midi processor. AU's of this type process midi input and produce midi output but do not produce any audio.

StarterAudioUnitExample (TremoloUnit) - This sample is referenced in the AudioUnit programming guide.

[Next](AudioUnitGeneratorExample-AUPinkNoiseVersion.h.md)

