---
title: MTLVertexAttributeDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattributedescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattributedescriptorarray.json'
content_hash: 'sha256:5c512d013da1cd2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexAttributeDescriptorArray

<sub>Class</sub>

An array of vertex attribute descriptor instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexAttributeDescriptorArray
```

## Overview

An [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) instance is an array of instances that defines how vertex attribute data is formatted and assigned to an index in the attribute argument table. The methods of [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) set or retrieve the attribute formatting information from the array.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing a specified vertex attribute

- [- objectAtIndexedSubscript:](<mtlvertexattributedescriptorarray/subscript(__).md>) — Returns the state of the specified vertex attribute.

## See Also

### Render pass inputs

- [MTLVertexDescriptor](mtlvertexdescriptor.md) — An instance that describes how to organize and map data to a vertex function.
- [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) — An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md) — An object that configures how a render pipeline fetches data to send to the vertex function.
- [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) — An array of vertex buffer layout descriptor instances.
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)
