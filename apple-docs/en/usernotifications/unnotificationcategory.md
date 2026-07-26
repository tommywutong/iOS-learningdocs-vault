---
title: UNNotificationCategory
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationcategory
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcategory.json'
content_hash: 'sha256:0fbdfcadd60f6215'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationCategory

<sub>Class</sub>

A type of notification your app supports and the custom actions that the system displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class UNNotificationCategory
```

## Overview

A [UNNotificationCategory](unnotificationcategory.md) object defines a type of notification that your executable can receive. You create category objects to define your app’s _actionable notifications_ — notifications that have action buttons the user can select in response to the notification. Each category object you create stores the actions and other behaviors associated with a specific type of notification. Register your category objects using the [- setNotificationCategories:](<unusernotificationcenter/setnotificationcategories(__).md>) method of [UNUserNotificationCenter](unusernotificationcenter.md). You can register as many category objects as you need.

> [!note] Note
> When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [UNNotificationActionOptionDestructive](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

To apply category objects to your notifications, include the category’s identifier string in the payload of any notifications you create. For local notifications, put this string in the [categoryIdentifier](unmutablenotificationcontent/categoryidentifier.md) property of the [UNMutableNotificationContent](unmutablenotificationcontent.md) object that you use to specify the notification’s content. For remote notifications, use this string as the value of the `category` key in the `aps` dictionary of your payload.

Categories can have associated actions, which define custom buttons the system displays for notifications of that category. When the system has unlimited space, the system displays up to 10 actions. When the system has limited space, the system displays at most two actions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Essentials

- [+ categoryWithIdentifier:actions:intentIdentifiers:options:](<unnotificationcategory/init(identifier_actions_intentidentifiers_options_).md>) — Creates a category object containing the specified actions and options.
- [+ categoryWithIdentifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:options:](<unnotificationcategory/init(identifier_actions_intentidentifiers_hiddenpreviewsbodyplaceholder_options_).md>) — Creates a category object containing the specified actions, options, and placeholder text used when previews aren’t shown.
- [+ categoryWithIdentifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:categorySummaryFormat:options:](<unnotificationcategory/init(identifier_actions_intentidentifiers_hiddenpreviewsbodyplaceholder_categorysummaryformat_options_).md>) — Creates a category object containing the specified actions, options, placeholder text used when previews aren’t shown, and summary format string.

### Getting the Information

- [identifier](unnotificationcategory/identifier.md) — The unique string assigned to the category.
- [actions](unnotificationcategory/actions.md) — The actions to display when the system delivers notifications of this type.
- [intentIdentifiers](unnotificationcategory/intentidentifiers.md) — The intents related to notifications of this category.
- [hiddenPreviewsBodyPlaceholder](unnotificationcategory/hiddenpreviewsbodyplaceholder.md) — The placeholder text to display when the system disables notification previews for the app.
- [categorySummaryFormat](unnotificationcategory/categorysummaryformat.md) — A format string for the summary description used when the system groups the category’s notifications.

### Getting the Options

- [options](unnotificationcategory/options.md) — Options for how to handle notifications of this type.
- [UNNotificationCategoryOptions](unnotificationcategoryoptions.md) — Constants indicating how to handle notifications associated with this category.

### Initializers

- [init(coder:)](<unnotificationcategory/init(coder_).md>)

## See Also

### Notification categories and user actions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md) — Differentiate your notifications and add action buttons to the notification interface.
- [UNNotificationAction](unnotificationaction.md) — A task your app performs in response to a notification that the system delivers.
- [UNTextInputNotificationAction](untextinputnotificationaction.md) — An action that accepts user-typed text.
