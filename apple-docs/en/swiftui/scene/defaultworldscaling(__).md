---
title: 'defaultWorldScaling(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultworldscaling(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultworldscaling(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultworldscaling%28_%3A%29.json'
content_hash: 'sha256:68bfad1715c69a48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultWorldScaling(_:)

<sub>Instance Method</sub>

Specify the world scaling behavior for the window.

<sub>visionOS</sub>

```swift
nonisolated func defaultWorldScaling(_ scaling: WorldScalingBehavior) -> some Scene

```

## Discussion

By default, regular windows increase their physical size as they move further away, ensuring they remain at the same angular size. This preserves legibility and ease of use for text and controls. Volumes render with a fixed physical size, because they are most commonly used for 3D content which is meant to behave with greater physical accuracy.

This modifier overrides the physical scaling behavior for volumes, so they scale like windows while still maintaining other volumetric behaviors.

This modifier has no effect on immersive spaces or windows without a window style of [volumetric](../windowstyle/volumetric.md).

```swift
@main
struct SampleApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .windowStyle(.volumetric)
        .defaultWorldScaling(.dynamic)
    }
}
```

For further information, see [Spatial layout](../../design/human-interface-guidelines/spatial-layout.md#Scale) in the Human Interface Guidelines.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<../view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](../viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](../squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](../worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](../worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [WorldScalingCompensation](../worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](../environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](../worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](../surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
