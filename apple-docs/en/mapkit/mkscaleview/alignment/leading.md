---
title: MKScaleView.Alignment.leading
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkscaleview/alignment/leading
source_url: 'https://developer.apple.com/documentation/mapkit/mkscaleview/alignment/leading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkscaleview/alignment/leading.json'
content_hash: 'sha256:78b2eeb1d8d56905'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKScaleView](../../mkscaleview.md) · [Alignment](../alignment.md)

# MKScaleView.Alignment.leading

<sub>Case</sub>

Scale measurements begin at the leading edge of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case leading
```

## Discussion

This value causes the scale view to place the value `0` at the leading edge of the view. The scale view places the distance representing the current scale of the map at the trailing edge of the view.

## See Also

### Alignment options

- [MKScaleViewAlignmentTrailing](trailing.md) — Scale measurements begin at the trailing edge of the view.
- [MKScaleViewAlignmentCenter](center.md) — Scale measurements appear horizontally centered within the view.
