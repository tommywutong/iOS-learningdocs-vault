---
title: pointerType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/pointertype()
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/pointertype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/pointertype%28%29.json'
content_hash: 'sha256:5a72ba20aef6d93f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# pointerType()

<sub>Instance Method</sub>

Provides a description of the underlying pointer when the struct member holds a pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pointerType() -> MTLPointerType?
```

## Return Value

An object that describes the pointer. If [dataType](datatype.md) indicates that this member isn’t a pointer, this method returns `nil`.

## See Also

### Obtaining struct member details

- [- arrayType](<arraytype().md>) — Provides a description of the underlying array when the struct member holds an array.
- [- structType](<structtype().md>) — Provides a description of the underlying struct when the struct member holds a struct.
- [- textureReferenceType](<texturereferencetype().md>) — Provides a description of the underlying texture when the struct member holds a texture.
