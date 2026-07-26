---
title: MTLVertexDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexdescriptor.json'
content_hash: 'sha256:6ed56ec60ec50bc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexDescriptor

<sub>Class</sub>

An instance that describes how to organize and map data to a vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexDescriptor
```

## Overview

An [MTLVertexDescriptor](mtlvertexdescriptor.md) instance is used to configure how vertex data stored in memory is mapped to attributes in a vertex shader.

A pipeline state is the state of the graphics rendering pipeline, including shaders, blending, multisampling, and visibility testing. For every pipeline state, there can be only one [MTLVertexDescriptor](mtlvertexdescriptor.md) instance. When you configure an [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) instance to create this pipeline state, you use an [MTLVertexDescriptor](mtlvertexdescriptor.md) instance to establish the vertex layout for the function associated with the pipeline. Create and configure an [MTLVertexDescriptor](mtlvertexdescriptor.md) instance, then use this instance to set the [vertexDescriptor](mtlrenderpipelinedescriptor/vertexdescriptor.md) property of the [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) instance.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting default values

- [- reset](<mtlvertexdescriptor/reset().md>) — Resets the default state for the vertex descriptor.

### Accessing the vertex buffer layouts and vertex attributes

- [attributes](mtlvertexdescriptor/attributes.md) — An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.
- [layouts](mtlvertexdescriptor/layouts.md) — An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.

## See Also

### Render pass inputs

- [MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md) — An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md) — An array of vertex attribute descriptor instances.
- [MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md) — An object that configures how a render pipeline fetches data to send to the vertex function.
- [MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md) — An array of vertex buffer layout descriptor instances.
- [MTLBufferLayoutStrideDynamic](mtlbufferlayoutstridedynamic.md)
