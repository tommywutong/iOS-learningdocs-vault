---
title: 'supportedVolumeViewpoints(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/supportedvolumeviewpoints(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/supportedvolumeviewpoints(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/supportedvolumeviewpoints%28_%3A%29.json'
content_hash: 'sha256:83ec83e39e6ccece'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# supportedVolumeViewpoints(_:)

<sub>Instance Method</sub>

Specifies which viewpoints are supported for the window bar and ornaments in a volume.

<sub>visionOS</sub>

```swift
nonisolated func supportedVolumeViewpoints(_ viewpoints: SquareAzimuth.Set) -> some View

```

## Discussion

This defaults to all viewpoints and determines which viewpoints the window bar and ornaments will ‘follow’ the user to as they move around the volume.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](../viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](../squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](../worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<../scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](../worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<../scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](../worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](../environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](../worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](../surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
