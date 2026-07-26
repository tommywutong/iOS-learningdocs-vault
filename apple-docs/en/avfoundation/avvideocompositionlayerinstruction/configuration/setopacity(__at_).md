---
title: 'setOpacity(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setopacity(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setopacity(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setopacity%28_%3Aat%3A%29.json'
content_hash: 'sha256:4089bcff76ded0f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../../avvideocompositionlayerinstruction.md) · [Configuration](../configuration.md)

# setOpacity(_:at:)

<sub>Instance Method</sub>

Sets the opacity value at a specific time within the time range of the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func setOpacity(_ opacity: Float, at time: CMTime)
```

## See Also

### Configuring the opacity

- [addOpacityRamp(_:)](<addopacityramp(__).md>) — Sets an opacity ramp to apply during a specified time range.
- [opacityRamp(at:)](<opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
