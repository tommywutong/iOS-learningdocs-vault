---
title: Marker
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/marker
source_url: 'https://developer.apple.com/documentation/mapkit/marker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/marker.json'
content_hash: 'sha256:5737554394b35145'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# Marker

<sub>Structure</sub>

A balloon-shaped annotation that marks a map location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Marker<Label> where Label : View
```

## Overview

Use this view to create marker instances in the closure you provide to the `content` parameter in the [Map](map.md) initializers.

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a marker

- [init(_:coordinate:)](<marker/init(__coordinate_)-82942.md>) — Creates a marker at the given location with the label you provide.
- [init(_:image:coordinate:)](<marker/init(__image_coordinate_)-36l1p.md>) — Creates a marker at the given location with the provided title and image resource to display as the balloon’s icon.
- [init(_:systemImage:coordinate:)](<marker/init(__systemimage_coordinate_)-50yl4.md>) — Creates a marker at the given location with the provided title and a system image the map displays as the balloon’s icon.
- [init(_:coordinate:)](<marker/init(__coordinate_)-8wxlv.md>) — Creates a marker at the given location with the localized string key you provide.
- [init(_:image:coordinate:)](<marker/init(__image_coordinate_)-28mge.md>) — Creates a marker at the given location with the provided localized title and image resource to display as the balloon’s icon.
- [init(_:monogram:coordinate:)](<marker/init(__monogram_coordinate_)-2ojcy.md>) — Creates a marker at the given location with the provided title key and monogram.
- [init(_:monogram:coordinate:)](<marker/init(__monogram_coordinate_)-21hql.md>) — Creates a marker at the given location with the provided title string and monogram.
- [init(_:systemImage:coordinate:)](<marker/init(__systemimage_coordinate_)-2t4i0.md>) — Creates a marker at the given location with a localized title, and a system image the map displays as the balloon’s icon.
- [init(coordinate:label:)](<marker/init(coordinate_label_).md>) — Creates a marker at the given location with the provided label.
- [init(item:)](<marker/init(item_).md>) — Creates a marker for a given map item using a MapKit-provided label.

### Displaying place information

- [mapItemDetailSelectionAccessory(_:)](<mapcontent/mapitemdetailselectionaccessory(__).md>) — Specifies the selection accessory to display for the selected map item content.

### Initializers

- [init(_:coordinate:)](<marker/init(__coordinate_)-3bjj6.md>) — Creates a marker at the given location.
- [init(_:image:coordinate:)](<marker/init(__image_coordinate_)-1q3pz.md>) — Creates a marker at the given location with an image displayed as the balloon’s icon.
- [init(_:monogram:coordinate:)](<marker/init(__monogram_coordinate_)-77k4r.md>) — Creates a marker at the given location with a monogram displayed as the balloon’s icon.
- [init(_:systemImage:coordinate:)](<marker/init(__systemimage_coordinate_)-18xnl.md>) — Creates a marker at the given location with a system image displayed as the balloon’s icon.

## See Also

### Annotations and overlays

- [Annotation](annotation.md) — A customizable annotation used to indicate a location on a map.
- [MapCircle](mapcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MapPolygon](mappolygon.md) — A closed polygon overlay.
- [MapPolyline](mappolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [UserAnnotation](userannotation.md) — Displays the person’s current location on the map.
