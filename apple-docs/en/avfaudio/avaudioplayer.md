---
title: AVAudioPlayer
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.2+, iPadOS 2.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudioplayer
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudioplayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudioplayer.json'
content_hash: 'sha256:85b46342b078b201'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioPlayer

<sub>Class</sub>

An object that plays audio data from a file or buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioPlayer
```

## Overview

Use an audio player to:

- Play audio of any duration from a file or buffer
- Control the volume, panning, rate, and looping behavior of the played audio
- Access playback-level metering data
- Play multiple sounds simultaneously by synchronizing the playback of multiple players

For more information about preparing your app to play audio, see [Configuring your app for media playback](../avfoundation/configuring-your-app-for-media-playback.md).

> [!important] Important
> For more advanced playback capabilities, like playing streaming or positional audio, use [AVAudioEngine](avaudioengine.md) instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an audio player

- [- initWithContentsOfURL:error:](<avaudioplayer/init(contentsof_).md>) — Creates a player to play audio from a file.
- [- initWithContentsOfURL:fileTypeHint:error:](<avaudioplayer/init(contentsof_filetypehint_).md>) — Creates a player to play audio from a file of a particular type.
- [- initWithData:error:](<avaudioplayer/init(data_).md>) — Creates a player to play in-memory audio data.
- [- initWithData:fileTypeHint:error:](<avaudioplayer/init(data_filetypehint_).md>) — Creates a player to play in-memory audio data of a particular type.

### Controlling playback

- [- prepareToPlay](<avaudioplayer/preparetoplay().md>) — Prepares the player for audio playback.
- [- play](<avaudioplayer/play().md>) — Plays audio asynchronously.
- [- playAtTime:](<avaudioplayer/play(attime_).md>) — Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [- pause](<avaudioplayer/pause().md>) — Pauses audio playback.
- [- stop](<avaudioplayer/stop().md>) — Stops playback and undoes the setup the system requires for playback.
- [playing](avaudioplayer/isplaying.md) — A Boolean value that indicates whether the player is currently playing audio.

### Configuring playback settings

- [volume](avaudioplayer/volume.md) — The audio player’s volume relative to other audio output.
- [- setVolume:fadeDuration:](<avaudioplayer/setvolume(__fadeduration_).md>) — Changes the audio player’s volume over a duration of time.
- [pan](avaudioplayer/pan.md) — The audio player’s stereo pan position.
- [enableRate](avaudioplayer/enablerate.md) — A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [rate](avaudioplayer/rate.md) — The audio player’s playback rate.
- [numberOfLoops](avaudioplayer/numberofloops.md) — The number of times the audio repeats playback.

### Accessing player timing

- [currentTime](avaudioplayer/currenttime.md) — The current playback time, in seconds, within the audio timeline.
- [duration](avaudioplayer/duration.md) — The total duration, in seconds, of the player’s audio.

### Configuring the Spatial Audio experience

- [intendedSpatialExperience](avaudioplayer/intendedspatialexperience-27klj.md) — The intended spatial experience for this player.

### Managing audio channels

- [numberOfChannels](avaudioplayer/numberofchannels.md) — The number of audio channels in the player’s audio.
- [channelAssignments](avaudioplayer/channelassignments.md) — An array of channel descriptions for the audio player.

### Managing audio-level metering

- [meteringEnabled](avaudioplayer/ismeteringenabled.md) — A Boolean value that indicates whether the player is able to generate audio-level metering data.
- [- updateMeters](<avaudioplayer/updatemeters().md>) — Refreshes the average and peak power values for all channels of an audio player.
- [- averagePowerForChannel:](<avaudioplayer/averagepower(forchannel_).md>) — Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [- peakPowerForChannel:](<avaudioplayer/peakpower(forchannel_).md>) — Returns the peak power, in decibels full-scale (dBFS), for an audio channel.

### Responding to player events

- [delegate](avaudioplayer/delegate.md) — The delegate object for the audio player.
- [AVAudioPlayerDelegate](avaudioplayerdelegate.md) — A protocol that defines the methods to respond to audio playback events and decoding errors.

### Inspecting the audio data

- [url](avaudioplayer/url.md) — The URL of the audio file.
- [data](avaudioplayer/data.md) — The audio data associated with the player.
- [format](avaudioplayer/format.md) — The format of the player’s audio data.
- [settings](avaudioplayer/settings.md) — A dictionary that provides information about the player’s audio data.

### Accessing device information

- [currentDevice](avaudioplayer/currentdevice.md) — The unique identifier of the current audio player.
- [deviceCurrentTime](avaudioplayer/devicecurrenttime.md) — The time value, in seconds, of the audio output device’s clock.

### Initializers

- [init(contentsOfURL:)](<avaudioplayer/init(contentsofurl_).md>)
- [init(contentsOfURL:fileTypeHint:)](<avaudioplayer/init(contentsofurl_filetypehint_).md>)

## See Also

### Basic playback and recording

- [AVAudioRecorder](avaudiorecorder.md) — An object that records audio data to a file.
- [AVMIDIPlayer](avmidiplayer.md) — An object that plays MIDI data through a system sound module.
