---
title: 'transformRamp(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/transformramp(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/transformramp(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/transformramp%28at%3A%29.json'
content_hash: 'sha256:5d3c9a5004393e64'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# transformRamp(at:)

<sub>Instance Method</sub>

Obtains the transform ramp that includes a specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func transformRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?
```

## See Also

### Configuring the transform

- [setTransform(_:at:)](<settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction.
- [addTransformRamp(_:)](<addtransformramp(__).md>) — Sets a transform ramp to apply during a given time range.
