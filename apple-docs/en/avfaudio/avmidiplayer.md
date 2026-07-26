---
title: AVMIDIPlayer
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avmidiplayer
source_url: 'https://developer.apple.com/documentation/avfaudio/avmidiplayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avmidiplayer.json'
content_hash: 'sha256:47d9c385d5aa6083'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVMIDIPlayer

<sub>Class</sub>

An object that plays MIDI data through a system sound module.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVMIDIPlayer
```

## Overview

For more information about preparing your app to play audio, see [Configuring your app for media playback](../avfoundation/configuring-your-app-for-media-playback.md).

> [!important] Important
> For more advanced MIDI playback capabilities, like playing MIDI data through an external synthesizer or sampler, use [AVAudioEngine](avaudioengine.md) instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a MIDI player

- [- initWithContentsOfURL:soundBankURL:error:](<avmidiplayer/init(contentsof_soundbankurl_).md>) — Creates a player to play a MIDI file with the specified soundbank.
- [- initWithData:soundBankURL:error:](<avmidiplayer/init(data_soundbankurl_).md>) — Creates a player to play MIDI data with the specified soundbank.

### Controlling playback

- [- prepareToPlay](<avmidiplayer/preparetoplay().md>) — Prepares the player to play the sequence by prerolling all events.
- [- play:](<avmidiplayer/play(__).md>) — Plays the MIDI sequence.
- [AVMIDIPlayerCompletionHandler](avmidiplayercompletionhandler.md) — A callback the system invokes when MIDI playback completes.
- [- stop](<avmidiplayer/stop().md>) — Stops playing the sequence.
- [playing](avmidiplayer/isplaying.md) — A Boolean value that indicates whether the sequence is playing.

### Configuring playback settings

- [rate](avmidiplayer/rate.md) — The playback rate of the player.

### Accessing player timing

- [currentPosition](avmidiplayer/currentposition.md) — The current playback position, in seconds.
- [duration](avmidiplayer/duration.md) — The duration, in seconds, of the currently loaded file.

### Initializers

- [init(contentsOfURL:soundBankURL:)](<avmidiplayer/init(contentsofurl_soundbankurl_).md>)

## See Also

### Basic playback and recording

- [AVAudioPlayer](avaudioplayer.md) — An object that plays audio data from a file or buffer.
- [AVAudioRecorder](avaudiorecorder.md) — An object that records audio data to a file.
