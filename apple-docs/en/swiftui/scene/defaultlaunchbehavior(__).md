---
title: 'defaultLaunchBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+, visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultlaunchbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultlaunchbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultlaunchbehavior%28_%3A%29.json'
content_hash: 'sha256:33b3e9b1b780d3c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultLaunchBehavior(_:)

<sub>Instance Method</sub>

Sets the default launch behavior for this scene.

<sub>macOS, visionOS</sub>

```swift
nonisolated func defaultLaunchBehavior(_ behavior: SceneLaunchBehavior) -> some Scene

```

## Discussion

This behavior can be used to define if a scene is shown on application launch in the absence of any previously saved state.

On platforms that do not support multiple windows, this value is ignored.

On platforms other than macOS, there must be at least one scene that presents itself. If no scenes are defined to present, the first scene will be presented, regardless of the value provided to this modifier.

> [!note] Note
> During app launch, on platforms other than macOS, the system will only consider scenes whose role matches the [UIApplicationPreferredDefaultSceneSessionRole](../../bundleresources/information-property-list/uiapplicationpreferreddefaultscenesessionrole.md) key in the application scene manifest of the `Info.plist` file. For instance, a volumetric window would need the `UIWindowSceneSessionRoleVolumetricApplication` role.

On macOS, this behavior will also be used to determine which scene is presented when clicking on the icon of a running application with no visible windows.

On visionOS, the system may background the last dismissed scene instead of closing it. Thus, the suppressed behavior additionally specifies that the scene should not be presented when tapping on the application icon with no visible windows.

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

The default value for all scenes if you do not apply this modifier is [automatic](../scenelaunchbehavior/automatic.md). With that strategy, a scene will only present itself if it is the first scene defined by the app, and no other scenes have presented themselves.

## See Also

### Configuring window visibility

- [WindowVisibilityToggle](../windowvisibilitytoggle.md) — A specialized button for toggling the visibility of a window.
- [restorationBehavior(_:)](<restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [SceneLaunchBehavior](../scenelaunchbehavior.md) — The launch behavior for a scene.
- [SceneRestorationBehavior](../scenerestorationbehavior.md) — The restoration behavior for a scene.
- [persistentSystemOverlays(_:)](<persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [windowToolbarFullScreenVisibility(_:)](<../view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md) — The visibility of the window toolbar with respect to full screen mode.
