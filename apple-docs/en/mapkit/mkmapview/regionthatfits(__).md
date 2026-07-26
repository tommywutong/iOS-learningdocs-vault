---
title: 'regionThatFits(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/regionthatfits(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/regionthatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/regionthatfits%28_%3A%29.json'
content_hash: 'sha256:e10e8be288ee6fe4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# regionThatFits(_:)

<sub>Instance Method</sub>

Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion
```

## Parameters

- `region` — The initial region whose span you want to adjust.

## Return Value

A region that is still centered on the same point of the map but whose span values are adjusted to fit in the map view’s frame.

## Discussion

You can use this method to normalize the region values before displaying them in the map. This method returns a new region that both contains the specified region and fits neatly inside the map view’s frame.

## See Also

### Adjusting map regions and rectangles

- [- mapRectThatFits:](<maprectthatfits(__).md>) — Returns a centered map rectangle with the same aspect ratio as the map view’s frame.
- [- mapRectThatFits:edgePadding:](<maprectthatfits(__edgepadding_).md>) — Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.
