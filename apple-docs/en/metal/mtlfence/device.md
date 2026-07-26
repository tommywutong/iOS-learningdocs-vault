---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfence/device
source_url: 'https://developer.apple.com/documentation/metal/mtlfence/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfence/device.json'
content_hash: 'sha256:7e602c51d4623797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFence](../mtlfence.md)

# device

<sub>Instance Property</sub>

The device object that created the fence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

Only the device that created the fence can use it.

## See Also

### Identifying a fence

- [label](label.md) — A string that identifies the fence.
