---
title: requiredSourceTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcetrackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcetrackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcetrackids.json'
content_hash: 'sha256:428146ab4984a8cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# requiredSourceTrackIDs

<sub>Instance Property</sub>

The identifiers of source video tracks that the compositor requires to compose frames for the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredSourceTrackIDs: [NSValue] { get }
```

## See Also

### Identifying source tracks

- [requiredSourceSampleDataTrackIDs](requiredsourcesampledatatrackids.md) — The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [passthroughTrackID](passthroughtrackid.md) — The track identifier from an instruction source frame.
