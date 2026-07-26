---
title: isFlashScene
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isflashscene
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isflashscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isflashscene.json'
content_hash: 'sha256:9bf2b9c2d47a1c54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isFlashScene

<sub>Instance Property</sub>

A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isFlashScene: Bool { get }
```

## Discussion

This property’s value changes depending on the scene currently visible to the camera. For example, you might use this property to highlight the flash control in your app’s camera UI, indicating to the user that the scene is dark enough that enabling the flash might be desirable.

If the photo capture output’s [supportedFlashModes](supportedflashmodes-4u69s.md) value is [AVCaptureFlashModeOff](../avcapturedevice/flashmode-swift.enum/off.md), this property’s value is always [false](../../swift/false.md).

This property supports key-value observing.

## See Also

### Monitoring the visible scene

- [photoSettingsForSceneMonitoring](photosettingsforscenemonitoring.md) — A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.
