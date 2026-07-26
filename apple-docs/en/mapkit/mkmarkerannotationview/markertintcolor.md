---
title: markerTintColor
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmarkerannotationview/markertintcolor
source_url: 'https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/markertintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmarkerannotationview/markertintcolor.json'
content_hash: 'sha256:7a897a5c17cfad6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMarkerAnnotationView](../mkmarkerannotationview.md)

# markerTintColor

<sub>Instance Property</sub>

The background color of the marker balloon.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var markerTintColor: UIColor? { get set }
```

<sub>macOS</sub>

```swift
@NSCopying var markerTintColor: NSColor? { get set }
```

## Discussion

The default value of this property is `nil`, which applies the standard color that’s appropriate for the current map style.
