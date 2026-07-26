---
title: textureReferenceType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/texturereferencetype()
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/texturereferencetype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/texturereferencetype%28%29.json'
content_hash: 'sha256:41d94ac7b1b8ee7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# textureReferenceType()

<sub>Instance Method</sub>

Provides a description of the underlying texture when the struct member holds a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func textureReferenceType() -> MTLTextureReferenceType?
```

## Return Value

An object that describes the texture. If [dataType](datatype.md) indicates that this member isn’t a texture, this method returns `nil`.

## See Also

### Obtaining struct member details

- [- arrayType](<arraytype().md>) — Provides a description of the underlying array when the struct member holds an array.
- [- structType](<structtype().md>) — Provides a description of the underlying struct when the struct member holds a struct.
- [- pointerType](<pointertype().md>) — Provides a description of the underlying pointer when the struct member holds a pointer.
