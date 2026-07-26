---
title: AVAudioQuality
framework: AVFAudio
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudioquality
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudioquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudioquality.json'
content_hash: 'sha256:e5d602be8b1f576b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioQuality

<sub>Enumeration</sub>

The values that specify the sample rate audio quality for encoding and conversion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVAudioQuality
```

## Overview

You use this value with [AVEncoderAudioQualityKey](avencoderaudioqualitykey.md) and [AVSampleRateConverterAudioQualityKey](avsamplerateconverteraudioqualitykey.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [AVAudioQualityMin](avaudioquality/min.md) — A value that represents a minimum audio quality for encoding and conversion.
- [AVAudioQualityLow](avaudioquality/low.md) — A value that represents a low audio quality for encoding and conversion.
- [AVAudioQualityMedium](avaudioquality/medium.md) — A value that represents a medium audio quality for encoding and conversion.
- [AVAudioQualityHigh](avaudioquality/high.md) — A value that represents a high audio quality for encoding and conversion.
- [AVAudioQualityMax](avaudioquality/max.md) — A value that represents a maximum audio quality for encoding and conversion.

### Initializers

- [init(rawValue:)](<avaudioquality/init(rawvalue_).md>)

## See Also

### Settings

- [Sample Rate Conversion Settings](sample-rate-conversion-settings.md) — The constants that define sample rate converter audio quality settings.
- [AVEncoderAudioQualityKey](avencoderaudioqualitykey.md) — A constant that represents an integer from the audio quality enumeration.
- [Encoder Settings](encoder-settings.md) — The constants that define the audio encoder settings for the audio recorder class.
- [Time pitch algorithm settings](../avfoundation/time-pitch-algorithm-settings.md) — The constants that define the values for the time pitch algorithms.
