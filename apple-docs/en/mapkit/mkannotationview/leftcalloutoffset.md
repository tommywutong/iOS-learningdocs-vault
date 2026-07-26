---
title: leftCalloutOffset
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/leftcalloutoffset
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/leftcalloutoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/leftcalloutoffset.json'
content_hash: 'sha256:914e07efeaedb331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# leftCalloutOffset

<sub>Instance Property</sub>

The offset in points from the middle-left of the annotation view.

<sub>Mac Catalyst, macOS</sub>

```swift
var leftCalloutOffset: CGPoint { get set }
```

## Discussion

This property specifies where the map view shows the anchor of the callout when it orients off the left side of the annotation view.

## See Also

### Managing callout views

- [accessoryOffset](accessoryoffset.md) — An offset that changes the accessory’s default anchor point.
- [canShowCallout](canshowcallout.md) — A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [leftCalloutAccessoryView](leftcalloutaccessoryview.md) — The view to display on the left side of the standard callout.
- [rightCalloutAccessoryView](rightcalloutaccessoryview.md) — The view to display on the right side of the standard callout.
- [detailCalloutAccessoryView](detailcalloutaccessoryview.md) — The detail accessory view to use in the standard callout.
- [rightCalloutOffset](rightcalloutoffset.md) — The offset in points from the middle-right of the annotation view.
