---
title: calloutOffset
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/calloutoffset
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/calloutoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/calloutoffset.json'
content_hash: 'sha256:3bbf764f1a0a4800'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# calloutOffset

<sub>Instance Property</sub>

The offset (in points) at which to place the callout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var calloutOffset: CGPoint { get set }
```

## Discussion

This property determines the additional distance by which to move the callout. When this property is `(0, 0)`, the map view places the anchor point of the callout on the top-center point of the annotation view’s frame. Specifying positive offset values moves the callout down and to the right, and specifying negative values moves it up and to the left.

MapKit doesn’t use the [calloutOffset](calloutoffset.md) property in macOS apps. Instead, macOS apps use [leftCalloutOffset](leftcalloutoffset.md) and [rightCalloutOffset](rightcalloutoffset.md).

## See Also

### Getting and setting attributes

- [enabled](isenabled.md) — A Boolean value that indicates whether the annotation is in an enabled state.
- [image](image.md) — The image the annotation view displays.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the map view highlights the annotation view.
- [annotation](annotation.md) — The annotation object associated with the view.
- [centerOffset](centeroffset.md) — The offset (in points) at which to display the view.
- [reuseIdentifier](reuseidentifier.md) — The string that identifies that the annotation view is reusable.
