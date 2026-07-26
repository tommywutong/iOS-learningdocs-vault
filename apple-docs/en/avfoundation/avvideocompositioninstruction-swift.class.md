---
title: AVVideoCompositionInstruction
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class.json'
content_hash: 'sha256:efb0f8069258c32b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionInstruction

<sub>Class</sub>

An operation that a compositor performs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoCompositionInstruction
```

## Overview

An [AVVideoComposition](avvideocomposition.md) object maintains an array of [instructions](avvideocomposition/instructions.md) to perform its composition.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)

- **Conforms To**: [AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an instruction

- [init(configuration:)](<avvideocompositioninstruction-swift.class/init(configuration_).md>) — Initialize an AVVideoCompositionInstruction with a configuration.
- [Configuration](avvideocompositioninstruction-swift.class/configuration.md) — Configurable properties for initializing a new AVVideoCompositionInstruction instance.

### Inspecting the instruction

- [backgroundColor](avvideocompositioninstruction-swift.class/backgroundcolor.md) — The background color of the composition.
- [layerInstructions](avvideocompositioninstruction-swift.class/layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [timeRange](avvideocompositioninstruction-swift.class/timerange.md) — The time range to which the instruction applies.
- [enablePostProcessing](avvideocompositioninstruction-swift.class/enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing.

### Identifying source tracks

- [requiredSourceTrackIDs](avvideocompositioninstruction-swift.class/requiredsourcetrackids.md) — The identifiers of source video tracks that the compositor requires to compose frames for the instruction.
- [requiredSourceSampleDataTrackIDs](avvideocompositioninstruction-swift.class/requiredsourcesampledatatrackids.md) — The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [passthroughTrackID](avvideocompositioninstruction-swift.class/passthroughtrackid.md) — The track identifier from an instruction source frame.

### Initializers

- [init(coder:)](<avvideocompositioninstruction-swift.class/init(coder_).md>)

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_
