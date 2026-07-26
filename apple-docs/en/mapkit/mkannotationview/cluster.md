---
title: cluster
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/cluster
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/cluster'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/cluster.json'
content_hash: 'sha256:997535c1e015621d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# cluster

<sub>Instance Property</sub>

The clustering annotation view that replaces the annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var cluster: MKAnnotationView? { get }
```

## Discussion

When the map is displaying this annotation view, the value of this property is `nil`.

## See Also

### Clustering annotation views

- [Decluttering a Map with MapKit Annotation Clustering](../decluttering-a-map-with-mapkit-annotation-clustering.md) — Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [clusteringIdentifier](clusteringidentifier.md) — An identifier that determines whether the annotation view participates in clustering.
