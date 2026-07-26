---
title: MTLStructType
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructtype
source_url: 'https://developer.apple.com/documentation/metal/mtlstructtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructtype.json'
content_hash: 'sha256:066147068861a4dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStructType

<sub>Class</sub>

A description of a structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLStructType
```

## Overview

[MTLStructType](mtlstructtype.md) is part of the reflection API that allows Metal framework code to query details of a struct that is passed as an argument of a Metal shading language function. Don’t create [MTLStructType](mtlstructtype.md) instances directly; instead query the [bufferStructType](mtlargument/bufferstructtype.md) property of an [MTLArgument](mtlargument.md) instance, or call the [- structType](<mtlstructmember/structtype().md>) method for an [MTLStructMember](mtlstructmember.md) instance. To examine the details of the struct, you can recursively drill down the [members](mtlstructtype/members.md) property of the [MTLStructType](mtlstructtype.md) instance, which contains details about struct members, each of which is represented by an [MTLStructMember](mtlstructmember.md) instance.

## Relationships

- **Inherits From**: [MTLType](mtltype.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Obtaining information about struct members

- [members](mtlstructtype/members.md) — An array of instances that describe the fields in the struct.
- [- memberByName:](<mtlstructtype/memberbyname(__).md>) — Provides a representation of a struct member.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLDataType](mtldatatype.md) — The parameter type options for GPU functions, such as shaders and compute kernels.
- [MTLArrayType](mtlarraytype.md) — A description of an array.
- [MTLStructMember](mtlstructmember.md) — An instance that provides information about a field in a structure.
- [MTLPointerType](mtlpointertype.md) — A description of a pointer.
- [MTLTextureReferenceType](mtltexturereferencetype.md) — A description of a texture.
