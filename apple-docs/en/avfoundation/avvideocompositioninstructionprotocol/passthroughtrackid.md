---
title: passthroughTrackID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol/passthroughtrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/passthroughtrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol/passthroughtrackid.json'
content_hash: 'sha256:226f3e7843d2af02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)

# passthroughTrackID

<sub>Instance Property</sub>

An identifier of a source track to pass through without compositing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var passthroughTrackID: CMPersistentTrackID { get }
```

## Discussion

If an instruction indicates to pass through a source frame without compositing, this property returns the corresponding track identifier. The compositor isn’t run for the duration of the instruction, and instead passes the source frame through to the output. The system automatically matches the required dimensions, clean aperture, and pixel aspect ratio values of the source buffer.

## See Also

### Getting track ID settings

- [requiredSourceTrackIDs](requiredsourcetrackids.md) — The identifiers of the video tracks the instruction requires to compose frames.
- [requiredSourceSampleDataTrackIDs](requiredsourcesampledatatrackids.md) — The identifiers of the sample data tracks the instruction requires to compose frames.
