---
title: sourceTrackIDForFrameTiming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（26.0 起废弃）, iPadOS 11.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.13+（26.0 起废弃）, tvOS 11.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition/sourcetrackidforframetiming
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/sourcetrackidforframetiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/sourcetrackidforframetiming.json'
content_hash: 'sha256:cef74338d72c0147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# sourceTrackIDForFrameTiming

<sub>Instance Property</sub>

An identifier of the source track from which the video composition derives frame timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceTrackIDForFrameTiming: CMPersistentTrackID { get set }
```

## Discussion

If an empty edit is encountered in the source asset’s track, the compositor composes frames as needed up to the frequency specified in [frameDuration](../avvideocomposition/frameduration.md) property. Otherwise the frame timing for the video composition is derived from the source asset’s track with the corresponding ID.

## See Also

### Identifying source tracks

- [sourceSampleDataTrackIDs](sourcesampledatatrackids-7i02t.md) — The identifiers of source sample data tracks in the composition that the object requires to compose frames.
