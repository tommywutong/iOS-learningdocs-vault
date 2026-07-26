---
title: AVMutableVideoCompositionLayerInstruction
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositionlayerinstruction
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction.json'
content_hash: 'sha256:664648330a2e7b75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableVideoCompositionLayerInstruction

<sub>Class</sub>

An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.

> [!warning] Deprecated
> Use [Configuration](avvideocompositionlayerinstruction/configuration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVMutableVideoCompositionLayerInstruction
```

## Relationships

- **Inherits From**: [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an instruction

- [+ videoCompositionLayerInstructionWithAssetTrack:](<avmutablevideocompositionlayerinstruction/init(assettrack_).md>) — Creates a new mutable video composition layer instruction for the given track. _(deprecated)_

### Configuring a track ID

- [trackID](avmutablevideocompositionlayerinstruction/trackid.md) — The track identifier of the source track to which the compositor applies the instruction. _(deprecated)_

### Managing properties

- [- setOpacity:atTime:](<avmutablevideocompositionlayerinstruction/setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction. _(deprecated)_
- [- setOpacityRampFromStartOpacity:toEndOpacity:timeRange:](<avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity_toendopacity_timerange_).md>) — Sets an opacity ramp to apply during a specified time range. _(deprecated)_
- [- setTransform:atTime:](<avmutablevideocompositionlayerinstruction/settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction. _(deprecated)_
- [- setTransformRampFromStartTransform:toEndTransform:timeRange:](<avmutablevideocompositionlayerinstruction/settransformramp(fromstart_toend_timerange_).md>) — Sets a transform ramp to apply during a given time range. _(deprecated)_

### Setting crop rectangle values

- [- setCropRectangle:atTime:](<avmutablevideocompositionlayerinstruction/setcroprectangle(__at_).md>) — Sets the crop rectangle  value at a time within the time range of the instruction. _(deprecated)_
- [- setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:](<avmutablevideocompositionlayerinstruction/setcroprectangleramp(fromstartcroprectangle_toendcroprectangle_timerange_).md>) — Sets a crop rectangle ramp to apply during the specified time range. _(deprecated)_

## See Also

### Built-in video compositing

- [Editing and playing HDR video](editing-and-playing-hdr-video.md) — Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md) — Resolve common problems when creating compositions, video compositions, and audio mixes.
- [AVVideoComposition](avvideocomposition.md) — An object that describes how to compose video frames at particular points in time.
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — An operation that a compositor performs.
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [AVMutableVideoComposition](avmutablevideocomposition.md) — A mutable video composition subclass. _(deprecated)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — A mutable video composition instruction subclass. _(deprecated)_
