---
title: 'dialogIcon(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/dialogicon(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/dialogicon(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/dialogicon%28_%3A%29.json'
content_hash: 'sha256:2e8cc8a5c3f42915'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# dialogIcon(_:)

<sub>Instance Method</sub>

Configures the icon used by alerts.

<sub>macOS</sub>

```swift
nonisolated func dialogIcon(_ icon: Image?) -> some Scene

```

## Parameters

- `icon` — The custom icon to use for the alert. Passing `nil` will use the default app icon.

## Discussion

In macOS, this icon replaces the default icon of the app.

```swift
struct MyApp: App {
    @State private var isShowingDialog = false

    var body: some Scene {
        Window(...) {
            Button("Delete items") {
                isShowingDialog = true
            }
        }

        AlertScene(
            "Are you sure you want to erase these items?",
            isPresented: $isShowingDialog
        ) {
            Button("Erase", role: .destructive) {
                // Handle item deletion.
            }
            Button("Cancel", role: .cancel) {
                // Handle cancellation
            }
        }
        .dialogIcon(Image(Trash.png))
    }
}
```

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<../view/dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogSeverity(_:)](<../view/dialogseverity(__).md>)
- [dialogSeverity(_:)](<dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<../view/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<../view/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<../view/dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
