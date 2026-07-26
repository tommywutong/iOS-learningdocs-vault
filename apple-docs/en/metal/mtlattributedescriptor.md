---
title: MTLAttributeDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattributedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptor.json'
content_hash: 'sha256:8bf52de9adb6ebb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAttributeDescriptor

<sub>Class</sub>

A descriptor of an argument’s format and where its data is in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAttributeDescriptor
```

## Overview

Attribute descriptors are part of an [MTLVertexDescriptor](mtlvertexdescriptor.md) or [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) instance to provide layout information about a function’s arguments. Each descriptor is for a single argument, containing information about the attached data, offset and stride, and data type.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Defining attribute location

- [bufferIndex](mtlattributedescriptor/bufferindex.md) — The index in the buffer argument table for the buffer that contains the data for this attribute.
- [offset](mtlattributedescriptor/offset.md) — The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [format](mtlattributedescriptor/format.md) — The format of the attribute’s data.
- [MTLAttributeFormat](mtlattributeformat.md) — The data format options for acceleration structures.

## See Also

### Configuring compute pass inputs

- [stageInputDescriptor](mtlcomputepipelinedescriptor/stageinputdescriptor.md) — The organization of input and output data for the next kernel call.
- [MTLAttributeDescriptorArray](mtlattributedescriptorarray.md) — An array of attribute descriptor objects.
- [MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md) — A description of how a compute function fetches input data for an attribute.
- [MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md) — An array of buffer layout descriptor objects.
