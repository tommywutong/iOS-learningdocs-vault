---
title: 'setOpaqueTriangleIntersectionFunction(signature:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setopaquetriangleintersectionfunction%28signature%3Aindex%3A%29.json'
content_hash: 'sha256:5677c8ac1e655a6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setOpaqueTriangleIntersectionFunction(signature:index:)

<sub>Instance Method</sub>

Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)
```

## Parameters

- `signature` — The signature of the function.

- `index` — The index in the table to change.

## See Also

### Specifying opaque triangle intersection testing

- [- setOpaqueTriangleIntersectionFunctionWithSignature:withRange:](<setopaquetriangleintersectionfunction(signature_range_).md>) — Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.
