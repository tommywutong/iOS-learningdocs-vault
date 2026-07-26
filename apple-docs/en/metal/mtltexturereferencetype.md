---
title: MTLTextureReferenceType
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturereferencetype
source_url: 'https://developer.apple.com/documentation/metal/mtltexturereferencetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturereferencetype.json'
content_hash: 'sha256:9af35e5afe5d2ca6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureReferenceType

<sub>Class</sub>

A description of a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTextureReferenceType
```

## Relationships

- **Inherits From**: [MTLType](mtltype.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the texture

- [textureType](mtltexturereferencetype/texturetype.md) — The texture type of the texture.
- [textureDataType](mtltexturereferencetype/texturedatatype.md) — The data type of the texture.
- [access](mtltexturereferencetype/access.md) — The texture’s read/write access to the argument.
- [isDepthTexture](mtltexturereferencetype/isdepthtexture.md) — A Boolean value that indicates whether the texture is a depth texture.

## See Also

### Shader types

- [MTLType](mtltype.md) — A description of a data type.
- [MTLDataType](mtldatatype.md) — The parameter type options for GPU functions, such as shaders and compute kernels.
- [MTLArrayType](mtlarraytype.md) — A description of an array.
- [MTLStructType](mtlstructtype.md) — A description of a structure.
- [MTLStructMember](mtlstructmember.md) — An instance that provides information about a field in a structure.
- [MTLPointerType](mtlpointertype.md) — A description of a pointer.
