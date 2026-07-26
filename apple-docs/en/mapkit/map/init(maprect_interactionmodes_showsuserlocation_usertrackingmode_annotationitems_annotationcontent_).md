---
title: 'init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:)'
source_url: 'https://developer.apple.com/documentation/mapkit/map/init(maprect:interactionmodes:showsuserlocation:usertrackingmode:annotationitems:annotationcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map/init%28maprect%3Ainteractionmodes%3Ashowsuserlocation%3Ausertrackingmode%3Aannotationitems%3Aannotationcontent%3A%29.json'
content_hash: 'sha256:a0232d7d4afe7ab1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Map](../map.md)

# init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)

<sub>Initializer</sub>

Creates a map that displays a map rectangle with annotations, and optionally configures available interactions, user location, and tracking behavior.

> [!warning] Deprecated
> Use [Map](../map.md) initializers that take a [MapContentBuilder](../mapcontentbuilder.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Items, Annotation>(mapRect: Binding<MKMapRect>, interactionModes: MapInteractionModes = .all, showsUserLocation: Bool = false, userTrackingMode: Binding<MapUserTrackingMode>? = nil, annotationItems: Items, annotationContent: @escaping (Items.Element) -> Annotation) where Content == _DefaultAnnotatedMapContent<Items>, Items : RandomAccessCollection, Annotation : MapAnnotationProtocol, Items.Element : Identifiable
```

## Parameters

- `mapRect` — The map rectangle defining the area to display.

- `interactionModes` — An enumeration that indicates the user interactions to which the map responds.

- `showsUserLocation` — A Boolean value that indicates the option to display a person’s location on a map. The map displays the location only if they authorized the app to access their location.

- `userTrackingMode` — A binding to a tracking mode that determines how the map responds to location updates.

- `annotationItems` — The collection of data that the view uses to display annotations.

- `annotationContent` — A closure that produces the annotation content.

## See Also

### Initializers

- [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:)](<init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_).md>) — Creates a map that displays a coordinate region and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) — Creates a map that displays a coordinate region with annotations, and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:)](<init(maprect_interactionmodes_showsuserlocation_usertrackingmode_).md>) — Creates a map that displays a map rectangle and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
