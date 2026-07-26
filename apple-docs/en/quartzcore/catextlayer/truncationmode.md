---
title: truncationMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/truncationmode
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/truncationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/truncationmode.json'
content_hash: 'sha256:05a9743dcae5580b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# truncationMode

<sub>Instance Property</sub>

Determines how the text is truncated to fit within the receiver’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var truncationMode: CATextLayerTruncationMode { get set }
```

## Discussion

The possible values are described in [Truncation modes](../truncation-modes.md). Defaults to [kCATruncationNone](../catextlayertruncationmode/none.md).

## See Also

### Text Alignment and Truncation

- [wrapped](iswrapped.md) — Determines whether the text is wrapped to fit within the receiver’s bounds.
- [alignmentMode](alignmentmode.md) — Determines how individual lines of text are horizontally aligned within the receiver’s bounds.
