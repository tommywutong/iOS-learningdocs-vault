---
title: AVAssetTrackSegment
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettracksegment
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettracksegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettracksegment.json'
content_hash: 'sha256:df0632d5e2f10a49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetTrackSegment

<sub>Class</sub>

An object that represents a time range segment of an asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetTrackSegment
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCompositionTrackSegment](avcompositiontracksegment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Retrieving segment information

- [timeMapping](avassettracksegment/timemapping.md) — The time range of the track that this segment presents.
- [empty](avassettracksegment/isempty.md) — A Boolean value that indicates whether the segment is empty.

## See Also

### Assets

- [AVAsset](avasset.md) — An object that models timed audiovisual media.
- [AVURLAsset](avurlasset.md) — An asset that represents media at a local or remote URL.
- [AVAssetTrack](avassettrack.md) — An object that models a track of media that an asset contains.
- [AVAssetTrackGroup](avassettrackgroup.md) — A group of related tracks in an asset.
