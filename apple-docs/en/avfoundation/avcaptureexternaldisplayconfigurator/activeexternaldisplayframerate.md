---
title: activeExternalDisplayFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.json'
content_hash: 'sha256:4beaf59448dbf880'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# activeExternalDisplayFrameRate

<sub>Instance Property</sub>

The currently configured frame rate on the external display that’s displaying the preview layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var activeExternalDisplayFrameRate: Double { get }
```

## Discussion

Observe this property to determine if the configured frame rate matches the max frame rate ([activeVideoMinFrameDuration](../avcapturedevice/activevideominframeduration.md)) of the device. When the [active](isactive.md) property becomes `false`, this property changes to 0.

## See Also

### Inspecting the configurator

- [device](device.md) — The device for which the coordinator configures the preview layer.
- [active](isactive.md) — This property tells you whether the configurator is actively configuring the external display.
- [previewLayer](previewlayer.md) — The layer for which the configurator adjusts display properties to match the device’s state.
