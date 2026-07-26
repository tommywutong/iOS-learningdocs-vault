---
title: 'sideBySideButtons(title:message:primaryButton:secondaryButton:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alert/sidebysidebuttons%28title%3Amessage%3Aprimarybutton%3Asecondarybutton%3A%29.json'
content_hash: 'sha256:c6d47c422e02fb27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alert](../alert.md)

# sideBySideButtons(title:message:primaryButton:secondaryButton:)

<sub>Type Method</sub>

Creates a side by side button alert.

> [!warning] Deprecated
> Use a [View](../view.md) modifier like [alert(_:isPresented:presenting:actions:message:)](<../view/alert(__ispresented_presenting_actions_message_)-8584l.md>) instead.

<sub>watchOS</sub>

```swift
static func sideBySideButtons(title: Text, message: Text? = nil, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert
```

## Parameters

- `title` — The title of the alert.

- `message` — The message to display in the body of the alert.

- `primaryButton` — The first button to show in the alert.

- `secondaryButton` — The second button to show in the alert.

## Discussion

The system determines the visual ordering of the buttons.

## See Also

### Creating an alert

- [init(title:message:dismissButton:)](<init(title_message_dismissbutton_).md>) — Creates an alert with one button. _(deprecated)_
- [init(title:message:primaryButton:secondaryButton:)](<init(title_message_primarybutton_secondarybutton_).md>) — Creates an alert with two buttons. _(deprecated)_
