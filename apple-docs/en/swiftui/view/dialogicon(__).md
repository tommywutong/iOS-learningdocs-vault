---
title: 'dialogIcon(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dialogicon(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dialogicon(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dialogicon%28_%3A%29.json'
content_hash: 'sha256:29bfe0b68d4453b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dialogIcon(_:)

<sub>Instance Method</sub>

Configures the icon used by dialogs within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated func dialogIcon(_ icon: Image?) -> some View

```

## Parameters

- `icon` — The custom icon to use for confirmation dialogs and alerts. Passing `nil` will use the default app icon.

## Discussion

On macOS, this icon replaces the default icon of the app.

On watchOS, this icon will be shown in any dialogs presented.

This modifier has no effect on other platforms.

The following example configures a `confirmationDialog` with a custom image.

```swift
Button("Delete items") {
    isShowingDialog = true
}
.confirmationDialog(
    "Are you sure you want to erase these items?",
        isPresented: $isShowingDialog
) {
    Button("Erase", role: .destructive) {
        // Handle item deletion.
    }
    Button("Cancel", role: .cancel) {
        isShowingDialog = false
    }
}
.dialogIcon(Image(...))
```

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<../scene/dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<dialogseverity(__).md>)
- [dialogSeverity(_:)](<../scene/dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<../scene/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<../scene/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
