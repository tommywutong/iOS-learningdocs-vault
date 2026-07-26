---
title: shared
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/shared
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/shared.json'
content_hash: 'sha256:5550c24ea58dbde1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# shared

<sub>Type Property</sub>

Returns the singleton instance for Pro Video Storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var shared: AVProVideoStorage? { get }
```

## Return Value

An instance of the Pro Video Storage class if supported; otherwise, `nil`.

## See Also

### Getting the shared storage

- [supported](issupported.md) — Whether Pro Video Storage is supported in its current configuration. _(beta)_
