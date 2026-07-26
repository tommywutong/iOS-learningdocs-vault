---
title: UNTextInputNotificationAction
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/untextinputnotificationaction
source_url: 'https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/untextinputnotificationaction.json'
content_hash: 'sha256:7cbd84e9345d9bcb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNTextInputNotificationAction

<sub>Class</sub>

An action that accepts user-typed text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class UNTextInputNotificationAction
```

## Overview

Use [UNTextInputNotificationAction](untextinputnotificationaction.md) objects to define an action that allows the user to provide a custom text-based response. When the user selects an action of this type, the system displays controls for the user to enter or dictate the text content. That text is then included in the response object that’s delivered to your app.

For information on how to define actions and categories, see [Declaring your actionable notification types](declaring-your-actionable-notification-types.md).

## Relationships

- **Inherits From**: [UNNotificationAction](unnotificationaction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Essentials

- [+ actionWithIdentifier:title:options:textInputButtonTitle:textInputPlaceholder:](<untextinputnotificationaction/init(identifier_title_options_textinputbuttontitle_textinputplaceholder_).md>) — Creates an action object that accepts text input from the user.
- [+ actionWithIdentifier:title:options:icon:textInputButtonTitle:textInputPlaceholder:](<untextinputnotificationaction/init(identifier_title_options_icon_textinputbuttontitle_textinputplaceholder_).md>) — Creates an action object with an icon that accepts text input from the user.

### Getting Information

- [textInputButtonTitle](untextinputnotificationaction/textinputbuttontitle.md) — The localized title of the text input button that the system displays to the user.
- [textInputPlaceholder](untextinputnotificationaction/textinputplaceholder.md) — The placeholder text that the system localizes and displays in the text input field.

## See Also

### Notification categories and user actions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md) — Differentiate your notifications and add action buttons to the notification interface.
- [UNNotificationCategory](unnotificationcategory.md) — A type of notification your app supports and the custom actions that the system displays.
- [UNNotificationAction](unnotificationaction.md) — A task your app performs in response to a notification that the system delivers.
