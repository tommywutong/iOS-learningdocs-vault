---
title: 'CGPointCreateDictionaryRepresentation(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpointcreatedictionaryrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpointcreatedictionaryrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpointcreatedictionaryrepresentation%28_%3A%29.json'
content_hash: 'sha256:6294d3f706be1f7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPointCreateDictionaryRepresentation(_:)

<sub>Function</sub>

Returns a dictionary representation of the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPointCreateDictionaryRepresentation(_ point: CGPoint) -> CFDictionary
```

## Parameters

- `point` — A point.

## Return Value

The dictionary representation of the point.

## See Also

### Creating a Dictionary Representation from a Geometric Primitive

- [CGSizeCreateDictionaryRepresentation](<cgsizecreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the specified size.
- [CGRectCreateDictionaryRepresentation](<cgrectcreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the provided rectangle.
