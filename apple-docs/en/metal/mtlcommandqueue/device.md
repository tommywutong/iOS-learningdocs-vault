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
doc_path: /documentation/metal/mtlcommandqueue/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/device.json'
content_hash: 'sha256:f5a6df560d3dc6a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# device

<sub>Instance Property</sub>

The GPU device that creates the command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

The command queue can submit work only to the GPU the [MTLDevice](../mtldevice.md) instance represents.

## See Also

### Identifying the command queue

- [label](label.md) — An optional name that can help you identify the command queue.
