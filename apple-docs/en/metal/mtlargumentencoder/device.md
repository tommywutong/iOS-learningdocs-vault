---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentencoder/device
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/device.json'
content_hash: 'sha256:c48120951d7adef5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# device

<sub>Instance Property</sub>

The device object that created the argument encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can only use the encoder to encode data into buffers created by the same Metal device object.

## See Also

### Identifying the argument encoder

- [label](label.md) — A string that identifies the argument buffer.
