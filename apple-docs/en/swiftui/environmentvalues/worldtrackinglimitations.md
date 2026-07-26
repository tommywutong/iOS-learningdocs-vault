---
title: worldTrackingLimitations
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/worldtrackinglimitations
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/worldtrackinglimitations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/worldtrackinglimitations.json'
content_hash: 'sha256:123249b19bba9e48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# worldTrackingLimitations

<sub>Instance Property</sub>

The current limitations of the device tracking the user’s surroundings.

<sub>macOS, visionOS</sub>

```swift
var worldTrackingLimitations: Set<WorldTrackingLimitation> { get set }
```

## Discussion

Read this environment value from within a view to obtain the current limitations of the device tracking the user’s surroundings. The device’s capabilities may be limited due to physical circumstances such as the lighting. If any of the limitations occur due to changing circumstances, the set is updated accordingly. For example, the following [Text](../text.md) view automatically updates when the world tracking limitations change:

```swift
@Environment(\.worldTrackingLimitations)
private var worldTrackingLimitations

var body: some View {
    Text("Can track translation?" + worldTrackingLimitations
        .contains(.translation) ? "No" : "Yes")
}
```

When the device’s world tracking capabilities are limited, don’t prevent the user from experiencing your app entirely. Instead, try to adapt the user experience to the current circumstances in order to provide a meaningful experience at all times.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<../view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](../viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](../squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](../worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<../scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](../worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<../scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](../worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [WorldTrackingLimitation](../worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](../surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
