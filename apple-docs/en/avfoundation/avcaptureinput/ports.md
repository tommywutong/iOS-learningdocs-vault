---
title: ports
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/ports
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/ports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/ports.json'
content_hash: 'sha256:eb653b9d984fbff1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureInput](../avcaptureinput.md)

# ports

<sub>Instance Property</sub>

The ports available on a capture input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var ports: [AVCaptureInput.Port] { get }
```

## Discussion

Individual ports post an [AVCaptureInputPortFormatDescriptionDidChangeNotification](port/formatdescriptiondidchangenotification.md) notification when their [formatDescription](port/formatdescription.md) changes.

## See Also

### Accessing ports

- [Port](port.md) — An object that represents a stream of data that a capture input provides.
