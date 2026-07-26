---
title: 'updating(from:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationcontent/updating(from:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationcontent/updating(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationcontent/updating%28from%3A%29.json'
content_hash: 'sha256:f9e71b1950b0ca1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationContent](../unnotificationcontent.md)

# updating(from:)

<sub>Instance Method</sub>

Returns a copy of the notification that includes content from the specified provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updating(from provider: any UNNotificationContentProviding) throws -> UNNotificationContent
```

## Parameters

- `provider` — The notification content providing object.

## Return Value

The notification content object for the content handler.

## Discussion

The system contextualizes your [UNNotificationContent](../unnotificationcontent.md) object with other Apple SDK objects conforming to [UNNotificationContentProviding](../unnotificationcontentproviding.md). The system specializes the notification and decorates its look and behavior accordingly.

For example, the system treats the notification as a message with an avatar and promotes it to the top of notification center if the object passed in is a valid [INSendMessageIntent](../../intents/insendmessageintent.md) that conforms to `UNNotificationContentProviding`. The system throws an error with a [Code](../unerror/code.md), if the `UNNotificationContentProviding` object is invalid. Pass the valid `UNNotificationContent` result directly to [UNUserNotificationCenter](../unusernotificationcenter.md) without mutating.

Add this call to the [UNNotificationServiceExtension](../unnotificationserviceextension.md) in [- didReceiveNotificationRequest:withContentHandler:](<../unnotificationserviceextension/didreceive(__withcontenthandler_).md>). Your app passes the returned `UNNotificationContent` to the `contentHandler` for incoming push notifications.
