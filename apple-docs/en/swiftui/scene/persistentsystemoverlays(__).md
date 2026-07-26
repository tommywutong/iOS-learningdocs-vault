---
title: 'persistentSystemOverlays(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/persistentsystemoverlays(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/persistentsystemoverlays(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/persistentsystemoverlays%28_%3A%29.json'
content_hash: 'sha256:6bed83093076c816'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# persistentSystemOverlays(_:)

<sub>Instance Method</sub>

Sets the preferred visibility of the non-transient system views overlaying the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func persistentSystemOverlays(_ preferredVisibility: Visibility) -> some Scene

```

## Parameters

- `preferredVisibility` — A value that indicates the visibility of the non-transient system views overlaying the app.

## Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform.

In iOS, the following example hides every persistent system overlay. In visionOS 2 and later, the SharePlay Indicator hides if the scene is shared through SharePlay, or not shared at all. During screen sharing, the indicator always remains visible. The Home indicator doesn’t appear without specific user intent when you set visibility to `hidden`. For a [WindowGroup](../windowgroup.md), the modifier affects the visibility of the window chrome. For an [ImmersiveSpace](../immersivespace.md), it affects the Home indicator.

```swift
struct ImmersiveView: View {
    var body: some View {
        Text("Maximum immersion")
            .persistentSystemOverlays(.hidden)
    }
}
```

> [!note] Note
> You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](../windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](../scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](../scenerestorationbehavior.md) — The restoration behavior for a scene.
- [windowToolbarFullScreenVisibility(_:)](<../view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
