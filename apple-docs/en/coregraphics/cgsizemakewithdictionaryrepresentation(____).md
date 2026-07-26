---
title: 'CGSizeMakeWithDictionaryRepresentation(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgsizemakewithdictionaryrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsizemakewithdictionaryrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsizemakewithdictionaryrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:55e04767f8ff6fa0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSizeMakeWithDictionaryRepresentation(_:_:)

<sub>Function</sub>

Fills in a size using the contents of the specified dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ size: UnsafeMutablePointer<CGSize>) -> Bool
```

## Parameters

- `dict` — A dictionary that was previously returned from the function [CGSizeCreateDictionaryRepresentation](<cgsizecreatedictionaryrepresentation(__).md>).

- `size` — On return, the size created from the specified dictionary.

## Return Value

[true](../swift/true.md) if successful; otherwise [false](../swift/false.md).

## See Also

### Creating a Geometric Primitive from a Dictionary Representation

- [CGPointMakeWithDictionaryRepresentation](<cgpointmakewithdictionaryrepresentation(____).md>) — Fills in a point using the contents of the specified dictionary.
- [CGRectMakeWithDictionaryRepresentation](<cgrectmakewithdictionaryrepresentation(____).md>) — Fills in a rectangle using the contents of the specified dictionary.
