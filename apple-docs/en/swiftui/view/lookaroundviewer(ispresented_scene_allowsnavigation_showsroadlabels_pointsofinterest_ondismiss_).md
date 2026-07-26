---
title: 'lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/lookaroundviewer%28ispresented%3Ascene%3Aallowsnavigation%3Ashowsroadlabels%3Apointsofinterest%3Aondismiss%3A%29.json'
content_hash: 'sha256:a2ed843e1c843bcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool = true, showsRoadLabels: Bool = true, pointsOfInterest: PointOfInterestCategories = .all, onDismiss: (() -> Void)? = nil) -> some View

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
- [mapControlVisibility(_:)](<mapcontrolvisibility(__).md>) — Configures all Map controls in the environment to have the specified visibility
- [mapCameraKeyframeAnimator(trigger:keyframes:)](<mapcamerakeyframeanimator(trigger_keyframes_).md>) — Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<onmapcamerachange(frequency___).md>) — Performs an action when Map camera framing changes
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — Presents a map item detail popover.
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — Presents a map item detail popover.
