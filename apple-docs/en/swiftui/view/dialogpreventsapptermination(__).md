---
title: 'dialogPreventsAppTermination(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dialogpreventsapptermination(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dialogpreventsapptermination(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dialogpreventsapptermination%28_%3A%29.json'
content_hash: 'sha256:0b85873723e4b401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dialogPreventsAppTermination(_:)

<sub>Instance Method</sub>

Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.

<sub>macOS</sub>

```swift
nonisolated func dialogPreventsAppTermination(_ prevents: Bool?) -> some View

```

## Discussion

SwiftUI uses the actions passed to the above dialogs to determine whether the dialog should block app termination by default when presented. If all of the following are satisfied, the dialog will not block app quit:

- There is only a single button and its role is not [destructive](../buttonrole/destructive.md)
- The [dialogSeverity(_:)](<dialogseverity(__).md>) is not `DialogSeverity/critical``
- There are no [TextField](../textfield.md)s

Use this modifier after a `View/alert` or `View/confirmationDialog` to specify whether the dialog should prevent app termination. Pass `nil` to explicitly request the automatic behavior/for the inert version of this modifier.

```swift
struct ConfirmLogoutView: View {
  @State private var isConfirming = false

  var body: some View {
    Button("Logout") { isConfirming = true }
      .confirmationDialog(
        Text("Logout?"),
          isPresented: $isConfirming
        ) {
          Button("Yes") {
            // Handle logout action.
          }
        }
        .dialogPreventsAppTermination(false)
    }
}
```

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogIcon(_:)](<../scene/dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<dialogseverity(__).md>)
- [dialogSeverity(_:)](<../scene/dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<../scene/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<../scene/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
