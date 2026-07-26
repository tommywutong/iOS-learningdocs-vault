---
title: UNMutableNotificationContent
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent.json'
content_hash: 'sha256:0d373f40e133791b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNMutableNotificationContent

<sub>Class</sub>

The editable content for a notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNMutableNotificationContent
```

## Overview

Create a [UNMutableNotificationContent](unmutablenotificationcontent.md) object when you want to specify the payload for a local notification. Specifically, use this object to specify the title and message for an alert, the sound to play, or the value to assign to your app’s badge. You might also provide details about how the system handles the notification. For example, you can specify a custom launch image and a thread identifier for visually grouping related notifications.

After creating your content object, assign it to a [UNNotificationRequest](unnotificationrequest.md) object, add a trigger condition, and schedule your notification. The trigger condition defines when the system delivers the notification to the user. Listing 1 shows the scheduling of a local notification that displays an alert and plays a sound after a delay of five seconds. Store the strings for the alert’s title and body in the app’s `Localizable.strings` file.

Listing 1. Creating the content for a local notification

**Swift**

```swift
// Configure the notification's payload.
let content = UNMutableNotificationContent()
content.title = NSString.localizedUserNotificationString(forKey: "Hello!", arguments: nil)
content.body = NSString.localizedUserNotificationString(forKey: "Hello_message_body", arguments: nil)
content.sound = UNNotificationSound.default
 
// Deliver the notification in five seconds.
let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5, repeats: false)
let request = UNNotificationRequest(identifier: "FiveSecond", content: content, trigger: trigger) // Schedule the notification.
let center = UNUserNotificationCenter.current()
center.add(request) { (error : Error?) in
     if let theError = error {
         // Handle any errors
     }
}
```

**Objective-C**

```objc
// Configure the notification's payload.
UNMutableNotificationContent *content = [[UNMutableNotificationContent alloc] init];
content.title = [NSString localizedUserNotificationStringForKey:@"Hello!" arguments:nil];
content.body = [NSString localizedUserNotificationStringForKey:@"Hello_message_body" arguments:nil];
content.sound = [UNNotificationSound defaultSound];
 
// Deliver the notification in five seconds.
UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger
            triggerWithTimeInterval:5 repeats:NO];
UNNotificationRequest* request = [UNNotificationRequest requestWithIdentifier:@"FiveSecond"
            content:content trigger:trigger];
 
// Schedule the notification.
UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
[center addNotificationRequest:request];
```

> [!note] Note
> Local notifications always result in user interactions, and the system ignores any interactions for which your app isn’t authorized. For information about how to request authorization for user interactions, see [Asking permission to use notifications](asking-permission-to-use-notifications.md).

### Localizing the Alert Strings

Localize the strings you display in a notification alert for the current user. Although you can use the [NSLocalizedString](../foundation/nslocalizedstring.md) macros to load strings from your app’s resource files, a better option is to specify your string using the [localizedUserNotificationString(forKey:arguments:)](<../foundation/nsstring/localizedusernotificationstring(forkey_arguments_).md>) method of [NSString](../foundation/nsstring.md). The [localizedUserNotificationString(forKey:arguments:)](<../foundation/nsstring/localizedusernotificationstring(forkey_arguments_).md>) method delays the loading of the localized string until the system delivers the notification. If the user changes the language setting before the system delivers a notification, the system updates the alert text to the user’s current language instead of the language in use when the system scheduled the notification.

## Relationships

- **Inherits From**: [UNNotificationContent](unnotificationcontent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Providing the primary content

- [title](unmutablenotificationcontent/title.md) — The localized text that provides the notification’s primary description.
- [subtitle](unmutablenotificationcontent/subtitle.md) — The localized text that provides the notification’s secondary description.
- [body](unmutablenotificationcontent/body.md) — The localized text that provides the notification’s main content.

### Providing supplementary content

- [attachments](unmutablenotificationcontent/attachments.md) — The visual and audio attachments to display alongside the notification’s main content.
- [userInfo](unmutablenotificationcontent/userinfo.md) — The custom data to associate with the notification.

### Configuring app behavior

- [launchImageName](unmutablenotificationcontent/launchimagename.md) — The name of the image or storyboard to use when your app launches because of the notification.
- [badge](unmutablenotificationcontent/badge.md) — The number that your app’s icon displays.
- [targetContentIdentifier](unmutablenotificationcontent/targetcontentidentifier.md) — The value your app uses to determine which scene to display to handle the notification.

### Integrating with the system

- [sound](unmutablenotificationcontent/sound.md) — The sound that plays when the system delivers the notification.
- [interruptionLevel](unmutablenotificationcontent/interruptionlevel.md) — The notification’s importance and required delivery timing.
- [UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [relevanceScore](unmutablenotificationcontent/relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
- [filterCriteria](unmutablenotificationcontent/filtercriteria.md) — The criteria the system evaluates to determine if it displays the notification in the current Focus.

### Grouping notifications

- [threadIdentifier](unmutablenotificationcontent/threadidentifier.md) — The identifier that groups related notifications.
- [categoryIdentifier](unmutablenotificationcontent/categoryidentifier.md) — The identifier of the notification’s category.
- [summaryArgument](unmutablenotificationcontent/summaryargument.md) — The text the system adds to the notification summary to provide additional context. _(deprecated)_
- [summaryArgumentCount](unmutablenotificationcontent/summaryargumentcount.md) — The number the system adds to the notification summary when the notification represents multiple items. _(deprecated)_

### Instance Properties

- [appEntityIdentifiers](unmutablenotificationcontent/appentityidentifiers.md) _(beta)_

## See Also

### Notification content

- [Implementing communication notifications](implementing-communication-notifications.md) — Configure and display your app’s communication notifications by using intents.
- [UNNotificationContentProviding](unnotificationcontentproviding.md) — A protocol the system uses to provide context relevant to user notifications.
- [UNNotificationActionIcon](unnotificationactionicon.md) — An icon associated with an action.
- [UNNotificationContent](unnotificationcontent.md) — The uneditable content of a notification.
- [UNNotificationAttachment](unnotificationattachment.md) — A media file associated with a notification.
- [UNNotificationSound](unnotificationsound.md) — The sound played upon delivery of a notification.
- [UNNotificationSoundName](unnotificationsoundname.md) — A string providing the name of a sound file.
