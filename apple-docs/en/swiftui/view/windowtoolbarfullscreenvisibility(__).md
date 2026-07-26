---
title: 'windowToolbarFullScreenVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/windowtoolbarfullscreenvisibility%28_%3A%29.json'
content_hash: 'sha256:95bef7c0c2a6b5b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# windowToolbarFullScreenVisibility(_:)

<sub>Instance Method</sub>

Configures the visibility of the window toolbar when the window enters full screen mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func windowToolbarFullScreenVisibility(_ visibility: WindowToolbarFullScreenVisibility) -> some View

```

## Parameters

- `visibility` — The visibility to use for the window toolbar in full screen mode.

## Discussion

By default, the window toolbar will show at the top of the display, above the window’s contents.

You can use this modifier to override the default behavior.

For example, you can specify that the window toolbar should be hidden by default, and only show once the mouse moves into the area occupied by the menu bar:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ...
            }
            .windowToolbarFullScreenVisibility(.onHover)
    }
}
```

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](../windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<../scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<../scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](../scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](../scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<../scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
