---
title: WorldScalingBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldscalingbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/worldscalingbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldscalingbehavior.json'
content_hash: 'sha256:6903eb4510642a16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WorldScalingBehavior

<sub>Structure</sub>

Specifies the scaling behavior a window should have within the world.

<sub>visionOS</sub>

```swift
struct WorldScalingBehavior
```

## Overview

By default, a regular [WindowGroup](windowgroup.md) uses a scaling behavior of [dynamic](worldscalingbehavior/dynamic.md), and a window with [volumetric](windowstyle/volumetric.md) has a fixed scale.

Dynamic scale means the window will scale larger as it moves further away, maintaining the same angular size. Fixed scale means the window will keep its physical size in the world.

For further information, see [Spatial layout](../design/human-interface-guidelines/spatial-layout.md#Scale) in the Human Interface Guidelines.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](worldscalingbehavior/automatic.md) — The scaling behavior that is standard for the window’s style.
- [dynamic](worldscalingbehavior/dynamic.md) — The window will scale up as it moves further away, maintaining the same angular size.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
