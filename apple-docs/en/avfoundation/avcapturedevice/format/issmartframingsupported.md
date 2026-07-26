---
title: isSmartFramingSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/issmartframingsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/issmartframingsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/issmartframingsupported.json'
content_hash: 'sha256:2787e2f41a8ac233'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isSmartFramingSupported

<sub>Instance Property</sub>

Returns `true` if smart framing is supported by the current format.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isSmartFramingSupported: Bool { get }
```

## Discussion

An ultra wide camera device that supports dynamic aspect ratio configuration may also support “smart framing monitoring” on particular formats.
