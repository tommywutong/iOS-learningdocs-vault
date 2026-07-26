---
title: delegate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/delegate
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/delegate.json'
content_hash: 'sha256:69a84dee66c8eb1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@IBOutlet weak var delegate: (any MKMapViewDelegate)? { get set }
```

## Discussion

A map view sends messages to its delegate regarding the loading of map data and changes in the portion of the map it displays. The delegate also manages the annotation views that highlight points of interest on the map.

The delegate needs to implement the methods of the [MKMapViewDelegate](../mkmapviewdelegate.md) protocol.

## See Also

### Customizing the map view behavior

- [MKMapViewDelegate](../mkmapviewdelegate.md) — Optional methods that you use to receive map-related update messages.
