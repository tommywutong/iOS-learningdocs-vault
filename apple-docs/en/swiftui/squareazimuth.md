---
title: SquareAzimuth
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/squareazimuth
source_url: 'https://developer.apple.com/documentation/swiftui/squareazimuth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/squareazimuth.json'
content_hash: 'sha256:d635deed23e5da50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SquareAzimuth

<sub>Enumeration</sub>

A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.

<sub>visionOS</sub>

```swift
@frozen enum SquareAzimuth
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [Set](squareazimuth/set.md)

### Enumeration Cases

- [SquareAzimuth.back](squareazimuth/back.md) — Has an orientation with an horizontal angle equal to `180°`
- [SquareAzimuth.front](squareazimuth/front.md) — Has an orientation with an horizontal angle equal to `0°`.
- [SquareAzimuth.left](squareazimuth/left.md) — Has an orientation with an horizontal angle equal to `270°`.
- [SquareAzimuth.right](squareazimuth/right.md) — Has an orientation with an horizontal angle equal to `90°`.

### Initializers

- [init(closestToAzimuth:)](<squareazimuth/init(closesttoazimuth_).md>) — Creates a [SquareAzimuth](squareazimuth.md) case with an orientation that has a horizontal angle closest to the provided azimuth.

### Instance Properties

- [orientation](squareazimuth/orientation.md) — A 3D rotation that is snapped to the center of one of the four sides.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](viewpoint3d.md) — A type describing what direction something is being viewed from.
- [WorldAlignmentBehavior](worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
