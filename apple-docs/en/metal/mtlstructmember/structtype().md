---
title: structType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/structtype()
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/structtype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/structtype%28%29.json'
content_hash: 'sha256:c7b0cfe43e11208c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# structType()

<sub>Instance Method</sub>

Provides a description of the underlying struct when the struct member holds a struct.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func structType() -> MTLStructType?
```

## Return Value

An object that describes the struct. If [dataType](datatype.md) indicates that this member is not a struct, this method returns `nil`.

## See Also

### Obtaining struct member details

- [- arrayType](<arraytype().md>) — Provides a description of the underlying array when the struct member holds an array.
- [- pointerType](<pointertype().md>) — Provides a description of the underlying pointer when the struct member holds a pointer.
- [- textureReferenceType](<texturereferencetype().md>) — Provides a description of the underlying texture when the struct member holds a texture.
