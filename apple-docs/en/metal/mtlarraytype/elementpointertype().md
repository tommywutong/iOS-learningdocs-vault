---
title: elementPointerType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype/elementpointertype()
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype/elementpointertype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype/elementpointertype%28%29.json'
content_hash: 'sha256:489ded0b53ce79a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArrayType](../mtlarraytype.md)

# elementPointerType()

<sub>Instance Method</sub>

Provides a description of the underlying pointer type when an array holds pointers as its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func elementPointerType() -> MTLPointerType?
```

## Return Value

An object that describes the pointer. If the array elements aren’t pointers, this method returns `nil`.

## Discussion

Use this method if [elementType](elementtype.md) is [MTLDataTypePointer](../mtldatatype/pointer.md).

## See Also

### Obtaining details for complex array elements

- [- elementArrayType](<element().md>) — Provides a description of the underlying type when an array holds other arrays as its elements.
- [- elementStructType](<elementstructtype().md>) — Provides a description of the underlying struct type when an array holds structs as its elements.
- [- elementTextureReferenceType](<elementtexturereferencetype().md>) — Provides a description of the underlying texture type when an array holds textures as its elements.
