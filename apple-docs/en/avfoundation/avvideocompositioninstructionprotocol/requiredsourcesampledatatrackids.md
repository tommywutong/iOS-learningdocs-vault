---
title: requiredSourceSampleDataTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids.json'
content_hash: 'sha256:8f579d218b0d8e1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)

# requiredSourceSampleDataTrackIDs

<sub>Instance Property</sub>

The identifiers of the sample data tracks the instruction requires to compose frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional var requiredSourceSampleDataTrackIDs: [NSNumber] { get }
```

## Discussion

An empty array indicates the instruction requires no sample data.

## See Also

### Getting track ID settings

- [passthroughTrackID](passthroughtrackid.md) — An identifier of a source track to pass through without compositing.
- [requiredSourceTrackIDs](requiredsourcetrackids.md) — The identifiers of the video tracks the instruction requires to compose frames.
