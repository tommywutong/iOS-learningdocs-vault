---
title: requiredSourceSampleDataTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids.json'
content_hash: 'sha256:760556529baa91ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# requiredSourceSampleDataTrackIDs

<sub>Instance Property</sub>

The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredSourceSampleDataTrackIDs: [NSNumber] { get }
```

## See Also

### Identifying source tracks

- [requiredSourceTrackIDs](requiredsourcetrackids.md) — The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [passthroughTrackID](passthroughtrackid.md) — The track identifier from an instruction source frame.
