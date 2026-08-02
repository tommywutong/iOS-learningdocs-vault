---
title: Music Player Sequence Destinations
apple_id: DTS10003181
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2011-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1330/_index.html
archived_at: '2026-07-18T02:30:25.117322Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1330

# Music Player Sequence Destinations

## Q:  Sending MIDI events seems to have no effect. Have I set my MIDI destinations correctly?

A: A music player is associated with a music sequence in a one-to-one relationship. A music sequence is designed to hold various music tracks which are intended to be logical groupings of events.

The `MusicPlayerSetSequence` method will associate a sequence and its tracks with a music player. A MusicSequence may have an associated AUGraph object which represents a set of AudioUnits and the connections between them. Therefore, each MusicTrack of the MusicSequence may address its events to a specific AudioUnit within the AUGraph.

`MusicPlayerSetSequence` will automatically associate a MusicSequence to a MusicPlayer in the sequences' default configuration; this includes setting the sequences' tracks to their default destinations.

The methods `MusicSequenceSetMIDIEndpoint` or `MusicSequenceSetAUGraph` can assign an entire sequence to a specific endpoint or an AUGraph. However, if a client would like to have custom connections of the tracks of a sequence to particular AudioUnits within an AUGraph, a call to `MusicTrackSetDestNode` must be made after `MusicPlayerSetSequence` is used. This is the same when connecting individual tracks to MIDIEndpoints; `MusicTrackSetDestMIDIEndpoint` must be called only after `MusicPlayerSetSequence`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-22 | Editorial |
| 2004-01-15 | New document that provides clarification on MIDI Endpoints and assigning MIDI data flow. |

