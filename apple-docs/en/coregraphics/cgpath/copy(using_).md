---
title: 'copy(using:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/copy(using:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/copy(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/copy%28using%3A%29.json'
content_hash: 'sha256:baeaef7958e55549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# copy(using:)

<sub>Instance Method</sub>

Creates an immutable copy of a graphics path transformed by a transformation matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(using transform: UnsafePointer<CGAffineTransform>?) -> CGPath?
```

## Parameters

- `transform` — A pointer to an affine transformation matrix, or `NULL` if no transformation is needed. If specified, Core Graphics applies the transformation to all elements of the new path.

## Return Value

A new, immutable copy of the path. You are responsible for releasing this object.

## See Also

### Copying a Graphics Path

- [CGPathCreateCopy](<copy().md>) — Creates an immutable copy of a graphics path.
- [copy(dashingWithPhase:lengths:transform:)](<copy(dashingwithphase_lengths_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)](<copy(strokingwithwidth_linecap_linejoin_miterlimit_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [CGPathCreateMutableCopy](<mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
- [CGPathCreateMutableCopyByTransformingPath](<mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.
