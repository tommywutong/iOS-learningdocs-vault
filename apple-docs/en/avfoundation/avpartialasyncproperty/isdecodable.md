---
title: isDecodable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/isdecodable
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/isdecodable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/isdecodable.json'
content_hash: 'sha256:64d0572267e4e7cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# isDecodable

<sub>Type Property</sub>

A Boolean value that indicates whether the track is decodable in the current environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var isDecodable: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

When this property is [true](../../swift/true.md), the system can decode the track, even if decoding may be too slow for real-time playback.

## See Also

### Loading track information

- [formatDescriptions](formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [isPlayable](isplayable-6txa5.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isEnabled](isenabled.md) — A Boolean value that indicates whether the track is in an enabled state.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether the track references sample data only within its container file.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [mediaCharacteristics](mediacharacteristics.md) — The media characteristics for the track.
