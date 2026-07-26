---
title: SceneLaunchBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenelaunchbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/scenelaunchbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenelaunchbehavior.json'
content_hash: 'sha256:623c0262f4af99d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SceneLaunchBehavior

<sub>Structure</sub>

The launch behavior for a scene.

<sub>macOS, visionOS</sub>

```swift
struct SceneLaunchBehavior
```

## Overview

Use the [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) modifier to apply a value of this type to a [Scene](scene.md) you specify in your [App](app.md). The value you specify determines how the system will present the scene in the absense of any previously restored scenes on launch of your application.

For example, you may wish to present a welcome window on launch of your app when there are no previous document windows being restored:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { configuration in
            DocumentEditor(configuration.$document)
        }

        Window("Welcome to My App", id: "welcome") {
            WelcomeView()
        }
        .defaultLaunchBehavior(.presented)
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](scenelaunchbehavior/automatic.md) — The automatic behavior.
- [presented](scenelaunchbehavior/presented.md) — The presented behavior. The scene will present itself in the absence of any previously restored scenes.
- [suppressed](scenelaunchbehavior/suppressed.md) — The suppressed behavior. The scene will not present itself in the absence of any previously restored scenes.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneRestorationBehavior](scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
