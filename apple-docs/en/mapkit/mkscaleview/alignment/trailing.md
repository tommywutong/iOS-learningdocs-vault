---
title: MKScaleView.Alignment.trailing
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkscaleview/alignment/trailing
source_url: 'https://developer.apple.com/documentation/mapkit/mkscaleview/alignment/trailing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkscaleview/alignment/trailing.json'
content_hash: 'sha256:c0da208c3b3a507f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKScaleView](../../mkscaleview.md) · [Alignment](../alignment.md)

# MKScaleView.Alignment.trailing

<sub>Case</sub>

Scale measurements begin at the trailing edge of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case trailing
```

## Discussion

This value causes the scale view to place the value `0` at the trailing edge of the view. The scale places the distance representing the current scale of the map at the leading edge of the view.

## See Also

### Alignment options

- [MKScaleViewAlignmentLeading](leading.md) — Scale measurements begin at the leading edge of the view.
- [MKScaleViewAlignmentCenter](center.md) — Scale measurements appear horizontally centered within the view.
