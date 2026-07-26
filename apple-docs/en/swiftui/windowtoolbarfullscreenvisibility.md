---
title: WindowToolbarFullScreenVisibility
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowtoolbarfullscreenvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowtoolbarfullscreenvisibility.json'
content_hash: 'sha256:5b9687453aa0a02b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowToolbarFullScreenVisibility

<sub>Structure</sub>

The visibility of the window toolbar with respect to full screen mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WindowToolbarFullScreenVisibility
```

## Overview

Use values of this type in conjunction with the [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) modifier to configure how the window toolbar displays itself when the window enters full screen mode.

For example, you can specify that the window toolbar should be hidden by default, and only show when the mouse moves into the area occupied by the menu bar:

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

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](windowtoolbarfullscreenvisibility/automatic.md) — The window toolbar visibility will be defined by the system default behavior.
- [onHover](windowtoolbarfullscreenvisibility/onhover.md) — Hide the window toolbar in full screen mode by default. It will reveal itself when the mouse moves into the area occupied by the menu bar.
- [visible](windowtoolbarfullscreenvisibility/visible.md) — Prefer to show window toolbar when the window is in full screen mode.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
