---
title: 'onVolumeViewpointChange(updateStrategy:initial:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onvolumeviewpointchange(updatestrategy:initial:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onvolumeviewpointchange%28updatestrategy%3Ainitial%3A_%3A%29.json'
content_hash: 'sha256:8b139fba85a8fff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onVolumeViewpointChange(updateStrategy:initial:_:)

<sub>Instance Method</sub>

Adds an action to perform when the viewpoint of the volume changes.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy = .supported, initial: Bool = true, _ action: @escaping (Viewpoint3D, Viewpoint3D) -> Void) -> some View

```

## Parameters

- `updateStrategy` — Whether the action should be run for all viewpoint changes or only for supported viewpoint changes.

- `initial` — Whether the action should be run when this view initially appears.

- `action` — A closure to run when the viewpoint changes. The closure is also run when the volume is first opened if `initial` is `true`.

## Discussion

Use the provided [Viewpoint3D](../viewpoint3d.md) to update the content of the volume:

```swift
struct RobotContentView: View {
    @State var robotRotation: Rotation3D = .identity

    var body: some View {
        Model3D(named: "robot")
            .onVolumeViewpointChange { _, newValue in
                robotRotation = Rotation3D.slerp(
                    from: robotRotation,
                    to: newValue.squareAzimuth.orientation,
                    t: 1.0,
                    along: .shortest
                )
            }
            .rotation3DEffect(robotRotation)
            .animation(.easeInOut, value: robotRotation)
    }
}
```

By default, the action will only be run when the new viewpoint is equivalent to one of the values provided through [supportedVolumeViewpoints(_:)](<supportedvolumeviewpoints(__).md>). The viewpoint will be equivalent to where the window bar and ornaments are presented for a volume. Providing `.all` for the `updateStrategy` argument will result in the action being called without regard to the supported viewpoints.

To determine if the volume is being viewed from an unsupported viewpoint, provide `.all` for the `updateStrategy` argument and check if the viewpoint is not within the supported viewpoints:

```swift
struct ContentView: View {
    @State var showingMoveToFrontSign = false
    @State var moveToFrontSignViewpoint: Viewpoint3D = .standard

    let supportedViewpoints = [SquareAzimuth.front]

    var body: some View {
        MoveToFrontSignView(viewpoint: moveToFrontSignViewpoint)
            .opacity(showingMoveToFrontSign ? 1.0 : 0.0)
            .animation(.easeInOut, value: showingMoveToFrontSign)
            .onVolumeViewpointChange(updateStrategy: .all)
                { _, newValue in

                moveToFrontSignViewpoint = newViewpoint

                let isSupported = supportedViewpoints.contains(
                    newViewpoint.squareAzimuth)
                showingMoveToFrontSign = !isSupported
            }
            .supportedVolumeViewpoints(supportedViewpoints)
    }
}
```

The old and new [Viewpoint3D](../viewpoint3d.md) provided to the action are relative to the center of the volume.

Reading this value is only valid inside a [View](../view.md) that inherits the environment of a [Scene](../scene.md) created with a [VolumetricWindowStyle](../volumetricwindowstyle.md).

## See Also

### Interacting with volumes

- [supportedVolumeViewpoints(_:)](<supportedvolumeviewpoints(__).md>) — Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md) — A type describing when the action provided to [onVolumeViewpointChange(updateStrategy:initial:_:)](<onvolumeviewpointchange(updatestrategy_initial___).md>) should be called.
- [Viewpoint3D](../viewpoint3d.md) — A type describing what direction something is being viewed from.
- [SquareAzimuth](../squareazimuth.md) — A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [WorldAlignmentBehavior](../worldalignmentbehavior.md) — A type representing the world alignment behavior for a scene.
- [volumeWorldAlignment(_:)](<../scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [WorldScalingBehavior](../worldscalingbehavior.md) — Specifies the scaling behavior a window should have within the world.
- [defaultWorldScaling(_:)](<../scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.
- [WorldScalingCompensation](../worldscalingcompensation.md) — Indicates whether returned metrics will take dynamic scaling into account.
- [worldTrackingLimitations](../environmentvalues/worldtrackinglimitations.md) — The current limitations of the device tracking the user’s surroundings.
- [WorldTrackingLimitation](../worldtrackinglimitation.md) — A structure to represent limitations of tracking the user’s surroundings.
- [SurfaceSnappingInfo](../surfacesnappinginfo.md) — A type representing information about the window scenes snap state.
