---
title: sourceTrackIDForFrameTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/sourcetrackidforframetiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/sourcetrackidforframetiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/sourcetrackidforframetiming.json'
content_hash: 'sha256:e90ef5527c18d82e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# sourceTrackIDForFrameTiming

<sub>Instance Property</sub>

An identifier of the source track from which the video composition derives frame timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceTrackIDForFrameTiming: CMPersistentTrackID { get }
```

## Discussion

If an empty edit is encountered in the source asset’s track, the compositor composes frames as needed up to the frequency specified in [frameDuration](frameduration.md) property. Otherwise the frame timing for the video composition is derived from the source asset’s track with the corresponding ID.

## See Also

### Identifying source tracks

- [sourceSampleDataTrackIDs](sourcesampledatatrackids-2hgue.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.
