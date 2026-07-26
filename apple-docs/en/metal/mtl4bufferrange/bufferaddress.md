---
title: bufferAddress
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4bufferrange/bufferaddress
source_url: 'https://developer.apple.com/documentation/metal/mtl4bufferrange/bufferaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4bufferrange/bufferaddress.json'
content_hash: 'sha256:fc7fa8aeb3aa0526'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4BufferRange](../mtl4bufferrange.md)

# bufferAddress

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferAddress: MTLGPUAddress
```

## Discussion

Buffer address returned by the gpuAddress property of an MTLBuffer plus any offset into the buffer
