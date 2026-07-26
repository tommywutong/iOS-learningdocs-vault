---
title: stride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexbufferlayoutdescriptor/stride
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptor/stride.json'
content_hash: 'sha256:92c24b3c6aa7a731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexBufferLayoutDescriptor](../mtlvertexbufferlayoutdescriptor.md)

# stride

<sub>Instance Property</sub>

The number of bytes between the first byte of two consecutive vertices in a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stride: Int { get set }
```

## Discussion

Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Organizing the vertex buffer layout

- [stepFunction](stepfunction.md) — The circumstances under which the vertex and its attributes are presented to the vertex function.
- [stepRate](steprate.md) — The interval at which the vertex and its attributes are presented to the vertex function.
- [MTLVertexStepFunction](../mtlvertexstepfunction.md) — The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.
