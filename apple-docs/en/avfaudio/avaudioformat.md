---
title: AVAudioFormat
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudioformat
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudioformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudioformat.json'
content_hash: 'sha256:b3f33cfa636c50c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioFormat

<sub>Class</sub>

An object that describes the representation of an audio format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioFormat
```

## Overview

The [AVAudioFormat](avaudioformat.md) class wraps Core Audio’s [AudioStreamBasicDescription](../coreaudiotypes/audiostreambasicdescription.md), and includes convenience initializers and accessors for common formats, including Core Audio’s standard deinterleaved 32-bit floating point format.

Instances of this class are immutable.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a New Audio Format Representation

- [- initStandardFormatWithSampleRate:channelLayout:](<avaudioformat/init(standardformatwithsamplerate_channellayout_).md>) — Creates an audio format instance as a deinterleaved float with the specified sample rate and channel layout.
- [- initStandardFormatWithSampleRate:channels:](<avaudioformat/init(standardformatwithsamplerate_channels_).md>) — Creates an audio format instance with the specified sample rate and channel count.
- [- initWithCommonFormat:sampleRate:channels:interleaved:](<avaudioformat/init(commonformat_samplerate_channels_interleaved_).md>) — Creates an audio format instance.
- [- initWithCommonFormat:sampleRate:interleaved:channelLayout:](<avaudioformat/init(commonformat_samplerate_interleaved_channellayout_).md>) — Creates an audio format instance with the specified audio format, sample rate, interleaved state, and channel layout.
- [- initWithSettings:](<avaudioformat/init(settings_).md>) — Creates an audio format instance using the specified settings dictionary.
- [- initWithStreamDescription:](<avaudioformat/init(streamdescription_).md>) — Creates an audio format instance from a stream description.
- [- initWithStreamDescription:channelLayout:](<avaudioformat/init(streamdescription_channellayout_).md>) — Creates an audio format instance from a stream description and channel layout.
- [- initWithFormatDescription:](<avaudioformat/init(formatdescription_).md>) _(beta)_
- [- initWithCMAudioFormatDescription:](<avaudioformat/init(cmaudioformatdescription_)-8rdfj.md>) — Creates an audio format instance from a Core Media audio format description. _(deprecated)_

### Getting the Audio Stream Description

- [streamDescription](avaudioformat/streamdescription.md) — The audio format properties of a stream of audio data.

### Comparing Instances

- [- isEqual:](<avaudioformat/isequal(__).md>) — Indicates whether the audio format instance and a specified object are functionally equivalent.

### Getting Audio Format Values

- [sampleRate](avaudioformat/samplerate.md) — The audio format sampling rate, in hertz.
- [channelCount](avaudioformat/channelcount.md) — The number of channels of audio data.
- [channelLayout](avaudioformat/channellayout.md) — The underlying audio channel layout.
- [formatDescription](avaudioformat/formatdescription.md) — The audio format description to use with Core Media APIs.

### Determining the Audio Format

- [interleaved](avaudioformat/isinterleaved.md) — A Boolean value that indicates whether the samples mix into one stream.
- [standard](avaudioformat/isstandard.md) — A Boolean value that indicates whether the format is in a deinterleaved native-endian float state.
- [commonFormat](avaudioformat/commonformat.md) — The common format identifier instance.
- [settings](avaudioformat/settings.md) — A dictionary that represents the format as a dictionary using audio setting keys.
- [magicCookie](avaudioformat/magiccookie.md) — An object that contains metadata that encoders and decoders require.

### Constants

- [AVAudioCommonFormat](avaudiocommonformat.md) — The format options that describe common audio formats.

### Initializers

- [init(CMAudioFormatDescription:)](<avaudioformat/init(cmaudioformatdescription_)-2tldd.md>) _(deprecated)_
- [init(coder:)](<avaudioformat/init(coder_).md>)

## See Also

### Formats

- [AVAudioChannelLayout](avaudiochannellayout.md) — An object that describes the roles of a set of audio channels.
- [AVChannelLayoutKey](avchannellayoutkey.md)
- [Linear PCM Format Settings](linear-pcm-format-settings.md) — The audio settings that apply to linear PCM audio formats.
- [Format Settings](format-settings.md) — The audio settings that apply to all audio formats that the audio player and recorder classes support.
