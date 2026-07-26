---
title: VolumeViewpointUpdateStrategy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/volumeviewpointupdatestrategy
source_url: 'https://developer.apple.com/documentation/swiftui/volumeviewpointupdatestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/volumeviewpointupdatestrategy.json'
content_hash: 'sha256:4c91dcc7288cf611'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VolumeViewpointUpdateStrategy

<sub>Structure</sub>

A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.

<sub>visionOS</sub>

```swift
struct VolumeViewpointUpdateStrategy
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [all](volumeviewpointupdatestrategy/all.md) — The action should be run for all viewpoint changes.
- [supported](volumeviewpointupdatestrategy/supported.md) — The action should only be run when the new viewpoint is equivalent to one of the values provided through [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>).

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [Viewpoint3D](viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
