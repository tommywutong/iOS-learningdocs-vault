---
title: shared()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturemanager/shared()
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/shared()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/shared%28%29.json'
content_hash: 'sha256:12691f123bbd524c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# shared()

<sub>Type Method</sub>

Provides the shared capture manager for your Metal app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func shared() -> MTLCaptureManager
```

## Discussion

There is only one capture manager per process.
