---
title: isDeferredStartSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/isdeferredstartsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/isdeferredstartsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/isdeferredstartsupported.json'
content_hash: 'sha256:8590c5b51452d006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# isDeferredStartSupported

<sub>Instance Property</sub>

A `BOOL` value that indicates whether the preview layer supports deferred start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isDeferredStartSupported: Bool { get }
```

## Discussion

You can only set the [deferredStartEnabled](isdeferredstartenabled.md) property to `true` if the preview layer supports deferred start.

## See Also

### Configuring deferred start

- [deferredStartEnabled](isdeferredstartenabled.md) — A `BOOL` value that indicates whether to defer starting this preview layer.
