---
title: hlg
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caedrmetadata/hlg
source_url: 'https://developer.apple.com/documentation/quartzcore/caedrmetadata/hlg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caedrmetadata/hlg.json'
content_hash: 'sha256:1735f28854094d73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEDRMetadata](../caedrmetadata.md)

# hlg

<sub>Type Property</sub>

Extended dynamic range (EDR) metadata for the Hybrid Log-Gamma (HLG) transfer function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class var hlg: CAEDRMetadata { get }
```

## Discussion

Your content should be scene referred and encoded with the ITU-R BT.2100-2 Hybrid Log Gamma (HLG) opto-electrical transfer function (OETF). The system applies the opto-optical transfer function (OOTF) based on peak display brightness and ambient lighting. If you’re rendering to a [CAMetalLayer](../cametallayer.md) with a linear colorspace (for floating point EDR layers), you must apply the HLG inverse OETF without normalization, to provide a nominal range of `[0, 12]`.

For more information on HLG, see [https://www.itu.int/rec/R-REC-BT.2100](https://www.itu.int/rec/R-REC-BT.2100).
