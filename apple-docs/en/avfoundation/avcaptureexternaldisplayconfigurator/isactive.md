---
title: isActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/isactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/isactive.json'
content_hash: 'sha256:dc81246b04a96bcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# isActive

<sub>Instance Property</sub>

This property tells you whether the configurator is actively configuring the external display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isActive: Bool { get }
```

## Discussion

When this property returns `true`, the external display is successfully configured to match the device. If it returns`false`, the configurator is not making any configuration changes to the external display. If another [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md) instance takes over the configuration of the external display, this property returns `false`.

## See Also

### Inspecting the configurator

- [activeExternalDisplayFrameRate](activeexternaldisplayframerate.md) — The currently configured frame rate on the external display that’s displaying the preview layer.
- [device](device.md) — The device for which the coordinator configures the preview layer.
- [previewLayer](previewlayer.md) — The layer for which the configurator adjusts display properties to match the device’s state.
