---
title: placement
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectelement/placement
source_url: 'https://developer.apple.com/documentation/photosui/phprojectelement/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectelement/placement.json'
content_hash: 'sha256:df91e412fc92f77d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectElement](../phprojectelement.md)

# placement

<sub>Instance Property</sub>

A rectangle defining where an element is placed in grid space coordinates.

<sub>macOS</sub>

```swift
var placement: CGRect { get }
```

## Discussion

For layout grids with more than one column, the values in the rectangle will always have integer value.  For fixed layouts, rectangle values will be in fractional unit values.

If suggested placement could not be determined at the time of project creation, the placement will contain [CGRectNull](../../coregraphics/cgrectnull.md).

For example, a rect of `(0,` `0,` `3,` `4)` represents a placement in the upper-left corner of the layout grid, with 3 grid units of width and 4 grid units of height.

## See Also

### Describing Project Elements

- [weight](weight.md) — A value between 0 and 1 representing relative significance of the element in its section.
