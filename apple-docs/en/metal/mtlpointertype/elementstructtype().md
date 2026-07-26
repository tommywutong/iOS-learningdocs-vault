---
title: elementStructType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpointertype/elementstructtype()
source_url: 'https://developer.apple.com/documentation/metal/mtlpointertype/elementstructtype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpointertype/elementstructtype%28%29.json'
content_hash: 'sha256:c3a94254a869a889'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPointerType](../mtlpointertype.md)

# elementStructType()

<sub>Instance Method</sub>

Provides a description of the underlying struct when the pointer points to a struct.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func elementStructType() -> MTLStructType?
```

## Return Value

An object that describes the struct. If the pointer does not point to an struct, this method returns `nil`.

## See Also

### Obtaining details for complex pointer elements

- [- elementArrayType](<elementarraytype().md>) — Provides a description of the underlying array when the pointer points to an array.
