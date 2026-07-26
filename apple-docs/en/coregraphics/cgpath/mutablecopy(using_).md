---
title: 'mutableCopy(using:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/mutablecopy(using:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/mutablecopy(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/mutablecopy%28using%3A%29.json'
content_hash: 'sha256:677463d666ad02aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# mutableCopy(using:)

<sub>Instance Method</sub>

Creates a mutable copy of a graphics path transformed by a transformation matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableCopy(using transform: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?
```

## Parameters

- `transform` — A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to all elements of the new path.

## Return Value

A new, mutable copy of the specified path transformed by the transform parameter. You are responsible for releasing this object.

## See Also

### Copying a Graphics Path

- [CGPathCreateMutableCopy](<mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
