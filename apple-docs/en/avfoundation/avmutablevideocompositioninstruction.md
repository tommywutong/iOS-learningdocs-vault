---
title: AVMutableVideoCompositionInstruction
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositioninstruction
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositioninstruction.json'
content_hash: 'sha256:92b2eb77db3c1bf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableVideoCompositionInstruction

<sub>Class</sub>

A mutable video composition instruction subclass.

> [!warning] Deprecated
> Use [Configuration](avvideocompositioninstruction-swift.class/configuration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVMutableVideoCompositionInstruction
```

## Overview

An [AVVideoComposition](avvideocomposition.md) object maintains an array of [instructions](avvideocomposition/instructions.md) to perform its composition.

## Relationships

- **Inherits From**: [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)

- **Conforms To**: [AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the instructions

- [backgroundColor](avmutablevideocompositioninstruction/backgroundcolor.md) — The background color of the composition. _(deprecated)_
- [layerInstructions](avmutablevideocompositioninstruction/layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks. _(deprecated)_
- [timeRange](avmutablevideocompositioninstruction/timerange.md) — The time range to which the instruction applies. _(deprecated)_
- [enablePostProcessing](avmutablevideocompositioninstruction/enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing. _(deprecated)_

### Configuring source tracks

- [requiredSourceSampleDataTrackIDs](avmutablevideocompositioninstruction/requiredsourcesampledatatrackids.md) — The track identifiers of source sample data that the compositor requires to compose frames for the instruction. _(deprecated)_

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_
