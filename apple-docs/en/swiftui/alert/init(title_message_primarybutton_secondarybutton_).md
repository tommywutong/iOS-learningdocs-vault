---
title: 'init(title:message:primaryButton:secondaryButton:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/alert/init(title:message:primarybutton:secondarybutton:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alert/init(title:message:primarybutton:secondarybutton:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alert/init%28title%3Amessage%3Aprimarybutton%3Asecondarybutton%3A%29.json'
content_hash: 'sha256:b9943e354c11df4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alert](../alert.md)

# init(title:message:primaryButton:secondaryButton:)

<sub>Initializer</sub>

Creates an alert with two buttons.

> [!warning] Deprecated
> Use a [View](../view.md) modifier like [alert(_:isPresented:presenting:actions:message:)](<../view/alert(__ispresented_presenting_actions_message_)-8584l.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(title: Text, message: Text? = nil, primaryButton: Alert.Button, secondaryButton: Alert.Button)
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
- [sideBySideButtons(title:message:primaryButton:secondaryButton:)](<sidebysidebuttons(title_message_primarybutton_secondarybutton_).md>) — Creates a side by side button alert. _(deprecated)_
