---
title: NSEdgeInsets
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsedgeinsets
source_url: 'https://developer.apple.com/documentation/foundation/nsedgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsedgeinsets.json'
content_hash: 'sha256:0cb9345ebca706a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEdgeInsets

<sub>Structure</sub>

A description of the distance between the edges of two rectangles.

<sub>Mac Catalyst, macOS</sub>

```swift
struct NSEdgeInsets
```

## Overview

Edge insets describe the distance between the edges of one rectangle to a related rectangle that can be described by measuring a constant but edge-specific distance from each edge.

A common use for this structure is to describe the relationship between a view’s frame and its alignment rectangle.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an edge insets structure

- [init(top:left:bottom:right:)](<nsedgeinsets/init(top_left_bottom_right_).md>) — Creates an edge insets structure with the specified inset values.
- [NSEdgeInsetsMake](<nsedgeinsetsmake(________).md>) — Creates an edge insets structure with the specified inset values.
- [init()](<nsedgeinsets/init().md>) — Creates an edge insets structure.

### Specifying the edge insets

- [bottom](nsedgeinsets/bottom.md) — The distance from the bottom of the source rectangle to the bottom of the result rectangle.
- [left](nsedgeinsets/left.md) — The distance from the left side of the source rectangle to the left side of the result rectangle.
- [right](nsedgeinsets/right.md) — The distance from the right side of the source rectangle to the right side of the result rectangle.
- [top](nsedgeinsets/top.md) — The distance from the top of the source rectangle to the top of the result rectangle.

### Comparing edge insets

- [NSEdgeInsetsEqual](<nsedgeinsetsequal(____).md>) — Returns a Boolean value that indicates whether two edge insets structures are equal.

### Getting the zero constant

- [NSEdgeInsetsZero](nsedgeinsetszero.md) — An edge insets structure with a zero inset on each edge.

## See Also

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSPoint](nspoint.md) — A point in a Cartesian coordinate system.
- [NSSize](nssize.md) — A two-dimensional size.
- [NSRect](nsrect.md) — A rectangle.
- [AffineTransform](affinetransform.md) — A graphics coordinate transformation.
