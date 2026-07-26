---
title: 'setCropRectangle(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setcroprectangle%28_%3Aat%3A%29.json'
content_hash: 'sha256:f51b9fc7069dd8db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# setCropRectangle(_:at:)

<sub>Instance Method</sub>

Sets the crop rectangle value at a time within the time range of the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func setCropRectangle(_ rect: CGRect, at time: CMTime)
```

## See Also

### Configuring the crop rectangle

- [addCropRectangleRamp(_:)](<addcroprectangleramp(__).md>) — Sets a crop rectangle ramp to apply during the specified time range.
- [cropRectangleRamp(at:)](<croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
