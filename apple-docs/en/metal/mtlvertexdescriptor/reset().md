---
title: reset()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexdescriptor/reset()
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexdescriptor/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexdescriptor/reset%28%29.json'
content_hash: 'sha256:9ee951b791d33a8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexDescriptor](../mtlvertexdescriptor.md)

# reset()

<sub>Instance Method</sub>

Resets the default state for the vertex descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset()
```

## Discussion

After reset, each element of the [attributes](attributes.md) array has a default vertex attribute descriptor, and each element of the [layouts](layouts.md) array has a default vertex buffer layout descriptor.
