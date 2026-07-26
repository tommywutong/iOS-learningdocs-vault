---
title: 'CGSizeCreateDictionaryRepresentation(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgsizecreatedictionaryrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsizecreatedictionaryrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsizecreatedictionaryrepresentation%28_%3A%29.json'
content_hash: 'sha256:af7a36071a018fa0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSizeCreateDictionaryRepresentation(_:)

<sub>Function</sub>

Returns a dictionary representation of the specified size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGSizeCreateDictionaryRepresentation(_ size: CGSize) -> CFDictionary
```

## Parameters

- `size` — A size.

## Return Value

The dictionary representation of the size.

## See Also

### Creating a Dictionary Representation from a Geometric Primitive

- [CGPointCreateDictionaryRepresentation](<cgpointcreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the specified point.
- [CGRectCreateDictionaryRepresentation](<cgrectcreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the provided rectangle.
