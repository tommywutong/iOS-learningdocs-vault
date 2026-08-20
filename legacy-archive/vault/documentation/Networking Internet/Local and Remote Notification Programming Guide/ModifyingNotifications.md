---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/ModifyingNotifications.html
archived_at: '2026-07-15T08:19:07.776932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Modifying and Presenting Notifications

You can modify the content or presentation of arriving notifications using app extensions. To modify the content of a remote notification before it is delivered, use a notification service app extension. To change how the notification’s content is presented onscreen, use a notification content app extension.

### Modifying the Payload of a Remote Notification

Use a notification service app extension to modify the payload of a remote notification before it is delivered to the user. Remote notifications originate from a server, which has control over the configuration and contents of the notification. A service extension lets your app make changes to the server-provided payload data before that data is presented to the user. You use service extensions to implement the following types of behaviors:

- Decrypt data that was delivered in an encrypted format.
- Download images or other media files and add them as attachments to the notification.
- Change the body or title text of the notification.
- Add a thread identifier to the notification or modify the contents of the notification’s [userInfo](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649869-userinfo) dictionary.

__To add a notification service app extension to your iOS app__

1. In Xcode, select New > Target to add a new target to your project.
2. In the iOS > Application Extension section, select the Notification Service Extension target.
3. Click Next.
4. Specify the name and other details for your app extension.
5. Click Finish.

Xcode adds a preconfigured target to your app project.

The default notification service extension target provided by Xcode contains a subclass of the `UNNotificationServiceExtension` class for you to modify. Use the [didReceiveNotificationRequest:withContentHandler:](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648229-didreceivenotificationrequest) method to create and configure a new [UNMutableNotificationContent](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent) object. You can make any changes you want to the new content object, replacing some or all of the original content values. When you are done, call the provided completion handler with your new content object. The system integrates your new content into the notification and delivers it to the user.

The system gives you a limited amount of time to modify the notification and call the provided completion handler, so you should perform any tasks quickly. If your `didReceiveNotificationRequest:withContentHandler:` method takes too long to call the completion handler, the system calls the [serviceExtensionTimeWillExpire](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648227-serviceextensiontimewillexpire) method to give you one final opportunity to finish your modifications. If you do not call the completion handler in time, the system displays the notification’s original content.

Remote notifications sent by your server must be crafted explicitly to support modification by a notification service app extension. Notifications that do not include the proper modifications are delivered directly to the user without modification. When creating the payload for the remote notification, your server should do the following:

- Include the `mutable-content` key with a value of 1.
- Include an `alert` dictionary with subkeys for the `title` and `body` of the alert.

For more information about implementing the methods of your notification service app extension, see _[UNNotificationServiceExtension Class Reference](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension)_. For information about configuring the payload for remote notifications, see [Creating the Remote Notification Payload](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvomi).

### Presenting Notifications Using a Custom Interface on iOS

Use a notification content app extension to display a custom user interface for your app’s notifications. You use an extension of this type to incorporate custom content or to use a different layout than the default interface. For example, you might use this type of extension to display images or media files inline with your notifications.

A notification content app extension supports the presentation of local and remote notifications associated with a specific category. You specify the category for a local notification using the [categoryIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649866-categoryidentifier) of your `UNNotificationContent` object. For remote notifications, your server includes a `category` key with an appropriate value in the `aps` dictionary of the payload. When a notification with that category arrives, the system loads the view controller from your extension and incorporates your content into the system interfaces. You use the notification contents to configure your view controller before it appears onscreen.

__To add a notification content app extension to your iOS app__

1. In Xcode, select New > Target to add a new target to your project.
2. In the iOS > Application Extension section, select the Notification Content Extension target.
3. Click Next.
4. Specify the name and other details for your app extension.
5. Click Finish.

Xcode adds a preconfigured target to your app project.

The initial notification content app extension target is configured to present notifications associated with a single category. You must modify your target to specify which category of notifications you want to support with each extension. You specify the category using the `UNNotificationExtensionCategory` key in your target’s `Info.plist` file. Set the value of the key to the same string in the [identifier](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/1649276-identifier) property of the `UNNotificationCategory` object that your app registers at launch time.

__To support multiple notification categories with your app extension__

1. Select the `Info.plist` file of your notification content extension project.
2. Expand the `NSExtension` dictionary to view the extension-related keys.
3. Expand the `NSExtensionAttributes` dictionary.
4. Change the type of the `UNNotificationExtensionCategory` key to Array.
5. Add one entry for notification category that the extension handles.

You may include multiple notification content app extensions in your iOS app bundle. The system expects only one extension to support a given category, so you must configure the `UNNotificationExtensionCategory` key of each extension with a different set of values.

For more information about implementing your notification content app extension, see _[UNNotificationContentExtension Protocol Reference](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension)_.

### Presenting Notifications Using a Custom Interface on watchOS

The WatchKit framework provides direct support for presenting notifications using a custom interface. A WatchKit extension may include one or more notification interface controllers to display when notifications arrive for your app. You use these interface controllers to present the content of your notifications. For information on how to implement a notification interface controller, see _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_.

[Configuring Remote Notification Support](HandlingRemoteNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknltc)

[APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)
