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
doc_path: /documentation/metal/mtlcommandencoder/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencoder/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencoder/device.json'
content_hash: 'sha256:947c296019ca78ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoder](../mtlcommandencoder.md)

# device

<sub>Instance Property</sub>

The Metal device from which the command encoder was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

This command encoder can only be used with this [MTLDevice](../mtldevice.md).

## See Also

### Identifying the command encoder

- [label](label.md) — A string that labels the command encoder.
