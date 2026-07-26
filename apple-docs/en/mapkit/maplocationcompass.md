---
title: MapLocationCompass
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/maplocationcompass
source_url: 'https://developer.apple.com/documentation/mapkit/maplocationcompass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/maplocationcompass.json'
content_hash: 'sha256:164cb7ba39977809'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapLocationCompass

<sub>Structure</sub>

A view that displays a combined user location button and map compass.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency struct MapLocationCompass
```

## Overview

In watchOS 10 and later, this view displays a combined [MapUserLocationButton](mapuserlocationbutton.md) and [MapCompass](mapcompass.md) control. When the map camera has a heading of zero (where north is up), this view shows the user location button. When the map camera is in a rotated state, it shows a compass.

Use `MapLocationCompass` in conjunction with [Map](map.md) as a standalone view, as shown in this example:

```swift
    struct LocationCompassTestView: View {
        @Namespace var mapScope

        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapLocationCompass(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapLocationCompass` in conjunction with the `mapControls(_:)` modifier. For example:

```swift
    Map()
        .mapControls {
            MapLocationCompass()
        }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map loction compass

- [init(scope:)](<maplocationcompass/init(scope_).md>) — Creates a new map location compass with the provided scope.

## See Also

### Map controls

- [MapCompass](mapcompass.md) — A view that reflects the current orientation of the associated map.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapPitchToggle](mappitchtoggle.md) — A button that sets the pitch of the associated map.
- [MapScaleView](mapscaleview.md) — Displays a legend with distance information for the associated map.
- [MapUserLocationButton](mapuserlocationbutton.md) — A button that sets the framing of the associated map to the user location.
- [MapZoomStepper](mapzoomstepper.md) — Buttons a person uses to adjust the zoom level of the map.
