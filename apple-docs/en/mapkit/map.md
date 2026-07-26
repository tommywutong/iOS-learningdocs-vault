---
title: Map
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/map
source_url: 'https://developer.apple.com/documentation/mapkit/map'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map.json'
content_hash: 'sha256:834e6a7459fb623a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# Map

<sub>Structure</sub>

A view that displays an embedded map interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Map<Content> where Content : View
```

## Overview

Use this SwiftUI view to display a `Map` with markers, annotations, and custom content you provide. You can configure the `Map` to optionally display the user’s location, track a location, and display various controls to allow them to interact with and control the map’s display. The following example displays a map of downtown San Francisco that shows different markers, and an annotation with custom view content at specific locations:

```swift
    struct ContentView: View {
        var body: some View {
            Map {
                Marker("San Francisco City Hall", coordinate: cityHallLocation)
                    .tint(.orange)
                Marker("San Francisco Public Library", coordinate: publicLibraryLocation)
                    .tint(.blue)
                Annotation("Diller Civic Center Playground", coordinate: playgroundLocation) {
                    ZStack {
                        RoundedRectangle(cornerRadius: 5)
                            .fill(Color.yellow)
                        Text("🛝")
                            .padding(5)
                    }
                }
            }
            .mapControlVisibility(.hidden)
        }
    }
```

You create markers, annotations, and overlays using [MapContentBuilder](mapcontentbuilder.md) with any of several [MapContent](mapcontent.md) types including:

- [Annotation](annotation.md)
- [UserAnnotation](userannotation.md)
- [Marker](marker.md)
- [MapCircle](mapcircle.md)
- [MapPolygon](mappolygon.md)
- [MapPolyline](mappolyline.md)

You can also add a variety of controls to allow a person to interact with the map to change the map’s scale, display or hide the device’s current location, and so on:

- [MapCompass](mapcompass.md)
- `MapPitchButton`
- [MapPitchSlider](mappitchslider.md)
- [MapScaleView](mapscaleview.md)
- [MapUserLocationButton](mapuserlocationbutton.md)
- [MapZoomStepper](mapzoomstepper.md)

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a map

- [init(bounds:interactionModes:scope:)](<map/init(bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init(bounds:interactionModes:scope:content:)](<map/init(bounds_interactionmodes_scope_content_).md>) — Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds:interactionModes:selection:scope:)](<map/init(bounds_interactionmodes_selection_scope_)-11lec.md>) — Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:)](<map/init(bounds_interactionmodes_selection_scope_)-236di.md>) — Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<map/init(bounds_interactionmodes_selection_scope_content_)-28wns.md>) — Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<map/init(bounds_interactionmodes_selection_scope_content_)-2tdbr.md>) — Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:scope:)](<map/init(initialposition_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(initialPosition:bounds:interactionModes:scope:content:)](<map/init(initialposition_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_content_)-9feos.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_content_)-451vp.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position:bounds:interactionModes:scope:)](<map/init(position_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(position:bounds:interactionModes:scope:content:)](<map/init(position_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:)](<map/init(position_bounds_interactionmodes_selection_scope_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:content:)](<map/init(position_bounds_interactionmodes_selection_scope_content_)-47y4p.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:content:)](<map/init(position_bounds_interactionmodes_selection_scope_content_)-9xq1q.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
- [MapInteractionModes](mapinteractionmodes.md) — Options that indicate the user interactions that the map responds to.

### Deprecated

- [Deprecated Symbols](deprecated-symbols.md) — Map protocols and view modifiers that are no longer supported.

### Displaying place information

- [mapItemDetailSelectionAccessory(_:)](<mapcontent/mapitemdetailselectionaccessory(__).md>) — Specifies the selection accessory to display for the selected map item content.

### Initializers

- [init(bounds:interactionModes:selection:scope:content:)](<map/init(bounds_interactionmodes_selection_scope_content_)-335qt.md>)
- [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:)](<map/init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_).md>) — Creates a map that displays a coordinate region and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(coordinateRegion:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(coordinateregion_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) — Creates a map that displays a coordinate region with annotations, and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_content_)-2u4ry.md>)
- [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:)](<map/init(maprect_interactionmodes_showsuserlocation_usertrackingmode_).md>) — Creates a map that displays a map rectangle and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(mapRect:interactionModes:showsUserLocation:userTrackingMode:annotationItems:annotationContent:)](<map/init(maprect_interactionmodes_showsuserlocation_usertrackingmode_annotationitems_annotationcontent_).md>) — Creates a map that displays a map rectangle with annotations, and optionally configures available interactions, user location, and tracking behavior. _(deprecated)_
- [init(position:bounds:interactionModes:selection:scope:content:)](<map/init(position_bounds_interactionmodes_selection_scope_content_)-96bhq.md>)

## See Also

### Essentials

- [MapStyle](mapstyle.md) — A style that you can apply to a map.
