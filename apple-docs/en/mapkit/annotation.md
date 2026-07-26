---
title: Annotation
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/annotation
source_url: 'https://developer.apple.com/documentation/mapkit/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation.json'
content_hash: 'sha256:504fc06434641832'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# Annotation

<sub>Structure</sub>

A customizable annotation used to indicate a location on a map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Annotation<Label, Content> where Label : View, Content : View
```

## Overview

Use this view to annotations in the closure you provide to the `content` parameter in the [Map](map.md) initializers.

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating annotations

- [init(_:coordinate:anchor:accessoryAnchor:content:)](<annotation/init(__coordinate_anchor_accessoryanchor_content_)-6rxmn.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:accessoryAnchor:content:)](<annotation/init(__coordinate_anchor_accessoryanchor_content_)-14m3t.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate:anchor:accessoryAnchor:content:label:)](<annotation/init(coordinate_anchor_accessoryanchor_content_label_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(item:anchor:accessoryAnchor:content:)](<annotation/init(item_anchor_accessoryanchor_content_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<annotation/init(__coordinate_anchor_content_)-2w242.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<annotation/init(__coordinate_anchor_content_)-6wnoh.md>) — Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate:anchor:content:label:)](<annotation/init(coordinate_anchor_content_label_).md>) — Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.

### Displaying place information

- [mapItemDetailSelectionAccessory(_:)](<mapcontent/mapitemdetailselectionaccessory(__).md>) — Specifies the selection accessory to display for the selected map item content.

### Initializers

- [init(_:coordinate:anchor:accessoryAnchor:content:)](<annotation/init(__coordinate_anchor_accessoryanchor_content_)-8wi4r.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<annotation/init(__coordinate_anchor_content_)-8k419.md>) — Creates an annotation that displays a view at a coordinate on the map.

## See Also

### Annotations and overlays

- [MapCircle](mapcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MapPolygon](mappolygon.md) — A closed polygon overlay.
- [MapPolyline](mappolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [Marker](marker.md) — A balloon-shaped annotation that marks a map location.
- [UserAnnotation](userannotation.md) — Displays the person’s current location on the map.
