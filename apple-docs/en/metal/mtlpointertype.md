---
title: MTLPointerType
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpointertype
source_url: 'https://developer.apple.com/documentation/metal/mtlpointertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpointertype.json'
content_hash: 'sha256:a8602fc4849ddfca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPointerType

<sub>Class</sub>

A description of a pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLPointerType
```

## Relationships

- **Inherits From**: [MTLType](mtltype.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the pointer elements

- [alignment](mtlpointertype/alignment.md) — The required byte alignment in memory for the element data.
- [dataSize](mtlpointertype/datasize.md) — The size, in bytes, of the element data.
- [elementType](mtlpointertype/elementtype.md) — The data type of the element data.
- [access](mtlpointertype/access.md) — The function’s read/write access to the element data.
- [elementIsArgumentBuffer](mtlpointertype/elementisargumentbuffer.md) — A Boolean value that indicates whether the element is an argument buffer.

### Obtaining details for complex pointer elements

- [- elementArrayType](<mtlpointertype/elementarraytype().md>) — Provides a description of the underlying array when the pointer points to an array.
- [- elementStructType](<mtlpointertype/elementstructtype().md>) — Provides a description of the underlying struct when the pointer points to a struct.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLDataType](mtldatatype.md) — The parameter type options for GPU functions, such as shaders and compute kernels.
- [MTLArrayType](mtlarraytype.md) — A description of an array.
- [MTLStructType](mtlstructtype.md) — A description of a structure.
- [MTLStructMember](mtlstructmember.md) — An instance that provides information about a field in a structure.
- [MTLTextureReferenceType](mtltexturereferencetype.md) — A description of a texture.
