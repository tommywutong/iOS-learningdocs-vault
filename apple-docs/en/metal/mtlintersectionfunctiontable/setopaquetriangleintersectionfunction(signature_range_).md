---
title: 'setOpaqueTriangleIntersectionFunction(signature:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction%28signature%3Arange%3A%29.json'
content_hash: 'sha256:60e3499f44f4619b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setOpaqueTriangleIntersectionFunction(signature:range:)

<sub>Instance Method</sub>

Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)
```

## Parameters

- `signature` — The signature of the function.

- `range` — A range of indices to change in the table.

## See Also

### Specifying opaque triangle intersection testing

- [- setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:](<setopaquetriangleintersectionfunction(signature_index_).md>) — Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.
