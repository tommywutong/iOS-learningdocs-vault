---
title: 'CGRectMakeWithDictionaryRepresentation(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectmakewithdictionaryrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectmakewithdictionaryrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectmakewithdictionaryrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:56f62648d0ff1aa9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectMakeWithDictionaryRepresentation(_:_:)

<sub>Function</sub>

Fills in a rectangle using the contents of the specified dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary, _ rect: UnsafeMutablePointer<CGRect>) -> Bool
```

## Parameters

- `dict` — A dictionary that was previously returned from the function [CGRectCreateDictionaryRepresentation](<cgrectcreatedictionaryrepresentation(__).md>).

- `rect` — On return, the rectangle created from the specified dictionary.

## Return Value

[true](../swift/true.md) if successful; otherwise [false](../swift/false.md).

## See Also

### Creating a Geometric Primitive from a Dictionary Representation

- [CGPointMakeWithDictionaryRepresentation](<cgpointmakewithdictionaryrepresentation(____).md>) — Fills in a point using the contents of the specified dictionary.
- [CGSizeMakeWithDictionaryRepresentation](<cgsizemakewithdictionaryrepresentation(____).md>) — Fills in a size using the contents of the specified dictionary.
