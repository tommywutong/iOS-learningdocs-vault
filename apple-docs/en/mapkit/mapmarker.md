---
title: MapMarker
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mapmarker
source_url: 'https://developer.apple.com/documentation/mapkit/mapmarker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapmarker.json'
content_hash: 'sha256:8cfaf21d5d998db0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapMarker

<sub>Structure</sub>

A balloon-shaped annotation used to indicate the location on a map.

> [!warning] Deprecated
> Use [Marker](marker.md) along with [Map](map.md) initializers that take a [MapContentBuilder](mapcontentbuilder.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapMarker
```

## Overview

Create a [Map](map.md) and display marker annotations by returning a view that conforms to [MapAnnotationProtocol](mapannotationprotocol.md), such as [MapMarker](mapmarker.md), from the trailing closure of [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) or [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(maprect_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>). Items you provide as a collection to the source annotations need to conform to [Identifiable](../swift/identifiable.md).

For example, the following code displays a map with a marker annotation:

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

struct PinAnnotationMapView: View {
    let place: IdentifiablePlace
    @State var region: MKCoordinateRegion

    var body: some View {
        Map(coordinateRegion: $region,
            annotationItems: [place])
        { place in
            MapMarker(coordinate: place.location,
                   tint: Color.purple)
        }
    }
}

```

## Relationships

- **Conforms To**: [MapAnnotationProtocol](mapannotationprotocol.md)

## Topics

### Creating a map marker

- [init(coordinate:tint:)](<mapmarker/init(coordinate_tint_).md>) — Creates a marker annotation at the map location you specify. _(deprecated)_

## See Also

### Structures

- [MapAnnotation](mapannotation.md) — A customizable annotation that marks a map location. _(deprecated)_
- [MapPin](mappin.md) — A pin-shaped annotation used to indicate a location on a map. _(deprecated)_
