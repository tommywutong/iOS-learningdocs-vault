---
title: AVAudioChannelLayout
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiochannellayout
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiochannellayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiochannellayout.json'
content_hash: 'sha256:885a5a1c05c8a1ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioChannelLayout

<sub>Class</sub>

An object that describes the roles of a set of audio channels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioChannelLayout
```

## Overview

The `AVAudioChannelLayout` class is a thin wrapper for Core Audio’s [AudioChannelLayout](../coreaudiotypes/audiochannellayout.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an Audio Channel Layout

- [- initWithLayout:](<avaudiochannellayout/init(layout_).md>) — Creates an audio channel layout object from an existing one.
- [- initWithLayoutTag:](<avaudiochannellayout/init(layouttag_).md>) — Creates an audio channel layout object from a layout tag.

### Getting Audio Channel Layout Properties

- [AVAudioChannelCount](avaudiochannelcount.md) — The number of audio channels.
- [channelCount](avaudiochannellayout/channelcount.md) — The number of channels of audio data.
- [layout](avaudiochannellayout/layout.md) — The underlying audio channel layout.
- [layoutTag](avaudiochannellayout/layouttag.md) — The audio channel’s underlying layout tag.
- [- isEqual:](<avaudiochannellayout/isequal(__).md>) — Indicates whether another audio channel layout is exactly equal to the current layout.

### Initializers

- [init(coder:)](<avaudiochannellayout/init(coder_).md>)

## See Also

### Formats

- [AVAudioFormat](avaudioformat.md) — An object that describes the representation of an audio format.
- [AVChannelLayoutKey](avchannellayoutkey.md)
- [Linear PCM Format Settings](linear-pcm-format-settings.md) — The audio settings that apply to linear PCM audio formats.
- [Format Settings](format-settings.md) — The audio settings that apply to all audio formats that the audio player and recorder classes support.
