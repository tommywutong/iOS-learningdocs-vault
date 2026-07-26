---
title: element()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype/element()
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype/element()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype/element%28%29.json'
content_hash: 'sha256:02dc6e304ea1a78c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArrayType](../mtlarraytype.md)

# element()

<sub>Instance Method</sub>

Provides a description of the underlying type when an array holds other arrays as its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func element() -> MTLArrayType?
```

## Return Value

Returns an object that describes an array. If the array elements aren’t arrays, this method returns `nil`.

## Discussion

Use this method if [elementType](elementtype.md) is [MTLDataTypeArray](../mtldatatype/array.md).

## See Also

### Obtaining details for complex array elements

- [- elementStructType](<elementstructtype().md>) — Provides a description of the underlying struct type when an array holds structs as its elements.
- [- elementPointerType](<elementpointertype().md>) — Provides a description of the underlying pointer type when an array holds pointers as its elements.
- [- elementTextureReferenceType](<elementtexturereferencetype().md>) — Provides a description of the underlying texture type when an array holds textures as its elements.
