---
title: 'restorationBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/restorationbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/restorationbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/restorationbehavior%28_%3A%29.json'
content_hash: 'sha256:a847429b22a9f722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# restorationBehavior(_:)

<sub>Instance Method</sub>

Sets the restoration behavior for this scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func restorationBehavior(_ behavior: SceneRestorationBehavior) -> some Scene

```

## Discussion

Use this scene modifier to apply a value of this type to a [Scene](../scene.md) you define in your [App](../app.md) declaration. The value you specify determines how the system will restore windows from a previous run of your application.

For example, you may have a scene that you do not wish to be restored on launch:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window(id: "network-test", "Network Connection Test") {
            NetworkTestView()
        }
        .restorationBehavior(.disabled)
    }
}
```

The default value for all scenes if you do not apply the modifier is [automatic](../scenerestorationbehavior/automatic.md). With that strategy, scenes will restore themselves depending on the default behavior for the platform.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](../windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [SceneLaunchBehavior](../scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](../scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<../view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
