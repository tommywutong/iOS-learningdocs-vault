---
title: UNNotificationAction
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationaction
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction.json'
content_hash: 'sha256:4e3776d4b456cecc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationAction

<sub>Class</sub>

A task your app performs in response to a notification that the system delivers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class UNNotificationAction
```

## Overview

Use [UNNotificationAction](unnotificationaction.md) objects to define the actions that your app can perform in response to a delivered notification. You define the actions that your app supports. For example, a meeting app might define actions for accepting or rejecting a meeting invitation. The action object itself contains the title to display in an action button and the button’s appearance. After creating action objects, add them to a [UNNotificationCategory](unnotificationcategory.md) object and register your categories with the system.

> [!note] Note
> When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [UNNotificationActionOptionDestructive](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

For information on how to define actions and categories, see [Declaring your actionable notification types](declaring-your-actionable-notification-types.md).

### Responding to the Selection of Actions

When the user selects one of your actions in response to a notification, the system notifies the delegate of the shared [UNUserNotificationCenter](unusernotificationcenter.md) object. Specifically, the system calls the [- userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) method of your delegate object. The response object passed to your delegate includes the [identifier](unnotificationaction/identifier.md) string of the action the user selects, which you can use to perform the corresponding task.

For information on how to handle actions, see [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UNTextInputNotificationAction](untextinputnotificationaction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Essentials

- [+ actionWithIdentifier:title:options:](<unnotificationaction/init(identifier_title_options_).md>) — Creates an action object by using the specified title and options.
- [+ actionWithIdentifier:title:options:icon:](<unnotificationaction/init(identifier_title_options_icon_).md>) — Creates an action object by using the specified title, options, and icon.

### Getting Information

- [identifier](unnotificationaction/identifier.md) — The unique string that your app uses to identify the action.
- [title](unnotificationaction/title.md) — The localized string to use as the title of the action.
- [icon](unnotificationaction/icon.md) — The icon associated with the action.

### Getting Options

- [options](unnotificationaction/options.md) — The behaviors associated with the action.
- [UNNotificationActionOptions](unnotificationactionoptions.md) — The behaviors you can apply to an action.

### Initializers

- [init(coder:)](<unnotificationaction/init(coder_).md>)

## See Also

### Notification categories and user actions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md) — Differentiate your notifications and add action buttons to the notification interface.
- [UNNotificationCategory](unnotificationcategory.md) — A type of notification your app supports and the custom actions that the system displays.
- [UNTextInputNotificationAction](untextinputnotificationaction.md) — An action that accepts user-typed text.
