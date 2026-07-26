---
title: MapScaleView
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapscaleview
source_url: 'https://developer.apple.com/documentation/mapkit/mapscaleview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapscaleview.json'
content_hash: 'sha256:f83a10191c3cf465'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapScaleView

<sub>Structure</sub>

Displays a legend with distance information for the associated map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct MapScaleView
```

## Overview

You can use this with [Map](map.md) as a standalone view, for example:

```swift
    struct ScaleTestView: View {
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

The scale indicator grows and shrinks (although visually, its frame is static) based on the zoom level of the map. By default the leading edge remains anchored and the trailing edge moves as the scale changes. If the scale is trailing aligned, then it may be more visually appealing to anchor the `ScaleView` to the trailing edge

```swift
    ZStack(alignment: .trailing) {
        Map(mapScope)
        MapScaleView(anchorEdge: .trailing, scope: mapScope)
    }
    .mapScope(mapScope)
```

You can also use `MapScaleView` with the [mapControls(_:)](<../swiftui/view/mapcontrols(__).md>) modifier, as shown in this example:

```swift
    Map()
        .mapControls {
            MapScaleView()
        }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map scale view

- [init(anchorEdge:scope:)](<mapscaleview/init(anchoredge_scope_).md>) — Creates a map scale view.
- [init(alignment:scope:)](<mapscaleview/init(alignment_scope_).md>) — Creates a scale view with the provided alignment and scope.

## See Also

### Map controls

- [MapCompass](mapcompass.md) — A view that reflects the current orientation of the associated map.
- [MapLocationCompass](maplocationcompass.md) — A view that displays a combined user location button and map compass.
- [MapPitchSlider](mappitchslider.md) — A slider control that allows a person to change the pitch of the map.
- [MapPitchToggle](mappitchtoggle.md) — A button that sets the pitch of the associated map.
- [MapUserLocationButton](mapuserlocationbutton.md) — A button that sets the framing of the associated map to the user location.
- [MapZoomStepper](mapzoomstepper.md) — Buttons a person uses to adjust the zoom level of the map.
