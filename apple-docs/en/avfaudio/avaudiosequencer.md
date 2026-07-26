---
title: AVAudioSequencer
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosequencer
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosequencer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosequencer.json'
content_hash: 'sha256:5d903a5fa878795e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioSequencer

<sub>Class</sub>

An object that plays audio from a collection of MIDI events the system organizes into music tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAudioSequencer
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an Audio Sequencer

- [- init](<avaudiosequencer/init().md>) — Creates an audio sequencer object.
- [- initWithAudioEngine:](<avaudiosequencer/init(audioengine_).md>) — Creates an audio sequencer that the framework attaches to an audio engine instance.

### Writing to a MIDI File

- [- writeToURL:SMPTEResolution:replaceExisting:error:](<avaudiosequencer/write(to_smpteresolution_replaceexisting_).md>) — Creates and writes a MIDI file from the events in the sequence.

### Handling Music Tracks

- [AVMusicTrack](avmusictrack.md) — A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [- createAndAppendTrack](<avaudiosequencer/createandappendtrack().md>) — Creates a new music track and appends it to the sequencer’s list.
- [- reverseEvents](<avaudiosequencer/reverseevents().md>) — Reverses the order of all events in all music tracks, including the tempo track.
- [- removeTrack:](<avaudiosequencer/removetrack(__).md>) — Removes the music track from the sequencer.
- [AVMusicTrackLoopCount](avmusictrackloopcount.md) — Options that define the number of times a track loops.

### Handling Music Events

- [AVMusicEvent](avmusicevent.md) — A base class for the events you associate with a music track.
- [AVMusicUserEvent](avmusicuserevent.md) — An object that represents a custom user message.
- [AVParameterEvent](avparameterevent.md) — An object that represents a parameter event on a music track’s destination.
- [AVAUPresetEvent](avaupresetevent.md) — An object that represents a preset load and change on the music track’s destination audio unit.
- [AVExtendedTempoEvent](avextendedtempoevent.md) — An object that represents a tempo change to a specific beats-per-minute value.
- [AVExtendedNoteOnEvent](avextendednoteonevent.md) — An object that represents a custom extension of a MIDI note on event.

### Handling MIDI Events

- [AVMIDINoteEvent](avmidinoteevent.md) — An object that represents MIDI note on or off messages.
- [AVMIDIMetaEvent](avmidimetaevent.md) — An object that represents MIDI meta event messages.
- [AVMIDISysexEvent](avmidisysexevent.md) — An object that represents a MIDI system exclusive message.

### Handling MIDI Channel Events

- [AVMIDIChannelEvent](avmidichannelevent.md) — A base class for all MIDI messages that operate on a single MIDI channel.
- [AVMIDIChannelPressureEvent](avmidichannelpressureevent.md) — An object that represents a MIDI channel pressure message.
- [AVMIDIProgramChangeEvent](avmidiprogramchangeevent.md) — An object that represents a MIDI program or patch change message.
- [AVMIDIPolyPressureEvent](avmidipolypressureevent.md) — An object that represents a MIDI poly or key pressure event.
- [AVMIDIPitchBendEvent](avmidipitchbendevent.md) — An object that represents a MIDI pitch bend message.
- [AVMIDIControlChangeEvent](avmidicontrolchangeevent.md) — An object that represents a MIDI control change message.

### Managing Sequence Load Options

- [- loadFromData:options:error:](<avaudiosequencer/load(from_options_)-8o58w.md>) — Parses the data and adds its events to the sequence.
- [- loadFromURL:options:error:](<avaudiosequencer/load(from_options_)-9kb6m.md>) — Loads the file the URL references and adds the events to the sequence.
- [AVMusicSequenceLoadOptions](avmusicsequenceloadoptions.md) — A structure that defines whether data on different MIDI channels map to multiple tracks, or whether the framework preserves the tracks as they are.

### Operating an Audio Sequencer

- [- prepareToPlay](<avaudiosequencer/preparetoplay().md>) — Gets ready to play the sequence by prerolling all events.
- [- startAndReturnError:](<avaudiosequencer/start().md>) — Starts the sequencer’s player.
- [- stop](<avaudiosequencer/stop().md>) — Stops the sequencer’s player.

### Managing Time Stamps

- [AVMusicTimeStamp](avmusictimestamp.md) — A fractional number of beats.
- [- hostTimeForBeats:error:](<avaudiosequencer/hosttime(forbeats_error_).md>) — Gets the host time the sequence plays at the specified position.
- [- secondsForBeats:](<avaudiosequencer/seconds(forbeats_).md>) — Gets the time for the specified beat position (timestamp) in the track, in seconds.

### Handling Beat Range

- [- beatsForHostTime:error:](<avaudiosequencer/beats(forhosttime_error_).md>) — Gets the beat the system plays at the specified host time.
- [- beatsForSeconds:](<avaudiosequencer/beats(forseconds_).md>) — Gets the beat position (timestamp) for the specified time in the track.
- [AVMusicTimeStampEndOfTrack](avmusictimestampendoftrack.md) — A timestamp you use to access all events in a music track through a beat range.
- [AVBeatRange](avbeatrange-swift.typealias.md)

### Setting the User Callback

- [- setUserCallback:](<avaudiosequencer/setusercallback(__).md>) — Adds a callback that the sequencer calls each time it encounters a user event during playback.
- [AVAudioSequencerUserCallback](avaudiosequencerusercallback.md) — A callback the sequencer calls asynchronously during playback when it encounters a user event.

### Getting Sequence Properties

- [playing](avaudiosequencer/isplaying.md) — A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [rate](avaudiosequencer/rate.md) — The playback rate of the sequencer’s player.
- [tracks](avaudiosequencer/tracks.md) — An array that contains all the tracks in the sequence.
- [currentPositionInBeats](avaudiosequencer/currentpositioninbeats.md) — The current playback position, in beats.
- [currentPositionInSeconds](avaudiosequencer/currentpositioninseconds.md) — The current playback position, in seconds.
- [tempoTrack](avaudiosequencer/tempotrack.md) — The track that contains tempo information about the sequence.
- [userInfo](avaudiosequencer/userinfo.md) — A dictionary that contains metadata from a sequence.
- [InfoDictionaryKey](avaudiosequencer/infodictionarykey.md) — Constants that defines metadata keys for a sequencer.
- [- dataWithSMPTEResolution:error:](<avaudiosequencer/data(withsmpteresolution_error_).md>) — Gets a data object that contains the events from the sequence.
- [AVMusicTimeStampEndOfTrack](avmusictimestampendoftrack.md) — A timestamp you use to access all events in a music track through a beat range.

## See Also

### MIDI

- [AVAudioUnitSampler](avaudiounitsampler.md) — An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.
- [AVMIDIEventListBlock](avmidieventlistblock.md) _(beta)_
