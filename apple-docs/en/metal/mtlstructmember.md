---
title: MTLStructMember
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember.json'
content_hash: 'sha256:d37b335f2c07df36'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStructMember

<sub>Class</sub>

An instance that provides information about a field in a structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLStructMember
```

## Overview

[MTLStructMember](mtlstructmember.md) is part of the reflection API that allows Metal framework code to query details about an argument of a Metal shading language function. An [MTLStructMember](mtlstructmember.md) instance describes the data type of one field in a struct that is passed as an [MTLFunction](mtlfunction.md) argument, which is represented by [MTLArgument](mtlargument.md).

Don’t create [MTLStructMember](mtlstructmember.md) instances directly. You obtain an [MTLStructMember](mtlstructmember.md) instance from either the [members](mtlstructtype/members.md) property or the [- memberByName:](<mtlstructtype/memberbyname(__).md>) method of an [MTLStructType](mtlstructtype.md) instance. The [dataType](mtlstructmember/datatype.md) property of the [MTLStructMember](mtlstructmember.md) instance tells you what kind of data is stored in the member. Recursively drill down every struct member until you reach a data type that is neither a struct nor an array.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the struct member

- [name](mtlstructmember/name.md) — The name of the struct member.
- [dataType](mtlstructmember/datatype.md) — The data type of the struct member.
- [offset](mtlstructmember/offset.md) — The location of this member relative to the start of its struct, in bytes.
- [argumentIndex](mtlstructmember/argumentindex.md) — The index in the argument table that corresponds to the struct member.

### Obtaining struct member details

- [- arrayType](<mtlstructmember/arraytype().md>) — Provides a description of the underlying array when the struct member holds an array.
- [- structType](<mtlstructmember/structtype().md>) — Provides a description of the underlying struct when the struct member holds a struct.
- [- pointerType](<mtlstructmember/pointertype().md>) — Provides a description of the underlying pointer when the struct member holds a pointer.
- [- textureReferenceType](<mtlstructmember/texturereferencetype().md>) — Provides a description of the underlying texture when the struct member holds a texture.

### Instance Methods

- [- tensorReferenceType](<mtlstructmember/tensorreferencetype().md>) — Provides a description of the underlying tensor type when this struct member holds a tensor.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLDataType](mtldatatype.md) — The parameter type options for GPU functions, such as shaders and compute kernels.
- [MTLArrayType](mtlarraytype.md) — A description of an array.
- [MTLStructType](mtlstructtype.md) — A description of a structure.
- [MTLPointerType](mtlpointertype.md) — A description of a pointer.
- [MTLTextureReferenceType](mtltexturereferencetype.md) — A description of a texture.
