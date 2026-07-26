---
title: 'init(identifier:title:options:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationaction/init(identifier:title:options:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction/init(identifier:title:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction/init%28identifier%3Atitle%3Aoptions%3A%29.json'
content_hash: 'sha256:80743699e306824f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAction](../unnotificationaction.md)

# init(identifier:title:options:)

<sub>Initializer</sub>

Creates an action object by using the specified title and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
convenience init(identifier: String, title: String, options: UNNotificationActionOptions = [])
```

## Parameters

- `identifier` — The string that you use internally to identify the action. This string must be unique among your app’s supported actions. When the user selects the action, the system passes this string to your app and asks the user to perform the related task. This parameter must not be `nil` or an empty string.

- `title` — The localized string the system displays to the user. The system displays this string as the title of a button, which the system adds to the notification interface. This parameter must not be `nil`.

- `options` — Additional options that describe how the action behaves. Include options when you need the related behavior. For a list of possible values, see [UNNotificationActionOptions](../unnotificationactionoptions.md).

## Return Value

An action object that the system initializes.

## See Also

### Essentials

- [+ actionWithIdentifier:title:options:icon:](<init(identifier_title_options_icon_).md>) — Creates an action object by using the specified title, options, and icon.
