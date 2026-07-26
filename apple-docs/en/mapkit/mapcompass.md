---
title: MapCompass
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcompass
source_url: 'https://developer.apple.com/documentation/mapkit/mapcompass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcompass.json'
content_hash: 'sha256:e04da45750796555'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCompass

<sub>Structure</sub>

A view that reflects the current orientation of the associated map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct MapCompass
```

## Overview

You can use `MapCompass` with a [Map](map.md) as a stand alone view, as shown in the following example:

```swift
    struct CompassButtonTestView: View {
        @Namespace var mapScope
        var body: some View {
        VStack {
                Map(scope: mapScope)
                MapCompass(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapCompass` with the `Map/mapControls(_:)`, modifier, as shown below:

```swift
    Map()
        .mapControls {
            MapCompass()
        }
```

Tapping the compass reorients the map so that North is at the top of the [Map](map.md) view.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map compass

- [init(scope:)](<mapcompass/init(scope_).md>) — Creates a new map compass with the scope you specify.

## See Also

### Map controls

- [MapLocationCompass](maplocationcompass.md) — A view that displays a combined user location button and map compass.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapPitchToggle](mappitchtoggle.md) — A button that sets the pitch of the associated map.
- [MapScaleView](mapscaleview.md) — Displays a legend with distance information for the associated map.
- [MapUserLocationButton](mapuserlocationbutton.md) — A button that sets the framing of the associated map to the user location.
- [MapZoomStepper](mapzoomstepper.md) — Buttons a person uses to adjust the zoom level of the map.
