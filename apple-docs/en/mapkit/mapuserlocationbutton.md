---
title: MapUserLocationButton
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapuserlocationbutton
source_url: 'https://developer.apple.com/documentation/mapkit/mapuserlocationbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapuserlocationbutton.json'
content_hash: 'sha256:14523459509b1169'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapUserLocationButton

<sub>Structure</sub>

A button that sets the framing of the associated map to the user location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct MapUserLocationButton
```

## Overview

Use `MapUserLocationButton` in conjunction with [Map](map.md) as a stand alone view, as shown in this example:

```swift
    struct LocationButtonTestView: View {
        @Namespace var mapScope
        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapUserLocationButton(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use `MapUserLocationButton` in conjunction with the `Map/mapControls(_:)` modifier as shown in this example:

```swift
    Map()
        .mapControls {
            MapUserLocationButton()
        }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map user location button

- [init(scope:)](<mapuserlocationbutton/init(scope_).md>) — Creates a new user location button with the scope you specify.

## See Also

### Map controls

- [MapCompass](mapcompass.md) — A view that reflects the current orientation of the associated map.
- [MapLocationCompass](maplocationcompass.md) — A view that displays a combined user location button and map compass.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapPitchToggle](mappitchtoggle.md) — A button that sets the pitch of the associated map.
- [MapScaleView](mapscaleview.md) — Displays a legend with distance information for the associated map.
- [MapZoomStepper](mapzoomstepper.md) — Buttons a person uses to adjust the zoom level of the map.
