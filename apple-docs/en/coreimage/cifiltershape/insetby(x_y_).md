---
title: 'insetBy(x:y:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltershape/insetby(x:y:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape/insetby(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape/insetby%28x%3Ay%3A%29.json'
content_hash: 'sha256:f56c6d23acc8f3a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterShape](../cifiltershape.md)

# insetBy(x:y:)

<sub>Instance Method</sub>

Modifies a filter shape object so that it is inset by the specified x and y values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insetBy(x dx: Int32, y dy: Int32) -> CIFilterShape
```

## Parameters

- `dx` — A value that specifies an inset in the x direction.

- `dy` — A value that specifies an inset in the y direction.

## See Also

### Modifying a Filter Shape

- [- intersectWith:](<intersect(with_)-8iw.md>) — Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [- intersectWithRect:](<intersect(with_)-2o2n8.md>) — Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [- transformBy:interior:](<transform(by_interior_).md>) — Creates a filter shape that results from applying a transform to the current filter shape.
- [- unionWith:](<union(with_)-52mnd.md>) — Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [- unionWithRect:](<union(with_)-75ebo.md>) — Creates a filter shape that results from the union of the current filter shape and a rectangle.
