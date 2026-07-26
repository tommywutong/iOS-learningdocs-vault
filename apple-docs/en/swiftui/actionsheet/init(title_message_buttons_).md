---
title: 'init(title:message:buttons:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/actionsheet/init(title:message:buttons:)'
source_url: 'https://developer.apple.com/documentation/swiftui/actionsheet/init(title:message:buttons:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/actionsheet/init%28title%3Amessage%3Abuttons%3A%29.json'
content_hash: 'sha256:3261d7b75d93b007'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ActionSheet](../actionsheet.md)

# init(title:message:buttons:)

<sub>Initializer</sub>

Creates an action sheet with the provided buttons.

> [!warning] Deprecated
> Use a [View](../view.md) modifier like [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<../view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_)-8y541.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(title: Text, message: Text? = nil, buttons: [ActionSheet.Button] = [.cancel()])
```

## Parameters

- `title` — The title of the action sheet.

- `message` — The message to display in the body of the action sheet.

- `buttons` — The buttons to show in the action sheet.
