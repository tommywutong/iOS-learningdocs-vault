---
title: UNUserNotificationCenterDelegate
framework: User Notifications
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unusernotificationcenterdelegate
source_url: 'https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unusernotificationcenterdelegate.json'
content_hash: 'sha256:39eddd13f15021e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNUserNotificationCenterDelegate

<sub>Protocol</sub>

An interface for processing incoming notifications and responding to notification actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UNUserNotificationCenterDelegate : NSObjectProtocol
```

## Overview

Use the methods of the [UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md) protocol to handle user-selected actions from notifications, and to process notifications that arrive when your app is running in the foreground. After implementing these methods in an object, assign that object to the [delegate](unusernotificationcenter/delegate.md) property of the shared [UNUserNotificationCenter](unusernotificationcenter.md) object. The user notification center object calls the methods of your delegate at appropriate times.

> [!important] Important
> You must assign your delegate object to the [UNUserNotificationCenter](unusernotificationcenter.md) object before your app finishes launching. For example, in an iOS app, you must assign it in the [application(_:willFinishLaunchingWithOptions:)](<../uikit/uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) or [application(_:didFinishLaunchingWithOptions:)](<../uikit/uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) method of your app delegate. Assigning a delegate after the system calls these methods might cause you to miss incoming notifications.

For information about the shared user notification center object, see [UNUserNotificationCenter](unusernotificationcenter.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### First Steps

- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md) — Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.

### Handling the Selection of Custom Actions

- [- userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) — Asks the delegate to process the user’s response to a delivered notification.

### Receiving Notifications

- [- userNotificationCenter:willPresentNotification:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__willpresent_withcompletionhandler_).md>) — Asks the delegate how to handle a notification that arrived while the app was running in the foreground.
- [UNNotificationPresentationOptions](unnotificationpresentationoptions.md) — Constants indicating how to present a notification in a foreground app.

### Displaying Notification Settings

- [- userNotificationCenter:openSettingsForNotification:](<unusernotificationcenterdelegate/usernotificationcenter(__opensettingsfor_).md>) — Asks the delegate to display the in-app notification settings.

## See Also

### Notification management

- [UNUserNotificationCenter](unusernotificationcenter.md) — The central object for managing notification-related activities for your app or app extension.
- [UNNotificationSettings](unnotificationsettings.md) — The object for managing notification-related settings and the authorization status of your app.
