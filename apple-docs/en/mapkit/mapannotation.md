---
title: MapAnnotation
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mapannotation
source_url: 'https://developer.apple.com/documentation/mapkit/mapannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapannotation.json'
content_hash: 'sha256:0e7d8a8740a62f6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapAnnotation

<sub>Structure</sub>

A customizable annotation that marks a map location.

> [!warning] Deprecated
> Use [Annotation](annotation.md) along with [Map](map.md) initializers that take a [MapContentBuilder](mapcontentbuilder.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapAnnotation<Content> where Content : View
```

## Overview

Use [MapAnnotation](mapannotation.md) to declare the layout of the view that MapKit uses for the annotation. Create a [Map](map.md) and display annotations by returning a view that conforms to [MapAnnotationProtocol](mapannotationprotocol.md) from the trailing closure of [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) or [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(maprect_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>). Items you provide as a collection to the source  annotations need to conform to [Identifiable](../swift/identifiable.md).

For example, the following code displays a map and a single annotation:

```swift
struct IdentifiablePlace: Identifiable {
    let id: UUID
    let location: CLLocationCoordinate2D
    init(id: UUID = UUID(), lat: Double, long: Double) {
        self.id = id
        self.location = CLLocationCoordinate2D(
            latitude: lat,
            longitude: long)
    }
}

struct CustomAnnotationMapView: View {
    let place: IdentifiablePlace
    @State var region: MKCoordinateRegion

    var body: some View {
        Map(coordinateRegion: $region,
            annotationItems: [place]
        ) { place in
            MapAnnotation(coordinate: place.location) {
                Rectangle().stroke(Color.blue)
                .frame(width: 20, height: 20)
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [MapAnnotationProtocol](mapannotationprotocol.md)

## Topics

### Creating a map annotation

- [init(coordinate:anchorPoint:content:)](<mapannotation/init(coordinate_anchorpoint_content_).md>) — Creates a custom annotation that provides a SwiftUI view to display at the map location that you specify. _(deprecated)_

## See Also

### Structures

- [MapMarker](mapmarker.md) — A balloon-shaped annotation used to indicate the location on a map. _(deprecated)_
- [MapPin](mappin.md) — A pin-shaped annotation used to indicate a location on a map. _(deprecated)_
