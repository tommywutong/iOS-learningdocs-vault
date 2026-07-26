---
title: 'union(with:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltershape/union(with:)-75ebo'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape/union(with:)-75ebo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape/union%28with%3A%29-75ebo.json'
content_hash: 'sha256:f1a4a348bc3aca7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterShape](../cifiltershape.md)

# union(with:)

<sub>Instance Method</sub>

Creates a filter shape that results from the union of the current filter shape and a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func union(with r: CGRect) -> CIFilterShape
```

## Parameters

- `r` — A rectangle. Core Image uses the rectangle specified by integer parts of the width and height.

## See Also

### Modifying a Filter Shape

- [- insetByX:Y:](<insetby(x_y_).md>) — Modifies a filter shape object so that it is inset by the specified x and y values.
- [- intersectWith:](<intersect(with_)-8iw.md>) — Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [- intersectWithRect:](<intersect(with_)-2o2n8.md>) — Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [- transformBy:interior:](<transform(by_interior_).md>) — Creates a filter shape that results from applying a transform to the current filter shape.
- [- unionWith:](<union(with_)-52mnd.md>) — Creates a filter shape that results from the union of the current filter shape and another filter shape object.
