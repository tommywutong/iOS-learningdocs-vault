---
title: openSettings
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/opensettings
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/opensettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/opensettings.json'
content_hash: 'sha256:0f6a738aadbf8092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# openSettings

<sub>Instance Property</sub>

A Settings presentation action stored in a view’s environment.

<sub>macOS</sub>

```swift
var openSettings: OpenSettingsAction { get }
```

## Discussion

Use the `openSettings` environment value to get an [OpenSettingsAction](../opensettingsaction.md) instance for a given [Environment](../environment.md). Then call the instance to open a window. You call the instance directly because it defines a [callAsFunction()](<../opensettingsaction/callasfunction().md>) method that Swift calls when you call the instance.

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

## See Also

### Managing a settings window

- [Settings](../settings.md) — A scene that presents an interface for viewing and modifying an app’s settings.
- [SettingsLink](../settingslink.md) — A view that opens the Settings scene defined by an app.
- [OpenSettingsAction](../opensettingsaction.md) — An action that presents the settings scene for an app.
