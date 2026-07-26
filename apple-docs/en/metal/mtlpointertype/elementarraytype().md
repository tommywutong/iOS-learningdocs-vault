---
title: elementArrayType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpointertype/elementarraytype()
source_url: 'https://developer.apple.com/documentation/metal/mtlpointertype/elementarraytype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpointertype/elementarraytype%28%29.json'
content_hash: 'sha256:0d5f2f264d407af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPointerType](../mtlpointertype.md)

# elementArrayType()

<sub>Instance Method</sub>

Provides a description of the underlying array when the pointer points to an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func elementArrayType() -> MTLArrayType?
```

## Return Value

An object that describes the array. If the pointer does not point to an array, this method returns `nil`.

## See Also

### Obtaining details for complex pointer elements

- [- elementStructType](<elementstructtype().md>) — Provides a description of the underlying struct when the pointer points to a struct.
