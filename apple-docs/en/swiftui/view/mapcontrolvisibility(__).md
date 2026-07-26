---
title: 'mapControlVisibility(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/mapcontrolvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/mapcontrolvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/mapcontrolvisibility%28_%3A%29.json'
content_hash: 'sha256:c8331af9c4818ea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# mapControlVisibility(_:)

<sub>Instance Method</sub>

Configures all Map controls in the environment to have the specified visibility

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func mapControlVisibility(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — How modified map controls should show or hide

## Discussion

MapCompass, MapScaleView, and MapPitchToggle may automatically show and hide based on the current state of the Map. That may not be appropriate for all use cases, where always showing a control may be desirable.

```swift
HStack {
    MapCompass()
    MapScaleView()
    MapPitchToggle()
}
.mapControls(.visible)
```

Other controls don’t have an automatic visibility behavior, so they will always be visible when automatic is specified. Controls may also be hidden via this modifier when conditionalizing the view is not appropriate

```swift
MapUserLocationButton()
    .mapControls(.automatic)
MapZoomStepper()
    .mapControls(.hidden)
```

## See Also

### Getting location information

- [LocationButton](../../corelocationui/locationbutton.md) — A SwiftUI button that grants one-time location authorization.
- [Map](../../mapkit/map.md) — A view that displays an embedded map interface.
- [mapStyle(_:)](<mapstyle(__).md>) — Specifies the map style to be used.
- [mapScope(_:)](<mapscope(__).md>) — Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [mapFeatureSelectionDisabled(_:)](<mapfeatureselectiondisabled(__).md>) — Specifies which map features should have selection disabled.
- [mapFeatureSelectionAccessory(_:)](<mapfeatureselectionaccessory(__).md>) — Specifies the selection accessory to display for a `MapFeature`
- [mapFeatureSelectionContent(content:)](<mapfeatureselectioncontent(content_).md>) — Specifies a custom presentation for the currently selected feature.
- [mapControls(_:)](<mapcontrols(__).md>) — Configures all `Map` views in the associated environment to have standard size and position controls
- [mapCameraKeyframeAnimator(trigger:keyframes:)](<mapcamerakeyframeanimator(trigger_keyframes_).md>) — Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_scene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<onmapcamerachange(frequency___).md>) — Performs an action when Map camera framing changes
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
