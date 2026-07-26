---
title: alignmentMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/alignmentmode
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/alignmentmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/alignmentmode.json'
content_hash: 'sha256:478e4fc4a599e346'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# alignmentMode

<sub>Instance Property</sub>

Determines how individual lines of text are horizontally aligned within the receiver’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alignmentMode: CATextLayerAlignmentMode { get set }
```

## Discussion

The possible values are described in [Horizontal alignment modes](../horizontal-alignment-modes.md). Defaults to [kCAAlignmentNatural](../catextlayeralignmentmode/natural.md).

## See Also

### Text Alignment and Truncation

- [wrapped](iswrapped.md) — Determines whether the text is wrapped to fit within the receiver’s bounds.
- [truncationMode](truncationmode.md) — Determines how the text is truncated to fit within the receiver’s bounds.
