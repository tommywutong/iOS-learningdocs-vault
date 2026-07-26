---
title: levelsOfDetailBias
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catiledlayer/levelsofdetailbias
source_url: 'https://developer.apple.com/documentation/quartzcore/catiledlayer/levelsofdetailbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catiledlayer/levelsofdetailbias.json'
content_hash: 'sha256:c3c2b01aa68d48d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATiledLayer](../catiledlayer.md)

# levelsOfDetailBias

<sub>Instance Property</sub>

The number of magnified levels of detail for this layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var levelsOfDetailBias: Int { get set }
```

## Discussion

Defaults to 0. Each previous level of detail is twice the resolution of the later. For example, specifying a value of 2 means that the layer has two extra levels of detail: 2x and 4x.

## See Also

### Levels of detail

- [levelsOfDetail](levelsofdetail.md) — The number of levels of detail maintained by this layer.
