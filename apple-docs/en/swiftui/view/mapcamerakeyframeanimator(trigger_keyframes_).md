---
title: 'mapCameraKeyframeAnimator(trigger:keyframes:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/mapcamerakeyframeanimator(trigger:keyframes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/mapcamerakeyframeanimator(trigger:keyframes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/mapcamerakeyframeanimator%28trigger%3Akeyframes%3A%29.json'
content_hash: 'sha256:a3bb0f40847de0d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# mapCameraKeyframeAnimator(trigger:keyframes:)

<sub>Instance Method</sub>

Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func mapCameraKeyframeAnimator(trigger: some Equatable, @KeyframesBuilder<MapCamera> keyframes: @escaping (MapCamera) -> some Keyframes<MapCamera>) -> some View

```

## Parameters

- `trigger` — A value to observe for changes.

- `keyframes` — A keyframes builder closure that is called when starting a new keyframe animation. The current map camera is provided as the only parameter.

## Discussion

When the trigger value changes, the map calls the `keyframes` closure to generate the keyframes that will animate the camera. The animation will continue for the duration of the keyframes that you specify.

If the user performs a gesture while the animation is in progress, the animation will be immediately removed, allowing the interaction to take control of the camera.

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
- [mapControlVisibility(_:)](<mapcontrolvisibility(__).md>) — Configures all Map controls in the environment to have the specified visibility
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_scene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<onmapcamerachange(frequency___).md>) — Performs an action when Map camera framing changes
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
