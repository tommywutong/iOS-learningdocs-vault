---
title: MapContent
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcontent
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent.json'
content_hash: 'sha256:ca82f5fbba20ef8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapContent

<sub>Protocol</sub>

A protocol used to construct map content such as controls, markers, and annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol MapContent
```

## Relationships

- **Inherited By**: [DynamicMapContent](dynamicmapcontent.md)

- **Conforming Types**: [Annotation](annotation.md), [AnyMapContent](anymapcontent.md), [EmptyMapContent](emptymapcontent.md), [MapCircle](mapcircle.md), [MapPolygon](mappolygon.md), [MapPolyline](mappolyline.md), [Marker](marker.md), [TupleMapContent](tuplemapcontent.md), [UserAnnotation](userannotation.md)

## Topics

### Accessing the view body

- [body](mapcontent/body-swift.property.md) — The content and behavior of the view.

### Supplying annotation titles

- [annotationTitles(_:)](<mapcontent/annotationtitles(__).md>) — Sets the visibility of titles for markers and annotations.
- [annotationSubtitles(_:)](<mapcontent/annotationsubtitles(__).md>) — Sets the visibility of subtitles for markers and annotations.

### Setting the content style

- [foregroundStyle(_:)](<mapcontent/foregroundstyle(__).md>) — Specifies the shape style used to fill content in drawing map overlays.
- [tint(_:)](<mapcontent/tint(__).md>) — The tint shape style to apply to map content.

### Setting stroke properties

- [stroke(_:lineWidth:)](<mapcontent/stroke(__linewidth_).md>) — Applies the given shape style to drawn map overlays using the line width you specify.
- [stroke(_:style:)](<mapcontent/stroke(__style_).md>) — Applies the given shape style to drawn map overlays using the stroke style you specify.
- [stroke(lineWidth:)](<mapcontent/stroke(linewidth_).md>) — Applies the given stoke drawn map overlays using the line width you specify.
- [strokeStyle(style:)](<mapcontent/strokestyle(style_).md>) — Applies the given stroke style to drawn map overlays.

### Setting the overlay level

- [mapOverlayLevel(level:)](<mapcontent/mapoverlaylevel(level_).md>) — Specifies the position of overlays relative to other map content.

### Associated types

- [Body](mapcontent/body-swift.associatedtype.md) — The content and behavior of the view.

### Displaying place information

- [mapItemDetailSelectionAccessory(_:)](<mapcontent/mapitemdetailselectionaccessory(__).md>) — Specifies the selection accessory to display for the selected map item content.

### Instance Methods

- [tag(_:)](<mapcontent/tag(__).md>) — Sets the unique tag value of this piece of map content.

## See Also

### Protocols

- [DynamicMapContent](dynamicmapcontent.md) — A  type of view that generates views from an underlying collection of data.
- [MapContentBuilder](mapcontentbuilder.md) — A result builder that creates map content from closures you provide.
- [MapContentView](mapcontentview.md) — A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.
