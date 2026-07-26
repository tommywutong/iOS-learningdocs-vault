---
title: MTLBufferLayoutDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbufferlayoutdescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptorarray.json'
content_hash: 'sha256:4a66c8efad801f61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBufferLayoutDescriptorArray

<sub>Class</sub>

An array of buffer layout descriptor objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBufferLayoutDescriptorArray
```

## Overview

An [MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md) defines the data layout and loading for compute data, using [MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md) instances.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Array accessors

- [- objectAtIndexedSubscript:](<mtlbufferlayoutdescriptorarray/subscript(__).md>) — Returns the state of the specified buffer layout.

## See Also

### Configuring compute pass inputs

- [stageInputDescriptor](mtlcomputepipelinedescriptor/stageinputdescriptor.md) — The organization of input and output data for the next kernel call.
- [MTLAttributeDescriptor](mtlattributedescriptor.md) — A descriptor of an argument’s format and where its data is in memory.
- [MTLAttributeDescriptorArray](mtlattributedescriptorarray.md) — An array of attribute descriptor objects.
- [MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md) — A description of how a compute function fetches input data for an attribute.
