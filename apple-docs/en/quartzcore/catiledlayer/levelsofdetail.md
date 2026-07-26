---
title: levelsOfDetail
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catiledlayer/levelsofdetail
source_url: 'https://developer.apple.com/documentation/quartzcore/catiledlayer/levelsofdetail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catiledlayer/levelsofdetail.json'
content_hash: 'sha256:f7a43fae44d2d336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATiledLayer](../catiledlayer.md)

# levelsOfDetail

<sub>Instance Property</sub>

The number of levels of detail maintained by this layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var levelsOfDetail: Int { get set }
```

## Discussion

Defaults to 1. Each level of detail is half the resolution of the previous level. If too many levels are specified for the current size of the layer, then the number of levels is clamped to the maximum value (the bottom most level of detail must contain at least a single pixel in each dimension.)

## See Also

### Levels of detail

- [levelsOfDetailBias](levelsofdetailbias.md) — The number of magnified levels of detail for this layer.
