---
title: formats
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/formats
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/formats.json'
content_hash: 'sha256:6ba8e384bcbe6ec6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# formats

<sub>Instance Property</sub>

The capture formats a device supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var formats: [AVCaptureDevice.Format] { get }
```

## Discussion

A capture device format describes the details of the video, image, or audio parameters of a specific mode of capture. If you require specifying capture settings not covered by a capture session preset, you can set the [activeFormat](activeformat.md) property to any of the formats in this array.

This property value is key-value observable.

## See Also

### Configuring capture formats

- [activeFormat](activeformat.md) — The capture format in use by the device.
- [activeDepthDataFormat](activedepthdataformat.md) — The currently active depth data format of the capture device.
- [Format](format.md) — A class that defines media formats and capture settings that capture devices support.
