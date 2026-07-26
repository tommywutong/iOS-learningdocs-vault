---
title: DismissWindowAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismisswindowaction
source_url: 'https://developer.apple.com/documentation/swiftui/dismisswindowaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismisswindowaction.json'
content_hash: 'sha256:23eda6bc589560b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DismissWindowAction

<sub>Structure</sub>

An action that dismisses a window associated to a particular scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct DismissWindowAction
```

## Overview

Use the [dismissWindow](environmentvalues/dismisswindow.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to dismiss a window. You call the instance directly because it defines a [callAsFunction(id:)](<dismisswindowaction/callasfunction(id_).md>) method that Swift calls when you call the instance.

For example, you can define a button that closes an auxiliary window:

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

If the window was opened with [pushWindow](environmentvalues/pushwindow.md), the original presenting will reappear when this action is performed.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction()](<dismisswindowaction/callasfunction().md>) — Dismisses the current window.
- [callAsFunction(id:)](<dismisswindowaction/callasfunction(id_).md>) — Dismisses the window that’s associated with the specified identifier.
- [callAsFunction(id:value:)](<dismisswindowaction/callasfunction(id_value_).md>) — Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.
- [callAsFunction(value:)](<dismisswindowaction/callasfunction(value_).md>) — Dismisses the window defined by the window group that is presenting the specified value type.

## See Also

### Closing windows

- [dismissWindow](environmentvalues/dismisswindow.md) — A window dismissal action stored in a view’s environment.
- [dismiss](environmentvalues/dismiss.md) — An action that dismisses the current presentation.
- [DismissAction](dismissaction.md) — An action that dismisses a presentation.
- [DismissBehavior](dismissbehavior.md) — Programmatic window dismissal behaviors.
