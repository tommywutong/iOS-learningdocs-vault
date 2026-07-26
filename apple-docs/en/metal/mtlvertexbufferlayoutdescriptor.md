---
title: MTLVertexBufferLayoutDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexbufferlayoutdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptor.json'
content_hash: 'sha256:e888ba7dcff90e26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexBufferLayoutDescriptor

<sub>Class</sub>

An object that configures how a render pipeline fetches data to send to the vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexBufferLayoutDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Organizing the vertex buffer layout

- [stepFunction](mtlvertexbufferlayoutdescriptor/stepfunction.md) — The circumstances under which the vertex and its attributes are presented to the vertex function.
- [stepRate](mtlvertexbufferlayoutdescriptor/steprate.md) — The interval at which the vertex and its attributes are presented to the vertex function.
- [stride](mtlvertexbufferlayoutdescriptor/stride.md) — The number of bytes between the first byte of two consecutive vertices in a buffer.
- [MTLVertexStepFunction](mtlvertexstepfunction.md) — The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.

## See Also

### Render pass inputs

- [MTLVertexDescriptor](mtlvertexdescriptor.md) — An instance that describes how to organize and map data to a vertex function.
- [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) — An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) — An array of vertex attribute descriptor instances.
- [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) — An array of vertex buffer layout descriptor instances.
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)
