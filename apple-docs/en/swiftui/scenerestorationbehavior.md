---
title: SceneRestorationBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenerestorationbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/scenerestorationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenerestorationbehavior.json'
content_hash: 'sha256:ff6a5db8479131f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SceneRestorationBehavior

<sub>Structure</sub>

The restoration behavior for a scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SceneRestorationBehavior
```

## Overview

Use the [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) scene modifier to apply a value of this type to a [Scene](scene.md) you define in your [App](app.md) declaration. The value you specify determines how the system will restore windows from a previous run of your application.

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

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](scenerestorationbehavior/automatic.md) — The automatic behavior. The scene’s windows will be restored as defined by the underlying platform.
- [disabled](scenerestorationbehavior/disabled.md) — The disabled behavior. The scene’s windows will not be restored.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](scenelaunchbehavior.md) — The launch behavior for a scene.
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
