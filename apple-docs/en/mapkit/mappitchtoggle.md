---
title: MapPitchToggle
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mappitchtoggle
source_url: 'https://developer.apple.com/documentation/mapkit/mappitchtoggle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappitchtoggle.json'
content_hash: 'sha256:969f2a5af3880975'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapPitchToggle

<sub>Structure</sub>

A button that sets the pitch of the associated map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct MapPitchToggle
```

## Overview

The `MapPitchToggle` control sets the pitch of the associated map to a pleasing angle if flat, or returns the map to flat if pitched.

You can use this control in conjunction with [Map](map.md) as a standalone view, as this example shows:

```swift
    struct MyMapView: View {
        @Namespace var mapScope

        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapPitchToggle(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

Alternatively, use `MapPitchToggle` in conjunction with the `mapControls(_:)` modifier. For example:

```swift
    Map()
        .mapControls {
            MapPitchToggle()
        }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map pitch toggle

- [init(scope:)](<mappitchtoggle/init(scope_).md>) — Creates a new map pitch toggle control with the provided scope.

## See Also

### Map controls

- [MapCompass](mapcompass.md) — A view that reflects the current orientation of the associated map.
- [MapLocationCompass](maplocationcompass.md) — A view that displays a combined user location button and map compass.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapScaleView](mapscaleview.md) — Displays a legend with distance information for the associated map.
- [MapUserLocationButton](mapuserlocationbutton.md) — A button that sets the framing of the associated map to the user location.
- [MapZoomStepper](mapzoomstepper.md) — Buttons a person uses to adjust the zoom level of the map.
