---
title: MTLVertexAttribute
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattribute
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattribute.json'
content_hash: 'sha256:0ad6844154861a1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexAttribute

<sub>Class</sub>

An instance that represents an attribute of a vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLVertexAttribute
```

## Overview

An [MTLVertexAttribute](mtlvertexattribute.md) instance represents an attribute for per-vertex input in a vertex function. You use vertex attribute instances to inspect the inputs of a vertex function by examining the [vertexAttributes](mtlfunction/vertexattributes.md) property of the corresponding [MTLFunction](mtlfunction.md) instance.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the attribute

- [name](mtlvertexattribute/name.md) — The name of the attribute.
- [attributeIndex](mtlvertexattribute/attributeindex.md) — The index of the attribute, as declared in Metal shader source code.
- [attributeType](mtlvertexattribute/attributetype.md) — The data type for the attribute, as declared in Metal shader source code.
- [active](mtlvertexattribute/isactive.md) — A Boolean value that indicates whether this vertex attribute is active.
- [patchControlPointData](mtlvertexattribute/ispatchcontrolpointdata.md) — A Boolean value that indicates whether this vertex attribute represents control point data.
- [patchData](mtlvertexattribute/ispatchdata.md) — A Boolean value that indicates whether this vertex attribute represents patch data.

## See Also

### Function arguments

- [MTLAttribute](mtlattribute.md) — An object that describes an attribute defined in the stage-in argument for a shader.
- [MTLArgument](mtlargument.md) — Information about an argument of a graphics or compute function. _(deprecated)_
- [MTLAutoreleasedArgument](mtlautoreleasedargument.md) — A convenience type alias for an autoreleased argument instance. _(deprecated)_
- [MTLArgumentType](mtlargumenttype.md) — The resource type for an argument of a function. _(deprecated)_
- [MTLArgumentAccess](mtlargumentaccess.md) — Function access restrictions to argument data in the shading language code. _(deprecated)_
