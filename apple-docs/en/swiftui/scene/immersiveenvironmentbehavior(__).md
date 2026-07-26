---
title: 'immersiveEnvironmentBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/immersiveenvironmentbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/immersiveenvironmentbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/immersiveenvironmentbehavior%28_%3A%29.json'
content_hash: 'sha256:f4c7195705e10818'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# immersiveEnvironmentBehavior(_:)

<sub>Instance Method</sub>

Sets the immersive environment behavior that should apply when this scene opens.

<sub>visionOS</sub>

```swift
nonisolated func immersiveEnvironmentBehavior(_ behavior: ImmersiveEnvironmentBehavior) -> some Scene

```

## Parameters

- `behavior` — A immersive environment behavior that should be applied by the system when this scene opens.

## Return Value

A scene that uses the specified `behavior`.

## Discussion

Use this modifier to control how the immersive environment behaves when an [ImmersiveSpace](../immersivespace.md) is opened, that uses an immersion style that supports keeping the immersive environment visible.

For example, the following app defines an Immersive Space that displays an interactive car engine model, and by setting the system environment behavior to `.coexist`, the immersive environment can remain shown while inspecting the details of the engine:

```swift
@main
struct App: App {
    var body: some Scene {
        ImmersiveSpace {
            CarEngineModel()
        }
        .immersiveEnvironmentBehavior(.coexist)
    }
}
```

Note: The behavior is a preference and does not always have to be honored by the system.

## See Also

### Configuring immersive scenes

- [immersiveContentBrightness(_:)](<immersivecontentbrightness(__).md>) — Sets the content brightness of an immersive space.
