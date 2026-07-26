---
title: arrayType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/arraytype()
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/arraytype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/arraytype%28%29.json'
content_hash: 'sha256:e33086565401535b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# arrayType()

<sub>Instance Method</sub>

Provides a description of the underlying array when the struct member holds an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func arrayType() -> MTLArrayType?
```

## Return Value

An object that describes the array. If [dataType](datatype.md) indicates that this member is not an array, this method returns `nil.`

## See Also

### Obtaining struct member details

- [- structType](<structtype().md>) — Provides a description of the underlying struct when the struct member holds a struct.
- [- pointerType](<pointertype().md>) — Provides a description of the underlying pointer when the struct member holds a pointer.
- [- textureReferenceType](<texturereferencetype().md>) — Provides a description of the underlying texture when the struct member holds a texture.
