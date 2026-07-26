---
title: isDecodable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/isdecodable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/isdecodable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/isdecodable.json'
content_hash: 'sha256:5e1cda79f696dc93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# isDecodable

<sub>Instance Property</sub>

A Boolean value that indicates whether the track is decodable in the current environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDecodable: Bool { get }
```

## Discussion

When this property is [true](../../swift/true.md), the system can decode the track, even if decoding may be too slow for real-time playback.

## See Also

### Accessing track information

- [isPlayable](isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isEnabled](isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
