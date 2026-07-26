---
title: 'transform(by:interior:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltershape/transform(by:interior:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape/transform(by:interior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape/transform%28by%3Ainterior%3A%29.json'
content_hash: 'sha256:f0232660b1208de6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterShape](../cifiltershape.md)

# transform(by:interior:)

<sub>Instance Method</sub>

Creates a filter shape that results from applying a transform to the current filter shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func transform(by m: CGAffineTransform, interior flag: Bool) -> CIFilterShape
```

## Parameters

- `m` — A transform.

- `flag` — `false` specifies that the new filter shape object can contain all the pixels in the transformed shape (and possibly some that are outside the transformed shape). `true` specifies that the new filter shape object can contain  a subset of the pixels in the transformed shape (but none of those outside the transformed shape).

## Return Value

The transformed filter shape object.

## See Also

### Modifying a Filter Shape

- [- insetByX:Y:](<insetby(x_y_).md>) — Modifies a filter shape object so that it is inset by the specified x and y values.
- [- intersectWith:](<intersect(with_)-8iw.md>) — Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [- intersectWithRect:](<intersect(with_)-2o2n8.md>) — Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [- unionWith:](<union(with_)-52mnd.md>) — Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [- unionWithRect:](<union(with_)-75ebo.md>) — Creates a filter shape that results from the union of the current filter shape and a rectangle.
