---
title: none
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayertruncationmode/none
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayertruncationmode/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayertruncationmode/none.json'
content_hash: 'sha256:0308ddc18ae4f9d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayerTruncationMode](../catextlayertruncationmode.md)

# none

<sub>Type Property</sub>

Each line is displayed so that the text is either wrapped or clipped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let none: CATextLayerTruncationMode
```

## Discussion

If the [wrapped](../catextlayer/iswrapped.md) property is [true](../../swift/true.md), the text is wrapped to the receiver’s bounds, otherwise the text is clipped to the receiver’s bounds.

## See Also

### Constants

- [kCATruncationStart](start.md) — Each line is displayed so that the end fits in the container and the missing text is indicated by some kind of ellipsis glyph.
- [kCATruncationEnd](end.md) — Each line is displayed so that the beginning fits in the container and the missing text is indicated by some kind of ellipsis glyph.
- [kCATruncationMiddle](middle.md) — Each line is displayed so that the beginning and end fit in the container and the missing text is indicated by some kind of ellipsis glyph in the middle.
