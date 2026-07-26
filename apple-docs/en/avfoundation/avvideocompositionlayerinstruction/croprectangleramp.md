---
title: AVVideoCompositionLayerInstruction.CropRectangleRamp
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionlayerinstruction/croprectangleramp
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/croprectangleramp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/croprectangleramp.json'
content_hash: 'sha256:efc0f51a0500eeeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../avvideocompositionlayerinstruction.md)

# AVVideoCompositionLayerInstruction.CropRectangleRamp

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CropRectangleRamp
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a crop rectangle ramp

- [init(timeRange:start:end:)](<croprectangleramp/init(timerange_start_end_).md>)

### Inspecting the crop rectangle ramp

- [end](croprectangleramp/end.md)
- [start](croprectangleramp/start.md)
- [timeRange](croprectangleramp/timerange.md)

## See Also

### Getting opacity, transform, and cropping ramps

- [cropRectangleRamp(at:)](<croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [- getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:](<getcroprectangleramp(for_startcroprectangle_endcroprectangle_timerange_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [opacityRamp(at:)](<opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
- [OpacityRamp](opacityramp.md)
- [- getOpacityRampForTime:startOpacity:endOpacity:timeRange:](<getopacityramp(for_startopacity_endopacity_timerange_).md>) — Obtains the opacity ramp that includes a specified time.
- [transformRamp(at:)](<transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.
- [TransformRamp](transformramp.md)
- [- getTransformRampForTime:startTransform:endTransform:timeRange:](<gettransformramp(for_start_end_timerange_).md>) — Obtains the transform ramp that includes a specified time.
