---
title: MTLVertexBufferLayoutDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexbufferlayoutdescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptorarray.json'
content_hash: 'sha256:249e2beb38150a5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexBufferLayoutDescriptorArray

<sub>Class</sub>

An array of vertex buffer layout descriptor instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexBufferLayoutDescriptorArray
```

## Overview

An [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) holds an array of vertex buffer layout states. The methods of [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) set the vertex buffer layout state in the array or retrieve the state from the array.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing a specified vertex buffer layout

- [- objectAtIndexedSubscript:](<mtlvertexbufferlayoutdescriptorarray/subscript(__).md>) — Returns the state of the specified vertex buffer layout.

## See Also

### Render pass inputs

- [MTLVertexDescriptor](mtlvertexdescriptor.md) — An instance that describes how to organize and map data to a vertex function.
- [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) — An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) — An array of vertex attribute descriptor instances.
- [MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md) — An object that configures how a render pipeline fetches data to send to the vertex function.
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)
