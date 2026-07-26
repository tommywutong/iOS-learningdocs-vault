---
title: AVVideoCompositionLayerInstruction
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionlayerinstruction
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction.json'
content_hash: 'sha256:4248da6dda04c6ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionLayerInstruction

<sub>Class</sub>

An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoCompositionLayerInstruction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a layer instruction

- [init(configuration:)](<avvideocompositionlayerinstruction/init(configuration_).md>) — Initialize an AVVideoCompositionLayerInstruction with a configuration.
- [Configuration](avvideocompositionlayerinstruction/configuration.md) — Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.

### Getting the track ID

- [trackID](avvideocompositionlayerinstruction/trackid.md) — The track identifier of the source track to which the compositor will apply the instruction.

### Getting opacity, transform, and cropping ramps

- [cropRectangleRamp(at:)](<avvideocompositionlayerinstruction/croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [CropRectangleRamp](avvideocompositionlayerinstruction/croprectangleramp.md)
- [- getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:](<avvideocompositionlayerinstruction/getcroprectangleramp(for_startcroprectangle_endcroprectangle_timerange_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [opacityRamp(at:)](<avvideocompositionlayerinstruction/opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
- [OpacityRamp](avvideocompositionlayerinstruction/opacityramp.md)
- [- getOpacityRampForTime:startOpacity:endOpacity:timeRange:](<avvideocompositionlayerinstruction/getopacityramp(for_startopacity_endopacity_timerange_).md>) — Obtains the opacity ramp that includes a specified time.
- [transformRamp(at:)](<avvideocompositionlayerinstruction/transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.
- [TransformRamp](avvideocompositionlayerinstruction/transformramp.md)
- [- getTransformRampForTime:startTransform:endTransform:timeRange:](<avvideocompositionlayerinstruction/gettransformramp(for_start_end_timerange_).md>) — Obtains the transform ramp that includes a specified time.

### Initializers

- [init(coder:)](<avvideocompositionlayerinstruction/init(coder_).md>)

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition. _(deprecated)_
