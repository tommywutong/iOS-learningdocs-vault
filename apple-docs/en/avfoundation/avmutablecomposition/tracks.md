---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecomposition/tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/tracks.json'
content_hash: 'sha256:fef05cb19fddf768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# tracks

<sub>Instance Property</sub>

The tracks that a composition contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tracks: [AVMutableCompositionTrack] { get }
```

## Discussion

In a mutable composition, the tracks are instances of [AVMutableCompositionTrack](../avmutablecompositiontrack.md), whereas in [AVComposition](../avcomposition.md) the tracks are instances of [AVCompositionTrack](../avcompositiontrack.md).

## See Also

### Accessing tracks

- [- trackWithTrackID:](<track(withtrackid_).md>) — Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.
