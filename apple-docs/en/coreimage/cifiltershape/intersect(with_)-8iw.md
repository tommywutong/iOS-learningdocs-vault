---
title: 'intersect(with:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltershape/intersect(with:)-8iw'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape/intersect(with:)-8iw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape/intersect%28with%3A%29-8iw.json'
content_hash: 'sha256:f5ce745be2c5b9a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterShape](../cifiltershape.md)

# intersect(with:)

<sub>Instance Method</sub>

Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func intersect(with s2: CIFilterShape) -> CIFilterShape
```

## Parameters

- `s2` — A filter shape object.

## Return Value

The filter shape object that results from the intersection.

## See Also

### Modifying a Filter Shape

- [- insetByX:Y:](<insetby(x_y_).md>) — Modifies a filter shape object so that it is inset by the specified x and y values.
- [- intersectWithRect:](<intersect(with_)-2o2n8.md>) — Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [- transformBy:interior:](<transform(by_interior_).md>) — Creates a filter shape that results from applying a transform to the current filter shape.
- [- unionWith:](<union(with_)-52mnd.md>) — Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [- unionWithRect:](<union(with_)-75ebo.md>) — Creates a filter shape that results from the union of the current filter shape and a rectangle.
