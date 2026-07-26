---
title: clusteringIdentifier
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/clusteringidentifier
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/clusteringidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/clusteringidentifier.json'
content_hash: 'sha256:15af15b8902957cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# clusteringIdentifier

<sub>Instance Property</sub>

An identifier that determines whether the annotation view participates in clustering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var clusteringIdentifier: String? { get set }
```

## Discussion

The default value of this property is `nil`, which prevents MapKit from clustering the annotation view with other annotation views. Setting the property to a non-`nil` value enables it to participate in clustering.

Clustering occurs when there’s a collision between multiple annotation views with the same identifier on the map surface. MapKit removes the annotation views involved in the collision from the map view and replaces them with a clustering annotation view, which displays the title from one of the annotations and provides access to the other annotations.

## See Also

### Clustering annotation views

- [Decluttering a Map with MapKit Annotation Clustering](../decluttering-a-map-with-mapkit-annotation-clustering.md) — Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [clusterAnnotationView](cluster.md) — The clustering annotation view that replaces the annotation view.
