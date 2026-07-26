---
title: copy()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/copy()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/copy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/copy%28%29.json'
content_hash: 'sha256:53fde86e84af7135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# copy()

<sub>Instance Method</sub>

Creates an immutable copy of a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy() -> CGPath?
```

## Return Value

A new, immutable copy of the specified path. You are responsible for releasing this object.

## See Also

### Copying a Graphics Path

- [CGPathCreateCopyByTransformingPath](<copy(using_).md>) — Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [copy(dashingWithPhase:lengths:transform:)](<copy(dashingwithphase_lengths_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)](<copy(strokingwithwidth_linecap_linejoin_miterlimit_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [CGPathCreateMutableCopy](<mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
- [CGPathCreateMutableCopyByTransformingPath](<mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.
