---
title: AVVideoCompositionInstructionProtocol
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol.json'
content_hash: 'sha256:fd7209e31ef0b677'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionInstructionProtocol

<sub>Protocol</sub>

A protocol that defines the interface for a video composition instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVVideoCompositionInstructionProtocol : NSObjectProtocol, Sendable
```

## Overview

A video composition maintains an array of instructions that describe how to compose its content.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md), [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)

## Topics

### Getting track ID settings

- [passthroughTrackID](avvideocompositioninstructionprotocol/passthroughtrackid.md) — An identifier of a source track to pass through without compositing.
- [requiredSourceTrackIDs](avvideocompositioninstructionprotocol/requiredsourcetrackids.md) — The identifiers of the video tracks the instruction requires to compose frames.
- [requiredSourceSampleDataTrackIDs](avvideocompositioninstructionprotocol/requiredsourcesampledatatrackids.md) — The identifiers of the sample data tracks the instruction requires to compose frames.

### Getting tweening settings

- [containsTweening](avvideocompositioninstructionprotocol/containstweening.md) — A Boolean value that indicates whether the composition contains tweening.

### Getting post-processing status

- [enablePostProcessing](avvideocompositioninstructionprotocol/enablepostprocessing.md) — A Boolean value that indicates whether the composition enables post-processing.

### Getting timing settings

- [timeRange](avvideocompositioninstructionprotocol/timerange.md) — The time range during which the instruction is effective.

## See Also

### Specifying composition instructions

- [instructions](avmutablevideocomposition/instructions.md) — The video composition instructions. _(deprecated)_
