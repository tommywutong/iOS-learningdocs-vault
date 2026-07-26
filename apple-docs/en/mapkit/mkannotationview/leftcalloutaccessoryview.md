---
title: leftCalloutAccessoryView
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/leftcalloutaccessoryview
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/leftcalloutaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/leftcalloutaccessoryview.json'
content_hash: 'sha256:63881d18b4820780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# leftCalloutAccessoryView

<sub>Instance Property</sub>

The view to display on the left side of the standard callout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leftCalloutAccessoryView: UIView? { get set }
```

<sub>macOS</sub>

```swift
var leftCalloutAccessoryView: NSView? { get set }
```

## Discussion

The default value of this property is `nil`. Typically, you use the left callout view to display information about the annotation or to link to custom information that your app provides.

In an iOS app, if the view you specify is also a descendant of the [UIControl](../../uikit/uicontrol.md) class, you can use the map view’s delegate to receive notifications when the user taps your control. If it doesn’t descend from [UIControl](../../uikit/uicontrol.md), your view is responsible for handling any touch events within its bounds.

In a macOS app, the callout view’s view controller can implement an action method that responds when the user clicks the control in a callout view.

## See Also

### Managing callout views

- [accessoryOffset](accessoryoffset.md) — An offset that changes the accessory’s default anchor point.
- [canShowCallout](canshowcallout.md) — A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [rightCalloutAccessoryView](rightcalloutaccessoryview.md) — The view to display on the right side of the standard callout.
- [detailCalloutAccessoryView](detailcalloutaccessoryview.md) — The detail accessory view to use in the standard callout.
- [leftCalloutOffset](leftcalloutoffset.md) — The offset in points from the middle-left of the annotation view.
- [rightCalloutOffset](rightcalloutoffset.md) — The offset in points from the middle-right of the annotation view.
