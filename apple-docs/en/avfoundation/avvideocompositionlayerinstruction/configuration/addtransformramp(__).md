---
title: 'addTransformRamp(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addtransformramp(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addtransformramp(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addtransformramp%28_%3A%29.json'
content_hash: 'sha256:c49769a59be77dce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# addTransformRamp(_:)

<sub>Instance Method</sub>

Sets a transform ramp to apply during a given time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func addTransformRamp(_ ramp: AVVideoCompositionLayerInstruction.TransformRamp)
```

## See Also

### Configuring the transform

- [setTransform(_:at:)](<settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction.
- [transformRamp(at:)](<transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.
