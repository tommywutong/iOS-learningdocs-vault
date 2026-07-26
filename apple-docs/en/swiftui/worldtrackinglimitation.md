---
title: WorldTrackingLimitation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldtrackinglimitation
source_url: 'https://developer.apple.com/documentation/swiftui/worldtrackinglimitation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldtrackinglimitation.json'
content_hash: 'sha256:66741c78e907a52c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WorldTrackingLimitation

<sub>Structure</sub>

A structure to represent limitations of tracking the user’s surroundings.

<sub>macOS, visionOS</sub>

```swift
struct WorldTrackingLimitation
```

## Overview

You receive a set of world tracking limitations when you read the [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) environment value. The value tells you which limitations the device currently is facing. If any of the limitations occur due to changing circumstances, e.g., the lighting, the set is updated accordingly. For example, the following [Text](text.md) view automatically updates when the world tracking limitations change:

```swift
@Environment(\.worldTrackingLimitations)
private var worldTrackingLimitations

var body: some View {
    Text("Can track translation?" + worldTrackingLimitations
        .contains(.translation) ? "No" : "Yes")
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [orientation](worldtrackinglimitation/orientation.md) — The device capabilities of tracking orientation changes in all dimensions are currently limited.
- [translation](worldtrackinglimitation/translation.md) — The device capabilities of tracking translation changes in all dimensions are currently limited.

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
- [WorldScalingCompensation](worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
