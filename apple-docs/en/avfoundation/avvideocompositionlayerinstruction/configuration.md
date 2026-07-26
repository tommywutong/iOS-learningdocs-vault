---
title: AVVideoCompositionLayerInstruction.Configuration
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionlayerinstruction/configuration
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration.json'
content_hash: 'sha256:92b4543ebea559a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../avvideocompositionlayerinstruction.md)

# AVVideoCompositionLayerInstruction.Configuration

<sub>Structure</sub>

Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Configuration
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a configuration

- [init(assetTrack:)](<configuration/init(assettrack_).md>) — Creates a new video composition layer instruction for the given track.
- [init(trackID:)](<configuration/init(trackid_).md>) — Creates a new video composition layer instruction for the given track ID.

### Configuring the crop rectangle

- [setCropRectangle(_:at:)](<configuration/setcroprectangle(__at_).md>) — Sets the crop rectangle value at a time within the time range of the instruction.
- [addCropRectangleRamp(_:)](<configuration/addcroprectangleramp(__).md>) — Sets a crop rectangle ramp to apply during the specified time range.
- [cropRectangleRamp(at:)](<configuration/croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.

### Configuring the opacity

- [setOpacity(_:at:)](<configuration/setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction.
- [addOpacityRamp(_:)](<configuration/addopacityramp(__).md>) — Sets an opacity ramp to apply during a specified time range.
- [opacityRamp(at:)](<configuration/opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.

### Configuring the transform

- [setTransform(_:at:)](<configuration/settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction.
- [addTransformRamp(_:)](<configuration/addtransformramp(__).md>) — Sets a transform ramp to apply during a given time range.
- [transformRamp(at:)](<configuration/transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.

### Inspecting the configuration

- [trackID](configuration/trackid.md) — The track identifier of the source track to which the compositor will apply the instruction.

## See Also

### Creating a layer instruction

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoCompositionLayerInstruction with a configuration.
