---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibrary/device
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/device.json'
content_hash: 'sha256:d5b46856878a4790'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# device

<sub>Instance Property</sub>

The Metal device object that created the library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can only use the library with this [MTLDevice](../mtldevice.md).

## See Also

### Identifying the library

- [label](label.md) — A string that identifies the library.
