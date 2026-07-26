---
title: UILocalNotification
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification.json'
content_hash: 'sha256:272bf0b5edea60fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILocalNotification

<sub>Class</sub>

A notification that an app can schedule for presentation at a specific date and time.

> [!warning] Deprecated
> Use [UNNotificationRequest](../usernotifications/unnotificationrequest.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
@MainActor class UILocalNotification
```

## Overview

The operating system is responsible for delivering local notifications at their scheduled times; the app does not have to be running for this to happen. Although local notifications are similar to remote notifications in that they are used for displaying alerts, playing sounds, and badging app icons, they are composed and delivered locally and do not require connection with remote servers.

Local notifications are primarily intended for apps with timer-based behaviors and simple calendar or to-do list apps. An app that is running in the background may also schedule a local notification to inform the user of an incoming message, chat, or update. An app can have only a limited number of scheduled notifications; the system keeps the soonest-firing 64 notifications (with automatically rescheduled notifications counting as a single notification) and discards the rest.

When you create a local notification, you must specify either a specific date or a geographic region as the trigger for delivering the notification. Date-based notifications are delivered at the day and time you specify, and allowances can be made for time zone changes as needed. Region-based notifications are delivered when the user enters or exits the specified region. In both cases, you can specify whether the notifications are one-time events or can be rescheduled and delivered again.

After creating a `UILocalNotification` object, schedule it using either the [- scheduleLocalNotification:](<uiapplication/schedulelocalnotification(__).md>) or [- presentLocalNotificationNow:](<uiapplication/presentlocalnotificationnow(__).md>) method of the [UIApplication](uiapplication.md) class. The [- scheduleLocalNotification:](<uiapplication/schedulelocalnotification(__).md>) method uses the fire date to schedule delivery; the [- presentLocalNotificationNow:](<uiapplication/presentlocalnotificationnow(__).md>) method presents the notification immediately, regardless of the value of `fireDate`. You can cancel one or more local notifications using the [- cancelLocalNotification:](<uiapplication/cancellocalnotification(__).md>) or [- cancelAllLocalNotifications](<uiapplication/cancelalllocalnotifications().md>) method of the [UIApplication](uiapplication.md) object.

When the system delivers a local notification, several things can happen, depending on the app state and the type of notification. If the app is not frontmost and visible, the system displays the alert message, badges the app, and plays a sound—whatever is specified in the notification. If the notification is an alert and the user taps the action button (or, if the device is locked, drags open the action slider), the app is woken up or launched. (If the user taps one of the custom actions you specify using the [category](uilocalnotification/category.md) property, the app is woken up or launched into the background.) In its [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) method, the app delegate can obtain the `UILocalNotification` object from the launch options dictionary using the [UIApplicationLaunchOptionsLocalNotificationKey](uiapplication/launchoptionskey/localnotification.md) key. The delegate can inspect the properties of the notification and, if the notification includes custom data in its [userInfo](uilocalnotification/userinfo.md) dictionary, it can access that data and process it accordingly. On the other hand, if the local notification only badges the app icon, and the user in response launches the app, the [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) method is called, but no `UILocalNotification` object is included in the options dictionary. When the user selects a custom action, the app delegate’s [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_for_completionhandler_).md>) method is called to handle the action.

If the app is foremost and visible when the system delivers the notification, the app delegate’s [- application:didReceiveLocalNotification:](<uiapplicationdelegate/application(__didreceive_).md>) is called to process the notification. Use the information in the provided `UILocalNotification` object to decide what action to take. The system does not display any alerts, badge the app’s icon, or play any sounds when the app is already frontmost.

An app is responsible for managing the badge number displayed on its icon. For example, if a text-messaging app processes all incoming messages after receiving a local notification, it should remove the icon badge by setting the [applicationIconBadgeNumber](uiapplication/applicationiconbadgenumber.md) property of the [UIApplication](uiapplication.md) object to 0.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Scheduling a local notification

- [fireDate](uilocalnotification/firedate.md) — The date and time when the system should deliver the notification. _(deprecated)_
- [timeZone](uilocalnotification/timezone.md) — The time zone of the notification’s fire date. _(deprecated)_
- [repeatInterval](uilocalnotification/repeatinterval.md) — The calendar interval at which to reschedule the notification. _(deprecated)_
- [repeatCalendar](uilocalnotification/repeatcalendar.md) — The calendar the system should refer to when it reschedules a repeating notification. _(deprecated)_
- [region](uilocalnotification/region.md) — The geographic region that triggers the notification. _(deprecated)_
- [regionTriggersOnce](uilocalnotification/regiontriggersonce.md) — A Boolean value indicating whether crossing a geographic region boundary delivers only one notification. _(deprecated)_

### Composing the alert

- [alertBody](uilocalnotification/alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertAction](uilocalnotification/alertaction.md) — The title of the action button or slider. _(deprecated)_
- [alertTitle](uilocalnotification/alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [hasAction](uilocalnotification/hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [alertLaunchImage](uilocalnotification/alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
- [category](uilocalnotification/category.md) — The name of a group of actions to display in the alert. _(deprecated)_

### Configuring other parts of the notification

- [applicationIconBadgeNumber](uilocalnotification/applicationiconbadgenumber.md) — The number to display as the app’s icon badge. _(deprecated)_
- [soundName](uilocalnotification/soundname.md) — The name of the file containing the sound to play when an alert is displayed. _(deprecated)_
- [userInfo](uilocalnotification/userinfo.md) — A dictionary for passing custom information to the notified app. _(deprecated)_

### Constants

- [Notification sound](notification-sound.md) — The default system sound for local notifications.

### Initializers

- [- init](<uilocalnotification/init().md>) _(deprecated)_
- [- initWithCoder:](<uilocalnotification/init(coder_).md>) _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UIMenuController](uimenucontroller.md) — The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands. _(deprecated)_
- [UIMenuItem](uimenuitem.md) — A custom item in the editing menu managed by the menu controller. _(deprecated)_
- [UIMutableUserNotificationAction](uimutableusernotificationaction.md) — A modifiable version of the user notification action class. _(deprecated)_
- [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
- [UIPopoverController](uipopovercontroller.md) — An object that manages the presentation of content in a popover. _(deprecated)_
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
