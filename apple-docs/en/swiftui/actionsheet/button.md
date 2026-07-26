---
title: ActionSheet.Button
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/actionsheet/button
source_url: 'https://developer.apple.com/documentation/swiftui/actionsheet/button'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/actionsheet/button.json'
content_hash: 'sha256:232b07046e797784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ActionSheet](../actionsheet.md)

# ActionSheet.Button

<sub>Type Alias</sub>

A button representing an operation of an action sheet presentation.

> [!warning] Deprecated
> Use a [View](../view.md) modifier like [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<../view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_)-8y541.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
typealias Button = Alert.Button
```

## Discussion

The [ActionSheet](../actionsheet.md) button is type-aliased to the [Alert](../alert.md) button type, which provides default, cancel, and destructive styles.
