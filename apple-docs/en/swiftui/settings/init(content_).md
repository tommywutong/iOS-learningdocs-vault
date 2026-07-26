---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/settings/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/settings/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/settings/init%28content%3A%29.json'
content_hash: 'sha256:bf3c688af9ab793c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Settings](../settings.md)

# init(content:)

<sub>Initializer</sub>

Creates a scene that presents an interface for viewing and modifying an app’s preferences.

<sub>macOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A view that represents the content of the scene.

## Discussion

Use `Settings(content:)` to add a preferences scene when you declare your app using the [App](../app.md) protocol.

The example below shows the view content for the settings scene added to the SwiftUI app delegate:

```swift
@main
struct MacSwiftUISnippets: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}
```

When you use an [App](../app.md) declaration for multiple platforms, compile the settings scene only in macOS, as shown in the example above.
