---
title: 'addCropRectangleRamp(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addcroprectangleramp%28_%3A%29.json'
content_hash: 'sha256:f5a83669fb744e6d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# addCropRectangleRamp(_:)

<sub>Instance Method</sub>

Sets a crop rectangle ramp to apply during the specified time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func addCropRectangleRamp(_ ramp: AVVideoCompositionLayerInstruction.CropRectangleRamp)
```

## See Also

### Configuring the crop rectangle

- [setCropRectangle(_:at:)](<setcroprectangle(__at_).md>) — Sets the crop rectangle value at a time within the time range of the instruction.
- [cropRectangleRamp(at:)](<croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
