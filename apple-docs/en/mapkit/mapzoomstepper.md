---
title: MapZoomStepper
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 14.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapzoomstepper
source_url: 'https://developer.apple.com/documentation/mapkit/mapzoomstepper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapzoomstepper.json'
content_hash: 'sha256:3cae098a13d7b27f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapZoomStepper

<sub>Structure</sub>

Buttons a person uses to adjust the zoom level of the map.

<sub>Mac Catalyst, macOS</sub>

```swift
@MainActor @preconcurrency struct MapZoomStepper
```

## Overview

You typically use [MapZoomStepper](mapzoomstepper.md) with [Map](map.md) as a stand alone view, as shown in the following example:

```swift
    struct ZoomStepperTestView: View {
        @Namespace var mapScope
        var body: some View {
            VStack {
                Map(scope: mapScope)
                MapZoomStepper(scope: mapScope)
            }
            .mapScope(mapScope)
        }
    }
```

You can also use a MapZoomStepper in conjunction with the `Map/mapControls(_:)` modifier, as show in here:

```swift
    Map()
        .mapControls {
            MapZoomStepper()
        }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a zoom stepper

- [init(scope:)](<mapzoomstepper/init(scope_).md>) — Creates a new zoom stepper with the scope you specify.

## See Also

### Map controls

- [MapCompass](mapcompass.md) — A view that reflects the current orientation of the associated map.
- [MapLocationCompass](maplocationcompass.md) — A view that displays a combined user location button and map compass.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapPitchToggle](mappitchtoggle.md) — A button that sets the pitch of the associated map.
- [MapScaleView](mapscaleview.md) — Displays a legend with distance information for the associated map.
- [MapUserLocationButton](mapuserlocationbutton.md) — A button that sets the framing of the associated map to the user location.
