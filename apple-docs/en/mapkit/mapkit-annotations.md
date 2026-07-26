---
title: MapKit annotations
framework: MapKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapkit-annotations
source_url: 'https://developer.apple.com/documentation/mapkit/mapkit-annotations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapkit-annotations.json'
content_hash: 'sha256:64c5159bd8dc962c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md) · [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)

# MapKit annotations

<sub>API Collection</sub>

Create annotations to add indicators and additional details for specific locations on a map.

## Topics

### Location annotations

- [Annotating a Map with Custom Data](annotating-a-map-with-custom-data.md) — Annotate a map with location-specific data using default and customized annotation views and callouts.
- [MKPointAnnotation](mkpointannotation.md) — A string-based piece of location-specific data that you apply to a specific point on a map.
- [MKMapItemAnnotation](mkmapitemannotation.md) — An annotation that represents a map item
- [MKMarkerAnnotationView](mkmarkerannotationview.md) — An annotation view that displays a balloon-shaped marker at the designated location.
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_

### Grouped annotations

- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md) — Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [MKClusterAnnotation](mkclusterannotation.md) — An annotation that groups two or more distinct annotations into a single entity.

### User location

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [MKUserLocation](mkuserlocation.md) — An annotation that reflects the user’s location on the map.
- [MKUserLocationView](mkuserlocationview.md) — A configurable annotation that shows the user’s location using the default MapKit style.

### Annotations in SwiftUI

- [MapMarker](mapmarker.md) — A balloon-shaped annotation used to indicate the location on a map. _(deprecated)_
- [MapPin](mappin.md) — A pin-shaped annotation used to indicate a location on a map. _(deprecated)_
- [MapAnnotation](mapannotation.md) — A customizable annotation that marks a map location. _(deprecated)_
- [MapAnnotationProtocol](mapannotationprotocol.md) — A protocol that represents the possible return types of annotations.

### Shared behavior

- [MKPlacemark](mkplacemark.md) — A user-friendly description of a location on the map. _(deprecated)_
- [MKAnnotation](mkannotation.md) — An interface for associating your content with a specific map location.
- [MKAnnotationView](mkannotationview.md) — The visual representation of one of your annotation objects.

## See Also

### Annotations and overlays

- [MapKit overlays](mapkit-overlays.md) — Create overlays to highlight geographic regions or paths.
