---
title: requiredSourceTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcetrackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcetrackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcetrackids.json'
content_hash: 'sha256:1653d9d42a0adf9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)

# requiredSourceTrackIDs

<sub>Instance Property</sub>

The identifiers of the video tracks the instruction requires to compose frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredSourceTrackIDs: [NSValue]? { get }
```

## Discussion

If the value of this property is `nil`, the instruction requires all source tracks for composition.

## See Also

### Getting track ID settings

- [passthroughTrackID](passthroughtrackid.md) — An identifier of a source track to pass through without compositing.
- [requiredSourceSampleDataTrackIDs](requiredsourcesampledatatrackids.md) — The identifiers of the sample data tracks the instruction requires to compose frames.
