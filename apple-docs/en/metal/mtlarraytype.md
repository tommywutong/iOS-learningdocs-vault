---
title: MTLArrayType
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype.json'
content_hash: 'sha256:2d8d75b3cb2ba626'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArrayType

<sub>Class</sub>

A description of an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLArrayType
```

## Overview

An [MTLArrayType](mtlarraytype.md) instance provides details about an array parameter. Don’t create [MTLArrayType](mtlarraytype.md) instances directly; other reflection instances contain properties to determine if a parameter is an array and to obtain the [MTLArrayType](mtlarraytype.md) instance that describes the array.

## Relationships

- **Inherits From**: [MTLType](mtltype.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the array elements

- [arrayLength](mtlarraytype/arraylength.md) — The number of elements in the array.
- [elementType](mtlarraytype/elementtype.md) — The data type of the array’s elements.
- [stride](mtlarraytype/stride.md) — The stride between array elements, in bytes.
- [argumentIndexStride](mtlarraytype/argumentindexstride.md) — The stride, in bytes, between argument indices.

### Obtaining details for complex array elements

- [- elementArrayType](<mtlarraytype/element().md>) — Provides a description of the underlying type when an array holds other arrays as its elements.
- [- elementStructType](<mtlarraytype/elementstructtype().md>) — Provides a description of the underlying struct type when an array holds structs as its elements.
- [- elementPointerType](<mtlarraytype/elementpointertype().md>) — Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [- elementTextureReferenceType](<mtlarraytype/elementtexturereferencetype().md>) — Provides a description of the underlying texture type when an array holds textures as its elements.

### Instance Methods

- [- elementTensorReferenceType](<mtlarraytype/elementtensorreferencetype().md>) — Provides a description of the underlying tensor type when this array holds tensors as its elements.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLDataType](mtldatatype.md) — The parameter type options for GPU functions, such as shaders and compute kernels.
- [MTLStructType](mtlstructtype.md) — A description of a structure.
- [MTLStructMember](mtlstructmember.md) — An instance that provides information about a field in a structure.
- [MTLPointerType](mtlpointertype.md) — A description of a pointer.
- [MTLTextureReferenceType](mtltexturereferencetype.md) — A description of a texture.
