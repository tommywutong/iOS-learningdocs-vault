---
title: 'copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/copy(strokingwithwidth:linecap:linejoin:miterlimit:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/copy(strokingwithwidth:linecap:linejoin:miterlimit:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/copy%28strokingwithwidth%3Alinecap%3Alinejoin%3Amiterlimit%3Atransform%3A%29.json'
content_hash: 'sha256:9a4153a4f96ffa8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)

<sub>Instance Method</sub>

Returns a new path equivalent to the results of drawing the path with a solid stroke.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(strokingWithWidth lineWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform = .identity) -> CGPath
```

## Parameters

- `lineWidth` — The line width to use, in user space units. The value must be greater than `0`.

- `lineCap` — The line cap style to render. (For equivalent [CGContext](../cgcontext.md) drawing methods, the default style is [kCGLineCapButt](../cglinecap/butt.md).)

- `lineJoin` — The line join style to render. (For equivalent [CGContext](../cgcontext.md) drawing methods, the default style is [kCGLineJoinMiter](../cglinejoin/miter.md).)

- `miterLimit` — A value that limits how sharp individual corners in the path can be when using the [kCGLineJoinMiter](../cglinejoin/miter.md) line join style. When the ratio of a the length required for a mitered corner to the line width exceeds this value, that corner uses the [kCGLineJoinBevel](../cglinejoin/bevel.md) style instead.

- `transform` — An affine transform to apply to the path before dashing. Defaults to the [CGAffineTransformIdentity](../cgaffinetransformidentity.md) transform if not specified.

## Return Value

A new path.

## Discussion

The new path is created so that filling the new path draws the same pixels as stroking the original path with the specified line style.

## See Also

### Copying a Graphics Path

- [CGPathCreateCopy](<copy().md>) — Creates an immutable copy of a graphics path.
- [CGPathCreateCopyByTransformingPath](<copy(using_).md>) — Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [copy(dashingWithPhase:lengths:transform:)](<copy(dashingwithphase_lengths_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [CGPathCreateMutableCopy](<mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
- [CGPathCreateMutableCopyByTransformingPath](<mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.
