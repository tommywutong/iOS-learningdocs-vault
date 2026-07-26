---
title: MKOverlay
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlay
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlay.json'
content_hash: 'sha256:9c51035f156c4e9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKOverlay

<sub>Protocol</sub>

An interface for associating content with a specific map region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MKOverlay : MKAnnotation
```

## Overview

_Overlay objects_ are data objects that define the geographic data to cover. MapKit defines several concrete classes that adopt this protocol and define standard shapes like rectangles, circles, and polygons. You might use overlays to define the geographic boundaries of a national park or trace a bus route along city streets. You add an overlay to your map view by calling its [- addOverlay:](<mkmapview/addoverlay(__).md>) method or any other map view method for adding overlays to the map. When the overlay’s region intersects the visible portion of the map, the map view calls the [- mapView:rendererForOverlay:](<mkmapviewdelegate/mapview(__rendererfor_).md>) method of its delegate to obtain the renderer object responsible for drawing the overlay.

If you add an overlay to a map view as an annotation, instead of adding it as an overlay, the map view treats your overlay as an annotation. Specifically, it displays your overlay only when its [coordinate](mkoverlay/coordinate.md) is in the visible map region, rather than displaying the overlay when any portion of its covered area is visible.

## Relationships

- **Inherits From**: [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [MKCircle](mkcircle.md), [MKGeodesicPolyline](mkgeodesicpolyline.md), [MKMultiPolygon](mkmultipolygon.md), [MKMultiPolyline](mkmultipolyline.md), [MKPolygon](mkpolygon.md), [MKPolyline](mkpolyline.md), [MKTileOverlay](mktileoverlay.md)

## Topics

### Describing the overlay geometry

- [coordinate](mkoverlay/coordinate.md) — The approximate center point of the overlay area.
- [boundingMapRect](mkoverlay/boundingmaprect.md) — The projected rectangle that encompasses the overlay.

### Determining map intersections

- [- intersectsMapRect:](<mkoverlay/intersects(__).md>) — Returns a Boolean value that indicates whether the specified rectangle intersects the overlay’s shape.

### Optimizing map rendering

- [- canReplaceMapContent](<mkoverlay/canreplacemapcontent().md>) — Returns a Boolean value that indicates whether the overlay content replaces the underlying map content.

## See Also

### Shared behavior

- [MKOverlayRenderer](mkoverlayrenderer.md) — The shared infrastructure for drawing overlays on the map surface.
- [MKShape](mkshape.md) — An abstract class that defines the basic properties for all shape-based overlay objects.
- [MKMultiPoint](mkmultipoint.md) — An abstract class that defines the common behavior that open and closed polygon overlays share.
- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
