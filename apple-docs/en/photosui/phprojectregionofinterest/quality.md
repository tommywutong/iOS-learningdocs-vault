---
title: quality
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectregionofinterest/quality
source_url: 'https://developer.apple.com/documentation/photosui/phprojectregionofinterest/quality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectregionofinterest/quality.json'
content_hash: 'sha256:c19e45ae7efea883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectRegionOfInterest](../phprojectregionofinterest.md)

# quality

<sub>Instance Property</sub>

The region’s quality.

<sub>macOS</sub>

```swift
var quality: Double { get }
```

## Discussion

The `quality` score represents the quality of the region of interest in the individual asset, based on factors like sharpness, visibility, and prominence in the photo. Values range from `0` to `1`, with a default of `0.5`. Different regions of interest with the same identifier may have different quality values. If a project must choose between multiple assets containing the same region of interest, use the `quality` metric to choose the best representative.

![Two photos containing the same human faces, one with low quality, the other with high quality](../../../../attachments/7b13fcda86924d353836b16944918927/media-3030183@2x.png)

## See Also

### Determining Region Properties

- [rect](rect.md) — The rectangle representing the region’s location.
- [identifier](identifier-swift.property.md) — The region’s unique identifier.
- [weight](weight.md) — The face region’s weight.
