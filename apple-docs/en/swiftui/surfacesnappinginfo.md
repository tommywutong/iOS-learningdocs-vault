---
title: SurfaceSnappingInfo
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surfacesnappinginfo
source_url: 'https://developer.apple.com/documentation/swiftui/surfacesnappinginfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surfacesnappinginfo.json'
content_hash: 'sha256:4d1af6c693b727fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SurfaceSnappingInfo

<sub>Structure</sub>

A type representing information about the window scenes snap state.

<sub>visionOS</sub>

```swift
struct SurfaceSnappingInfo
```

## Overview

Use the provided [SurfaceSnappingInfo](surfacesnappinginfo.md) to modify the contents of your view.

```swift
struct LightFixtureView: View {
    @Environment(\.surfaceSnappingInfo)
    var snappingInfo: SurfaceSnappingInfo

    var body: some View {
        if snappingInfo.isSnapped {
            switch SurfaceSnappingInfo.authorizationStatus {
                case .authorized:
                    switch snappingInfo.classification {
                        case .table:
                            LampView()
                        case .floor:
                            FloorLampView()
                        default:
                            DefaultLampView()
                    }
                default:
                    DefaultLampView()
            }
        } else {
            FloatingOrbLampView()
        }
    }
}
```

The bottom of volumes may snap to horizontal surfaces and the back of windows may snap to vertical surfaces.

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [classification](surfacesnappinginfo/classification.md) — A type that provides information about the surface classification the scene is snapped to. This property only has a value if the scene is snapped and `authorizationStatus` is `.authorized`.
- [isSnapped](surfacesnappinginfo/issnapped.md) — A value that represents whether the scene is currently snapped to a physical surface or not.

### Type Properties

- [authorizationStatus](surfacesnappinginfo/authorizationstatus-swift.type.property.md) — A value that represents whether the user has authorized providing more detailed information about the surface scenes are snapped to. To request this detailed surface information, in your `Info.plist` file, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information.

### Enumerations

- [AuthorizationStatus](surfacesnappinginfo/authorizationstatus-swift.enum.md) — A type representing whether the user has granted permissions to provide more detailed information about the surface a scene is snapped to.

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
- [WorldTrackingLimitation](worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
