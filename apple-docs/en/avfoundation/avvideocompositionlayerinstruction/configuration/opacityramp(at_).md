---
title: 'opacityRamp(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/opacityramp(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/opacityramp(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/opacityramp%28at%3A%29.json'
content_hash: 'sha256:c3f0b7349d4882e7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# opacityRamp(at:)

<sub>Instance Method</sub>

Obtains the opacity ramp that includes a specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func opacityRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?
```

## See Also

### Configuring the opacity

- [setOpacity(_:at:)](<setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction.
- [addOpacityRamp(_:)](<addopacityramp(__).md>) — Sets an opacity ramp to apply during a specified time range.
