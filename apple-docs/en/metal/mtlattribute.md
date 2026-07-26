---
title: MTLAttribute
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattribute
source_url: 'https://developer.apple.com/documentation/metal/mtlattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattribute.json'
content_hash: 'sha256:ec9a30637a1656f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAttribute

<sub>Class</sub>

An object that describes an attribute defined in the stage-in argument for a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAttribute
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Reading an attribute’s properties

- [name](mtlattribute/name.md) — The name of the attribute.
- [attributeIndex](mtlattribute/attributeindex.md) — The index of the attribute, as declared in Metal shader source code.
- [attributeType](mtlattribute/attributetype.md) — The data type for the attribute, as declared in Metal shader source code.
- [active](mtlattribute/isactive.md) — A Boolean value that indicates whether the attribute is active.
- [patchControlPointData](mtlattribute/ispatchcontrolpointdata.md) — A Boolean value that indicates whether the attribute represents control point data.
- [patchData](mtlattribute/ispatchdata.md) — A Boolean value that indicates whether the attribute represents tessellation patch data.

## See Also

### Function arguments

- [MTLVertexAttribute](mtlvertexattribute.md) — An instance that represents an attribute of a vertex function.
- [MTLArgument](mtlargument.md) — Information about an argument of a graphics or compute function. _(deprecated)_
- [MTLAutoreleasedArgument](mtlautoreleasedargument.md) — A convenience type alias for an autoreleased argument instance. _(deprecated)_
- [MTLArgumentType](mtlargumenttype.md) — The resource type for an argument of a function. _(deprecated)_
- [MTLArgumentAccess](mtlargumentaccess.md) — Function access restrictions to argument data in the shading language code. _(deprecated)_
