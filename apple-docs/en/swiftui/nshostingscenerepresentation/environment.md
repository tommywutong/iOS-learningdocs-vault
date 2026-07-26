---
title: environment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingscenerepresentation/environment
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenerepresentation/environment.json'
content_hash: 'sha256:0189ef1a7a1e9eea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSceneRepresentation](../nshostingscenerepresentation.md)

# environment

<sub>Instance Property</sub>

The environment for any scene(s) being represented by `self`.

<sub>macOS</sub>

```swift
@MainActor var environment: EnvironmentValues { get }
```

## Discussion

Use the environment values to programmatically present a scene’s window.

For example, you can present the window for a `Settings` scene using `OpenSettingsAction` when a menu item is selected:

```swift
let settingsScene = NSHostingSceneRepresentation {
    Settings {
        SettingsView()
    }
}

@IBAction func showAppSettings(_ sender: NSMenuItem) {
    settingsScene.environment.openSettings()
}
```
