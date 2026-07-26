---
title: 'mapFeatureSelectionContent(content:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/mapfeatureselectioncontent(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/mapfeatureselectioncontent(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/mapfeatureselectioncontent%28content%3A%29.json'
content_hash: 'sha256:d57cee43021101b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# mapFeatureSelectionContent(content:)

<sub>Instance Method</sub>

Specifies a custom presentation for the currently selected feature.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func mapFeatureSelectionContent(@MapContentBuilder content: @escaping (MapFeature) -> some MapContent) -> some View

```

## Parameters

- `content` — Generates the custom presentation for a given map feature.

## Discussion

The supported presentation options are `Annotation`, and `Marker`. Other types of map content will be ignored and handled as though no content was returned.

If empty map content is returned, the system presentation will be used.

## See Also

### Getting location information

- [LocationButton](../../corelocationui/locationbutton.md) — A SwiftUI button that grants one-time location authorization.
- [Map](../../mapkit/map.md) — A view that displays an embedded map interface.
- [mapStyle(_:)](<mapstyle(__).md>) — Specifies the map style to be used.
- [mapScope(_:)](<mapscope(__).md>) — Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [mapFeatureSelectionDisabled(_:)](<mapfeatureselectiondisabled(__).md>) — Specifies which map features should have selection disabled.
- [mapFeatureSelectionAccessory(_:)](<mapfeatureselectionaccessory(__).md>) — Specifies the selection accessory to display for a `MapFeature`
- [mapControls(_:)](<mapcontrols(__).md>) — Configures all `Map` views in the associated environment to have standard size and position controls
- [mapControlVisibility(_:)](<mapcontrolvisibility(__).md>) — Configures all Map controls in the environment to have the specified visibility
- [mapCameraKeyframeAnimator(trigger:keyframes:)](<mapcamerakeyframeanimator(trigger_keyframes_).md>) — Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_scene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<onmapcamerachange(frequency___).md>) — Performs an action when Map camera framing changes
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
