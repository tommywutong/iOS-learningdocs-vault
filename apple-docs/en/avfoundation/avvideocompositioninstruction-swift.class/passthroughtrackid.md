---
title: passthroughTrackID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/passthroughtrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/passthroughtrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/passthroughtrackid.json'
content_hash: 'sha256:17d154803855a295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# passthroughTrackID

<sub>Instance Property</sub>

The track identifier from an instruction source frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var passthroughTrackID: CMPersistentTrackID { get }
```

## Discussion

If the video composition result is one of the source frames for the duration of the instruction, this property returns the corresponding track ID. The compositor won’t be run for the duration of the instruction and the proper source frame will be used instead. The value of this property is computed from the layer instructions

## See Also

### Identifying source tracks

- [requiredSourceTrackIDs](requiredsourcetrackids.md) — The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [requiredSourceSampleDataTrackIDs](requiredsourcesampledatatrackids.md) — The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
