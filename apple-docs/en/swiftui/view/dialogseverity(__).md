---
title: 'dialogSeverity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dialogseverity(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dialogseverity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dialogseverity%28_%3A%29.json'
content_hash: 'sha256:2670b8a3097c2099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dialogSeverity(_:)

<sub>Instance Method</sub>

<sub>macOS, watchOS</sub>

```swift
nonisolated func dialogSeverity(_ severity: DialogSeverity) -> some View

```

## Parameters

- `severity` — The severity to use for confirmation dialogs and alerts.

## See Also

### Configuring a dialog

- [dialogIcon(_:)](<dialogicon(__).md>) — Configures the icon used by dialogs within this view.
- [dialogIcon(_:)](<../scene/dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<../scene/dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(isSuppressed:)](<../scene/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [dialogSuppressionToggle(_:isSuppressed:)](<../scene/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogPreventsAppTermination(_:)](<dialogpreventsapptermination(__).md>) — Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
