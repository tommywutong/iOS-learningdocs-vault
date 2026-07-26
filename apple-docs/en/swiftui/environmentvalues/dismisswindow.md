---
title: dismissWindow
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/dismisswindow
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/dismisswindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/dismisswindow.json'
content_hash: 'sha256:dd64d349999932bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# dismissWindow

<sub>Instance Property</sub>

A window dismissal action stored in a view’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var dismissWindow: DismissWindowAction { get }
```

## Discussion

Use the `dismissWindow` environment value to get an [DismissWindowAction](../dismisswindowaction.md) instance for a given [Environment](../environment.md). Then call the instance to dismiss a window. You call the instance directly because it defines a [callAsFunction(id:)](<../dismisswindowaction/callasfunction(id_).md>) method that Swift calls when you call the instance.

For example, you can define a button that dismisses an auxiliary window:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Window("Auxiliary", id: "auxiliary") {
            AuxiliaryContentView()
        }
        #endif
    }
}

struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            dismissWindow(id: "auxiliary")
        }
    }
}
```

If the window was opened with [pushWindow](pushwindow.md), the presenting window will reappear when this action is performed.

## See Also

### Closing windows

- [DismissWindowAction](../dismisswindowaction.md) — An action that dismisses a window associated to a particular scene.
- [dismiss](dismiss.md) — An action that dismisses the current presentation.
- [DismissAction](../dismissaction.md) — An action that dismisses a presentation.
- [DismissBehavior](../dismissbehavior.md) — Programmatic window dismissal behaviors.
