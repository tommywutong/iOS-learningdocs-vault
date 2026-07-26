---
title: isSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/issupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/issupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/issupported.json'
content_hash: 'sha256:f90b5bbf1d6b5834'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# isSupported

<sub>Type Property</sub>

Whether Pro Video Storage is supported in its current configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isSupported: Bool { get }
```

## Return Value

`YES` if the device and OS support Pro Video Storage functionality; otherwise, `NO`.

## See Also

### Getting the shared storage

- [sharedStorage](shared.md) — Returns the singleton instance for Pro Video Storage. _(beta)_
