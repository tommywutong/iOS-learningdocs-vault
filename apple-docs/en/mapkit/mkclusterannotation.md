---
title: MKClusterAnnotation
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkclusterannotation
source_url: 'https://developer.apple.com/documentation/mapkit/mkclusterannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkclusterannotation.json'
content_hash: 'sha256:8aa54f4986437c81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKClusterAnnotation

<sub>Class</sub>

An annotation that groups two or more distinct annotations into a single entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKClusterAnnotation
```

## Overview

A cluster annotation object stands in for the group of annotations. Cluster views promote legibility of the underlying annotations by displaying a single annotation that takes it’s title from one annotation and includes a subtitle that indicates how many additional annotations belong to the group.

MapKit automatically creates cluster annotations when two or more annotation views group too closely together on the map surface. To customize the cluster annotations that display on your map, implement the [- mapView:clusterAnnotationForMemberAnnotations:](<mkmapviewdelegate/mapview(__clusterannotationformemberannotations_).md>) method in your map’s delegate.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a cluster annotation

- [- initWithMemberAnnotations:](<mkclusterannotation/init(memberannotations_).md>) — Creates a cluster annotation with the specified individual annotations.

### Getting the cluster attributes

- [title](mkclusterannotation/title.md) — The title string to display for the group of annotations.
- [subtitle](mkclusterannotation/subtitle.md) — The subtitle string to display for the group of annotations.

### Getting the annotations

- [memberAnnotations](mkclusterannotation/memberannotations.md) — The annotations that the cluster contains.

## See Also

### Grouped annotations

- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md) — Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
