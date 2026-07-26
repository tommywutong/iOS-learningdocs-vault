---
title: commandBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandencoder/commandbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/commandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/commandbuffer.json'
content_hash: 'sha256:b14e790bc10cf941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# commandBuffer

<sub>Instance Property</sub>

Returns the command buffer that is currently encoding commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var commandBuffer: (any MTL4CommandBuffer)? { get }
```

## Discussion

This property may return undefined results if you call it after calling [- endEncoding](<endencoding().md>).
