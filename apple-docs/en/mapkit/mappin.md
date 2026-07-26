---
title: MapPin
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（16.0 起废弃）, iPadOS 14.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 11.0+（13.0 起废弃）, tvOS 14.0+（16.0 起废弃）, visionOS, watchOS 7.0+（9.0 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mappin
source_url: 'https://developer.apple.com/documentation/mapkit/mappin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappin.json'
content_hash: 'sha256:ce5036be76c99cbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapPin

<sub>Structure</sub>

A pin-shaped annotation used to indicate a location on a map.

> [!warning] Deprecated
> Use [Marker](marker.md) along with [Map](map.md) initializers that take a [MapContentBuilder](mapcontentbuilder.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapPin
```

## Overview

Create a [Map](map.md) and display pin annotations by returning a view that conforms to [MapAnnotationProtocol](mapannotationprotocol.md), such as [MapPin](mappin.md), from the trailing closure of [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) or [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(maprect_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>). Items you provide as a collection to the source annotations need to conform to [Identifiable](../swift/identifiable.md).

For example, the following code displays a map with a pin annotation:

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
            MapPin(coordinate: place.location,
                   tint: Color.purple)
        }
    }
}
```

## Relationships

- **Conforms To**: [MapAnnotationProtocol](mapannotationprotocol.md)

## Topics

### Creating a map pin

- [init(coordinate:tint:)](<mappin/init(coordinate_tint_).md>) — Creates a map pin at the map location that you specify. _(deprecated)_
