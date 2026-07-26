---
title: previewLayer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/previewlayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/previewlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/previewlayer.json'
content_hash: 'sha256:55203dcf0768d531'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# previewLayer

<sub>Instance Property</sub>

The layer for which the configurator adjusts display properties to match the device’s state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
weak var previewLayer: CALayer? { get }
```

## Discussion

The value of this property is the `CALayer` instance that you provided when instantiating the configurator. You may specify either an [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) or another `CALayer` instance that displays a camera’s video preview. [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)holds a weak reference to the layer. If the layer is released, this property returns `nil`.

## See Also

### Inspecting the configurator

- [activeExternalDisplayFrameRate](activeexternaldisplayframerate.md) — The currently configured frame rate on the external display that’s displaying the preview layer.
- [device](device.md) — The device for which the coordinator configures the preview layer.
- [active](isactive.md) — This property tells you whether the configurator is actively configuring the external display.
