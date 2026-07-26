---
title: 'volumeWorldAlignment(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/volumeworldalignment(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/volumeworldalignment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/volumeworldalignment%28_%3A%29.json'
content_hash: 'sha256:8302dc6e4a0a73c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# volumeWorldAlignment(_:)

<sub>Instance Method</sub>

Specifies how a volume should be aligned when moved in the world.

<sub>visionOS</sub>

```swift
nonisolated func volumeWorldAlignment(_ behavior: WorldAlignmentBehavior) -> some Scene

```

## Discussion

For example, you can create a volume that remains parallel to the floor even when lifted up high above eye level by applying a [gravityAligned](../worldalignmentbehavior/gravityaligned.md) alignment to the scene:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .windowStyle(.volumetric)
        .volumeWorldAlignment(.gravityAligned)
    }
}
```

The default value if you don’t apply the modifier is [automatic](../worldalignmentbehavior/automatic.md). With that strategy, volumes will tilt themselves so the front remains fully visible while being repositioned.

## See Also

### Interacting with volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) — Adds an action to perform when the viewpoint of the volume changes.
- [supportedVolumeViewpoints(_:)](<../view/supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<../view/onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](../viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](../squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](../worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [WorldScalingBehavior](../worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](../worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](../environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](../worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](../surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
