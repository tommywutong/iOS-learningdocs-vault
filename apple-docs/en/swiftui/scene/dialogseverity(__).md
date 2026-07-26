---
title: 'dialogSeverity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/dialogseverity(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/dialogseverity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/dialogseverity%28_%3A%29.json'
content_hash: 'sha256:d55ef41853dc39ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# dialogSeverity(_:)

<sub>Instance Method</sub>

Sets the severity for alerts.

<sub>macOS</sub>

```swift
nonisolated func dialogSeverity(_ severity: DialogSeverity) -> some Scene

```

## Parameters

- `severity` — The severity to use for alerts.

## Discussion

The following example configures an alert for erasing some number of items. Since this operation is destructive and non-recoverable, a `.critical` severity is used.

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
        .dialogSeverity(.critical)
    }
}
```

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<../view/dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogIcon(_:)](<dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<../view/dialogseverity(__).md>)
- [dialogSuppressionToggle(isSuppressed:)](<../view/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<../view/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<../view/dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
