---
title: canShowCallout
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/canshowcallout
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/canshowcallout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/canshowcallout.json'
content_hash: 'sha256:87fffd3c2f1964e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# canShowCallout

<sub>Instance Property</sub>

A Boolean value that indicates whether the annotation view is able to display extra information in a callout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canShowCallout: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the map view shows a standard callout  when the user taps a selected annotation view. The callout uses the title and subtitle text from the associated annotation object. If there’s no title text, the map view treats the annotation view as if its [enabled](isenabled.md) property is [false](../../swift/false.md). The callout also displays any custom callout views in the [leftCalloutAccessoryView](leftcalloutaccessoryview.md) and [rightCalloutAccessoryView](rightcalloutaccessoryview.md) properties.

If the value of this property is [false](../../swift/false.md), the map view ignores the value of the title and subtitle strings, and the annotation view remains in an enabled state by default. You can still disable the view explicitly using the [enabled](isenabled.md) property.

## See Also

### Managing callout views

- [accessoryOffset](accessoryoffset.md) — An offset that changes the accessory’s default anchor point.
- [leftCalloutAccessoryView](leftcalloutaccessoryview.md) — The view to display on the left side of the standard callout.
- [rightCalloutAccessoryView](rightcalloutaccessoryview.md) — The view to display on the right side of the standard callout.
- [detailCalloutAccessoryView](detailcalloutaccessoryview.md) — The detail accessory view to use in the standard callout.
- [leftCalloutOffset](leftcalloutoffset.md) — The offset in points from the middle-left of the annotation view.
- [rightCalloutOffset](rightcalloutoffset.md) — The offset in points from the middle-right of the annotation view.
