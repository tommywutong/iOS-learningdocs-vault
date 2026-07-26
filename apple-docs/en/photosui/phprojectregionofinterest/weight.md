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
doc_path: /documentation/photosui/phprojectregionofinterest/weight
source_url: 'https://developer.apple.com/documentation/photosui/phprojectregionofinterest/weight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectregionofinterest/weight.json'
content_hash: 'sha256:92d22267996d6960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectRegionOfInterest](../phprojectregionofinterest.md)

# weight

<sub>Instance Property</sub>

The face region’s weight.

<sub>macOS</sub>

```swift
var weight: Double { get }
```

## Discussion

The `weight` of a region of interest represents the pervasiveness of the face across the project as a whole. All regions of interest with the same identifier share the same weight. The values range between `0` and `1`. The default value is `0.5`.

![Four photos containing five different human faces, each showing up at different frequencies](../../../../attachments/ee24c6eb22f3a18f06c58a8cd6641f6d/media-3030188@2x.png)

For projects focused on animation or transition between assets, focus on the regions with the highest weight to ensure that your presentation features areas of greatest interest to the user.

## See Also

### Determining Region Properties

- [rect](rect.md) — The rectangle representing the region’s location.
- [identifier](identifier-swift.property.md) — The region’s unique identifier.
- [quality](quality.md) — The region’s quality.
