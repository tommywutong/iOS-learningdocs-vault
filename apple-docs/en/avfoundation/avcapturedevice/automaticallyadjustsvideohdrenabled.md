---
title: automaticallyAdjustsVideoHDREnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/automaticallyadjustsvideohdrenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsvideohdrenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/automaticallyadjustsvideohdrenabled.json'
content_hash: 'sha256:25be7f36ae47f9d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# automaticallyAdjustsVideoHDREnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device automatically manages the state of high dynamic range (HDR) video streaming.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyAdjustsVideoHDREnabled: Bool { get set }
```

## Discussion

By default, this value is `true`, and a capture device automatically enables [videoHDREnabled](isvideohdrenabled.md) if it’s a good fit for the active format.

This property is key-value observable.

## See Also

### Configuring HDR settings

- [videoHDREnabled](isvideohdrenabled.md) — A Boolean value that indicates whether the device streams high dynamic range video buffers, also known as extended dynamic range (EDR).
