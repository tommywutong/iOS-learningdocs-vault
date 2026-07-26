---
title: WorldAlignmentBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldalignmentbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/worldalignmentbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldalignmentbehavior.json'
content_hash: 'sha256:64922f1c647221d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WorldAlignmentBehavior

<sub>Structure</sub>

A type representing the world alignment behavior for a scene.

<sub>visionOS</sub>

```swift
struct WorldAlignmentBehavior
```

## Overview

A value of this type can be provided to the [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) scene modifier to control the world alignment volumes should maintain as they are repositioned. The default value is [automatic](worldalignmentbehavior/automatic.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [adaptive](worldalignmentbehavior/adaptive.md) — When lifted above eye level, the volume will tilt so the front remains fully visible.
- [automatic](worldalignmentbehavior/automatic.md) — The world alignment behavior that is standard for the system.
- [gravityAligned](worldalignmentbehavior/gravityaligned.md) — The volume will not tilt so as to remain aligned with gravity.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
