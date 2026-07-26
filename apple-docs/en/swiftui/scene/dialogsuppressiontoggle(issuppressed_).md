---
title: 'dialogSuppressionToggle(isSuppressed:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/dialogsuppressiontoggle(issuppressed:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/dialogsuppressiontoggle(issuppressed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/dialogsuppressiontoggle%28issuppressed%3A%29.json'
content_hash: 'sha256:c6708ee49e399574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# dialogSuppressionToggle(isSuppressed:)

<sub>Instance Method</sub>

Enables user suppression of an alert with a custom suppression message.

<sub>macOS</sub>

```swift
nonisolated func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene

```

## Parameters

- `isSuppressed` — Whether the suppression toggle is on or off in the dialog.

## Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows the user to request the alert not be displayed again. Typically whether a dialog is suppressed is stored in `AppStorage` and used to decide whether to present the dialog in the future.

The following example configures an alert with a suppression toggle. The toggle’s state is stored in `AppStorage` and used to determine whether or not to show the dialog when the “Delete Items” button is pressed.

```swift
struct MyApp: App {
    @State private var isShowingDialog = false
    @AppStorage("suppressEraseItemAlert")
    private var suppressAlert = false

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
        .dialogSuppressionToggle(
            "Do not ask about erasing items again",
            isSuppressed: $suppressAlert)
    }
}
```

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<../view/dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogIcon(_:)](<dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<../view/dialogseverity(__).md>)
- [dialogSeverity(_:)](<dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<../view/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<../view/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<../view/dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
