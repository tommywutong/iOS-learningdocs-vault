---
title: UNNotificationServiceExtension
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationserviceextension
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationserviceextension.json'
content_hash: 'sha256:1cc70e944f233ca9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationServiceExtension

<sub>Class</sub>

An object that modifies the content of a remote notification before it’s delivered to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class UNNotificationServiceExtension
```

## Overview

A [UNNotificationServiceExtension](unnotificationserviceextension.md) object provides the entry point for a notification service app extension. This object lets you customize the content of a remote notification before the system delivers it to the user. A notification service app extension doesn’t present any UI of its own. Instead, it’s launched on demand when the system delivers a notification of the appropriate type to the user’s device. You use this extension to modify the notification’s content or download content related to the extension. For example, you could use the extension to decrypt an encrypted data block or to download images associated with the notification.

You don’t create [UNNotificationServiceExtension](unnotificationserviceextension.md) objects yourself. Instead, the Xcode template for a notification service extension target contains a subclass for you to modify. Use the methods of that subclass to implement your app extension’s behavior. When your app receives a remote notification for your app, the system loads your extension and calls its [- didReceiveNotificationRequest:withContentHandler:](<unnotificationserviceextension/didreceive(__withcontenthandler_).md>) method given the following conditions:

- Your app has configured the remote notification to display an alert.
- The remote notification’s `aps` dictionary includes the `mutable-content` key with the value set to `1`.

> [!note] Note
> You can’t modify silent notifications or those that only play a sound or badge the app’s icon.

The [- didReceiveNotificationRequest:withContentHandler:](<unnotificationserviceextension/didreceive(__withcontenthandler_).md>) method performs the main work of your extension. You use that method to make any changes to the notification’s content. That method has a limited amount of time to perform its task and execute the provided completion block. If your method doesn’t finish in time, the system calls the [- serviceExtensionTimeWillExpire](<unnotificationserviceextension/serviceextensiontimewillexpire().md>) method to give you one last chance to submit your changes. If you don’t update the notification content before time expires, the system displays the original content.

As for any app extension, you deliver a notification service app extension class as a bundle inside your app. The template that Xcode provides configures the `Info.plist` file automatically for this app extension type. Specifically, it sets the value of the [NSExtensionPointIdentifier](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW15) key to `com.apple.usernotifications.service` and sets the value of the [NSExtensionPrincipalClass](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW16) key to the name of your [UNNotificationServiceExtension](unnotificationserviceextension.md) subclass.

For information about how to set up and send remote notifications, see [Setting up a remote notification server](setting-up-a-remote-notification-server.md).

### Subclassing Notes

The Xcode templates provide a subclass of [UNNotificationServiceExtension](unnotificationserviceextension.md) for you to modify. You must implement the [- didReceiveNotificationRequest:withContentHandler:](<unnotificationserviceextension/didreceive(__withcontenthandler_).md>) method and use it to process incoming notifications. It’s also strongly recommended that you override the [- serviceExtensionTimeWillExpire](<unnotificationserviceextension/serviceextensiontimewillexpire().md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Processing Notifications

- [- didReceiveNotificationRequest:withContentHandler:](<unnotificationserviceextension/didreceive(__withcontenthandler_).md>) — Asks you to make any needed changes to the notification and notify the system when you’re done.
- [- serviceExtensionTimeWillExpire](<unnotificationserviceextension/serviceextensiontimewillexpire().md>) — Tells you that the system is terminating your extension.

## See Also

### Notification service app extension

- [Modifying content in newly delivered notifications](modifying-content-in-newly-delivered-notifications.md) — Modify the payload of a remote notification before it’s displayed on the user’s iOS device.
