---
title: WorldScalingCompensation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldscalingcompensation
source_url: 'https://developer.apple.com/documentation/swiftui/worldscalingcompensation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldscalingcompensation.json'
content_hash: 'sha256:28e389fa7d116612'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WorldScalingCompensation

<sub>Structure</sub>

Indicates whether returned metrics will take dynamic scaling into account.

<sub>visionOS</sub>

```swift
struct WorldScalingCompensation
```

## Overview

On visionOS, a window scene or a volume scene with the [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) modifier may scale dynamically when the user repositions it. In those cases, the metrics returned by a [PhysicalMetric](physicalmetric.md) or [PhysicalMetricsConverter](physicalmetricsconverter.md) value may or may not correspond to the units of a `RealityView`.

World scale compensation lets you specify if this scaling is taken into account. If the values are [unscaled](worldscalingcompensation/unscaled.md), they will correspond to the physical metrics of the user’s surroundings, regardless of dynamic scale. If [scaled](worldscalingcompensation/scaled.md), they will be scaled appropriately for the scene, which means they will match the default coordinate system of a `RealityView` in that scene.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [scaled](worldscalingcompensation/scaled.md) — Returns metrics that are scaled appropriately to match the coordinate system of their scene, including any world scaling behavior.
- [unscaled](worldscalingcompensation/unscaled.md) — Returns metrics that match the scale of the user’s surroundings, regardless of the world scaling behavior of their scene.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
