---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibrary/device
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibrary/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibrary/device.json'
content_hash: 'sha256:59dd8bcd6d6b31a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDynamicLibrary](../mtldynamiclibrary.md)

# device

<sub>Instance Property</sub>

The Metal device object that created the dynamic library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## See Also

### Identifying the library

- [installName](installname.md) — A file path for this dynamic library.
- [label](label.md) — A string that identifies the library.
