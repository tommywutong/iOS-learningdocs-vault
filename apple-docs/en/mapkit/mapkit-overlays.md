---
title: MapKit overlays
framework: MapKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapkit-overlays
source_url: 'https://developer.apple.com/documentation/mapkit/mapkit-overlays'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapkit-overlays.json'
content_hash: 'sha256:f40adcc907a034ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md) · [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)

# MapKit overlays

<sub>API Collection</sub>

Create overlays to highlight geographic regions or paths.

## Topics

### Samples

- [Displaying overlays on a map](displaying-overlays-on-a-map.md) — Add regions of layered content to a map view.
- [Displaying an updating path of a user’s location history](displaying-an-updating-path-of-a-user-s-location-history.md) — Continually update a MapKit overlay displaying the path a user travels.

### Circular overlays

- [MKCircle](mkcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MKCircleRenderer](mkcirclerenderer.md) — The visual representation of a circular overlay.

### Custom shape overlays

- [MKPolygon](mkpolygon.md) — A closed polygon overlay.
- [MKPolygonRenderer](mkpolygonrenderer.md) — The visual representation of a single polygon overlay.
- [MKMultiPolygon](mkmultipolygon.md) — A collection of multiple closed polygon overlays.
- [MKMultiPolygonRenderer](mkmultipolygonrenderer.md) — The visual representation of multiple polygon overlays.
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md) — The visual representation of a path-based overlay.

### Multiple segment lines

- [MKPolyline](mkpolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [MKGeodesicPolyline](mkgeodesicpolyline.md) — An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [MKMultiPolyline](mkmultipolyline.md) — A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [MKPolylineRenderer](mkpolylinerenderer.md) — A visual representation of any polyline overlay object.
- [MKMultiPolylineRenderer](mkmultipolylinerenderer.md) — A visual representation of multiple polyline overlay objects.
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md) — A visual representation of any polyline overlay object with a gradient.

### Tiled image overlays

- [MKTileOverlay](mktileoverlay.md) — An overlay that covers an area of the map with tiles of bitmap images.
- [MKTileOverlayRenderer](mktileoverlayrenderer.md) — The renderer for a tile overlay that handles the drawing of bitmap images on the map surface.

### Shared behavior

- [MKOverlay](mkoverlay.md) — An interface for associating content with a specific map region.
- [MKOverlayRenderer](mkoverlayrenderer.md) — The shared infrastructure for drawing overlays on the map surface.
- [MKShape](mkshape.md) — An abstract class that defines the basic properties for all shape-based overlay objects.
- [MKMultiPoint](mkmultipoint.md) — An abstract class that defines the common behavior that open and closed polygon overlays share.
- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_

## See Also

### Annotations and overlays

- [MapKit annotations](mapkit-annotations.md) — Create annotations to add indicators and additional details for specific locations on a map.
