---
title: weight
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectelement/weight
source_url: 'https://developer.apple.com/documentation/photosui/phprojectelement/weight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectelement/weight.json'
content_hash: 'sha256:c415c6a7a2a96a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectElement](../phprojectelement.md)

# weight

<sub>Instance Property</sub>

A value between 0 and 1 representing relative significance of the element in its section.

<sub>macOS</sub>

```swift
var weight: Double { get }
```

## Discussion

Values range from `0.0` to `1.0` where a higher number represents higher overall significance within the project section. The default value is `0.5`.

Projects that allow a user to reduce the number of elements in a section can use this hint to determine which elements are most important to preserving context.

## See Also

### Describing Project Elements

- [placement](placement.md) — A rectangle defining where an element is placed in grid space coordinates.
