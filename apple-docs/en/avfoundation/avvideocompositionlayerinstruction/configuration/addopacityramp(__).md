---
title: 'addOpacityRamp(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addopacityramp(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addopacityramp(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addopacityramp%28_%3A%29.json'
content_hash: 'sha256:7b2e82a518d47c86'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# addOpacityRamp(_:)

<sub>Instance Method</sub>

Sets an opacity ramp to apply during a specified time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func addOpacityRamp(_ ramp: AVVideoCompositionLayerInstruction.OpacityRamp)
```

## See Also

### Configuring the opacity

- [setOpacity(_:at:)](<setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction.
- [opacityRamp(at:)](<opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
