---
title: AVAudioRecorder
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiorecorder
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiorecorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiorecorder.json'
content_hash: 'sha256:415d86b750812105'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioRecorder

<sub>Class</sub>

An object that records audio data to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioRecorder
```

## Overview

Use an audio recorder to:

- Record audio from the system’s active input device
- Record for a specified duration or until the user stops recording
- Pause and resume a recording
- Access recording-level metering data

To record audio in iOS or tvOS, configure your audio session to use the [AVAudioSessionCategoryRecord](avaudiosession/category-swift.struct/record.md) or [AVAudioSessionCategoryPlayAndRecord](avaudiosession/category-swift.struct/playandrecord.md) category.

> [!important] Important
> For more advanced recording capabilities, like applying signal processing to recorded audio, use [AVAudioEngine](avaudioengine.md) instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an audio recorder

- [- initWithURL:settings:error:](<avaudiorecorder/init(url_settings_)-5whyq.md>) — Creates an audio recorder with settings.
- [- initWithURL:format:error:](<avaudiorecorder/init(url_format_)-7herw.md>) — Creates an audio recorder with an audio format.

### Controlling recording

- [- prepareToRecord](<avaudiorecorder/preparetorecord().md>) — Creates an audio file and prepares the system for recording.
- [- record](<avaudiorecorder/record().md>) — Starts or resumes audio recording.
- [- recordAtTime:](<avaudiorecorder/record(attime_).md>) — Records audio starting at a specific time.
- [- recordForDuration:](<avaudiorecorder/record(forduration_).md>) — Records audio for the indicated duration of time.
- [- recordAtTime:forDuration:](<avaudiorecorder/record(attime_forduration_).md>) — Records audio starting at a specific time for the indicated duration.
- [- pause](<avaudiorecorder/pause().md>) — Pauses an audio recording.
- [- stop](<avaudiorecorder/stop().md>) — Stops recording and closes the audio file.
- [recording](avaudiorecorder/isrecording.md) — A Boolean value that indicates whether the audio recorder is recording.
- [- deleteRecording](<avaudiorecorder/deleterecording().md>) — Deletes a recorded audio file.

### Accessing recorder timing

- [currentTime](avaudiorecorder/currenttime.md) — The time, in seconds, since the beginning of the recording.
- [deviceCurrentTime](avaudiorecorder/devicecurrenttime.md) — The time, in seconds, of the host audio device.

### Managing audio channels

- [channelAssignments](avaudiorecorder/channelassignments.md) — An array of channel descriptions associated with the audio recorder.

### Managing audio-level metering

- [meteringEnabled](avaudiorecorder/ismeteringenabled.md) — A Boolean value that indicates whether you’ve enabled the recorder to generate audio-level metering data.
- [- updateMeters](<avaudiorecorder/updatemeters().md>) — Refreshes the average and peak power values for all channels of an audio recorder.
- [- averagePowerForChannel:](<avaudiorecorder/averagepower(forchannel_).md>) — Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [- peakPowerForChannel:](<avaudiorecorder/peakpower(forchannel_).md>) — Returns the peak power, in decibels full-scale (dBFS), for an audio channel.

### Responding to recorder events

- [delegate](avaudiorecorder/delegate.md) — The delegate object for the audio recorder.
- [AVAudioRecorderDelegate](avaudiorecorderdelegate.md) — A protocol that defines the methods to respond to audio recording events and encoding errors.

### Inspecting the audio data

- [url](avaudiorecorder/url.md) — The URL to which the recorder writes its data.
- [format](avaudiorecorder/format.md) — The format of the recorded audio.
- [settings](avaudiorecorder/settings.md) — The settings that describe the format of the recorded audio.

### Initializers

- [init(URL:format:)](<avaudiorecorder/init(url_format_)-hpsc.md>)
- [init(URL:settings:)](<avaudiorecorder/init(url_settings_)-9zay9.md>)

## See Also

### Basic playback and recording

- [AVAudioPlayer](avaudioplayer.md) — An object that plays audio data from a file or buffer.
- [AVMIDIPlayer](avmidiplayer.md) — An object that plays MIDI data through a system sound module.
