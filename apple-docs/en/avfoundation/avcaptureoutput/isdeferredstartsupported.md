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
doc_path: /documentation/avfoundation/avcaptureoutput/isdeferredstartsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/isdeferredstartsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/isdeferredstartsupported.json'
content_hash: 'sha256:9af1c872dde2e546'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# isDeferredStartSupported

<sub>Instance Property</sub>

A `BOOL` value that indicates whether the output supports deferred start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isDeferredStartSupported: Bool { get }
```

## Discussion

You can only set the [deferredStartEnabled](isdeferredstartenabled.md) property value to `true` if the output supports deferred start.

## See Also

### Managing deferred start

- [deferredStartEnabled](isdeferredstartenabled.md) — A Boolean value that indicates whether to defer starting this capture output.
