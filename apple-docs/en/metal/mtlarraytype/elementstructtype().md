---
title: elementStructType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype/elementstructtype()
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype/elementstructtype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype/elementstructtype%28%29.json'
content_hash: 'sha256:9fc384cffd2d36c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArrayType](../mtlarraytype.md)

# elementStructType()

<sub>Instance Method</sub>

Provides a description of the underlying struct type when an array holds structs as its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func elementStructType() -> MTLStructType?
```

## Return Value

An object that describes the struct. If the array elements aren’t structs, this method returns `nil`.

## Discussion

Use this method if [elementType](elementtype.md) is [MTLDataTypeStruct](../mtldatatype/struct.md).

## See Also

### Obtaining details for complex array elements

- [- elementArrayType](<element().md>) — Provides a description of the underlying type when an array holds other arrays as its elements.
- [- elementPointerType](<elementpointertype().md>) — Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [- elementTextureReferenceType](<elementtexturereferencetype().md>) — Provides a description of the underlying texture type when an array holds textures as its elements.
