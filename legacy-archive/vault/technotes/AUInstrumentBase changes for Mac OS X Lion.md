---
title: AUInstrumentBase changes for Mac OS X Lion
apple_id: DTS40011363
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2011-11-29'
source_url: https://developer.apple.com/library/archive/technotes/tn2291/_index.html
archived_at: '2026-07-26T19:54:10.157628Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2291

# AUInstrumentBase changes for Mac OS X Lion

This Technical Note lists changes made to the `AUInstrumentBase` classes for Mac OS X Lion. When building an Audio Unit on Mac OS X Lion that make use of these public utility classes, you will need to update your project accordingly.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi4yq)[AUInstrumentBase](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi4za)[New Methods](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi4zc2tsfk5pu2rkujbhuiuy)[Methods Removed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi4zc2tkfkree6rctl5jektkpkzcui)[SynthNote](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi4zq)[SynthElement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42a)[Methods Removed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42c2tkfkree6rctl5jektkpkzcui)[MidiControls](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42c2tkjireugt2okrje6tct)[SynthGroupElement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42q)[New Methods](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42s2tsfk5pu2rkujbhuiuy)[Methods Removed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42s2tkfkree6rctl5jektkpkzcui)[Other Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwugsbrfvke4vcbi42s2t2ujbcvex2djbau4r2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzwgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The AUInstrumentBase folder is part of the Xcode Developer tools and is located in `Developer/Extras/CoreAudio/AudioUnits/AUPublic/AUInstrumentBase`. This folder contains a number of classes used when building Audio Unit Instruments.

A number of changes have been made to these public utility files for Mac OS X Lion as listed:

[Back to Top](#)

## AUInstrumentBase

### New Methods

- `AUScope & Parts()`
- `AUElement* GetPart(AudioUnitElement inElement)`
- `virtual AUScope* GetScopeExtended(AudioUnitScope inScope)`
- `virtual void CreateExtendedElements()`

These methods allow subclasses to make use of the Part scope which represents specific instruments, patches and presets associated with the AUInstrumentBase.

### Methods Removed

- `MidiControls* GetControls( MusicDeviceGroupID inChannel)`

MIDI notification messages are handled via methods called directly on the appropriate `SynthGroupElement` instance.

[Back to Top](#)

## SynthNote

- `AttackNote()` now returns a `bool` - This allows `SynthElement` to not place a `SynthNote` instance into the active queue if the note will not be played (due to voice logic of any sort).
- `AttackNote()` argument 4 (`inAbsoluteSampleFrame`) changed from `SInt64` to `UInt64` - Start frame is always positive, and is unsigned in other uses in the system. This also allows more frames before value will wrap.
- `Render()` takes an additional argument, the first argument is: `inAbsoluteSampleFrame` - This is to allow a subclass to handle the "will this note play" logic (see AttackNote()).
- `Attack()` now returns a `bool`.
- `GetState()` returns `SynthNoteState` enum type - The member value being returned is this type.
- `GetAbsoluteStartFrame()` now returns `UInt64` instead of `SInt64` - Start frame is always positive, and is unsigned in other uses in the system.
- `PitchBend()` is now `GetPitchBend()` - Old name was misleading -- sounded like it performed an action when this is just a 'getter'.
- `SampleRate()` is virtual - Like `Frequency()` the subclass may want to override this.

[Back to Top](#)

## SynthElement

### Methods Removed

- `GetName()`
- `SetName()`

`SynthElement` is derived from `AUElement` which already has these methods and they are non-virtual. Overriding at this level could produce inconsistent results.

### MidiControls

`MidiControls` has been promoted to be a subclass of a new base class called `MIDIControlHandler` which defines a useful interface for working with MIDI events. The constants have been moved into the base class header.

[Back to Top](#)

## SynthGroupElement

### New Methods

- `virtual NoteOn()`
- `NoteFastReleased()`
- `ChannelMessage()`

### Methods Removed

- `GetOutputBus()`
- `SetOutputBus()`

For a multi-channel instrument, the concept of a single bus index does not make sense. This state is better handled by subclasses.

### Other Changes

- `Render()` takes additional `inAbsoluteSampleFrame` and `AUScope &` arguments - Sample frame is needed to allow a note to keep track of its exact place in its playback timeline. The `AUScope` allows different notes to play back via different output busses.
- `NoteOff()` has been made `virtual`.
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-11-29 | New document that describes the changes made to the public utility files that are part of the AUInstrumentBase folder for Mac OS X Lion. |

