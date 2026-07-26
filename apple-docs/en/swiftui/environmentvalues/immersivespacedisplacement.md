---
title: immersiveSpaceDisplacement
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/immersivespacedisplacement
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/immersivespacedisplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/immersivespacedisplacement.json'
content_hash: 'sha256:97a4aafcabfa15ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# immersiveSpaceDisplacement

<sub>Instance Property</sub>

The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.

<sub>visionOS</sub>

```swift
var immersiveSpaceDisplacement: Pose3D { get }
```

## Discussion

By default, the system places the origin of the immersive space at floor level, at the person’s feet. When joining a shared activity, the system moves the immersive space to an appropriate location for all participants. As participants join and leave the activity, the location of participants and the immersive space can update. Read this property to get the current offset of the immersive space relative to its default position.

If you access this property outside of an open immersive space, it contains the value [identity](../../spatial/pose3d/identity.md).

If you display participant-specific views or entities in your shared activity, use the inverse of this displacement value to position those views and entities in the immersive space. Applying the inverse value positions them as if they were in a single-participant immersive space.

In the following example, this value is applied to position a game HUD entity at the person’s location, rather than the shared activity’s location:

```swift
@main
struct GameApp: App {
    var body: some Scene {
        ImmersiveSpace {
            ImmersiveGameView()
        }
    }
}

struct ImmersiveGameView: View {
    @Environment(\.immersiveSpaceDisplacement) private var immersiveSpaceDisplacement

    let gameHUDEntity = makeGameHUDEntity()

    var body: some View {
        RealityView { content in
            // ...
        } update: { content in
            let inverseDisplacement = float4x4(immersiveSpaceDisplacement.inverse)
            gameHUDEntity.setTransformMatrix(inverseDisplacement, relativeTo: nil)
        }
    }
}
```

## See Also

### Creating an immersive space

- [ImmersiveSpace](../immersivespace.md) — A scene that presents its content in an unbounded space.
- [ImmersiveSpaceContentBuilder](../immersivespacecontentbuilder.md) — A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) — Sets the style for an immersive space.
- [ImmersionStyle](../immersionstyle.md) — The styles that an immersive space can have.
- [ImmersiveEnvironmentBehavior](../immersiveenvironmentbehavior.md) — The behavior of the system-provided immersive environments when a scene is opened by your app.
- [ProgressiveImmersionAspectRatio](../progressiveimmersionaspectratio.md)
