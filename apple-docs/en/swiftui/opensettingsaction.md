---
title: OpenSettingsAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/opensettingsaction
source_url: 'https://developer.apple.com/documentation/swiftui/opensettingsaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/opensettingsaction.json'
content_hash: 'sha256:40a8b44033b1db72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OpenSettingsAction

<sub>Structure</sub>

An action that presents the settings scene for an app.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct OpenSettingsAction
```

## Overview

Use the [openSettings](environmentvalues/opensettings.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to open a window. You call the instance directly because it defines a [callAsFunction()](<opensettingsaction/callasfunction().md>) method that Swift calls when you call the instance.

For example, you can define a button that opens the settings window to a particular tab:

```swift
@main
struct MyApp: App {
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

struct SettingsView: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    var body: some View {
        TabView(selection: $selectedSettingsTab) {
            GeneralSettings()
            AdvancedSettings()
        }
    }
}

struct AdvancedSettingsButton: View {
    @AppStorage("selectedSettingsTab")
    private var selectedSettingsTab = SettingsTab.general

    @Environment(\.openSettings) private var openSettings

    var body: some View {
        Button("Open Advanced Settings…") {
            selectedSettingsTab = .advanced
            openSettings()
        }
    }
}

enum SettingsTab: Int {
    case general
    case advanced
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Methods

- [callAsFunction()](<opensettingsaction/callasfunction().md>) — Opens the window associated to the [Settings](settings.md) scene defined by this app, if one exists.

## See Also

### Managing a settings window

- [Settings](settings.md) — A scene that presents an interface for viewing and modifying an app’s settings.
- [SettingsLink](settingslink.md) — A view that opens the Settings scene defined by an app.
- [openSettings](environmentvalues/opensettings.md) — A Settings presentation action stored in a view’s environment.
