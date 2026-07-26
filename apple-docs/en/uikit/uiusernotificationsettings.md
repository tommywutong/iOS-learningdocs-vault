---
title: UIUserNotificationSettings
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationsettings
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationsettings.json'
content_hash: 'sha256:9ef12dc9ffe89f63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationSettings

<sub>Class</sub>

The types of notifications that can be displayed to the user by your app.

> [!warning] Deprecated
> Use [UNNotificationSettings](../usernotifications/unnotificationsettings.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIUserNotificationSettings
```

## Overview

Apps that use visible or audible alerts in conjunction with a local or push notification must register the types of alerts they employ. UIKit correlates the information you provide with the user’s preferences to determine what types of alerts your app is allowed to employ.

Use this class to encapsulate your initial registration request and to view the request results. After creating an instance of this class and specifying your preferred settings, call the [- registerUserNotificationSettings:](<uiapplication/registerusernotificationsettings(__).md>) method of the [UIApplication](uiapplication.md) class to register those settings. After checking your request against the user preferences, the app delivers the results to the [- application:didRegisterUserNotificationSettings:](<uiapplicationdelegate/application(__didregister_).md>) method of its app delegate. The object passed to that method specifies the types of notifications that your app is allowed to use.

In addition to registering your app’s alert types, you can also use this class to register groups of custom actions to display in conjunction with local or push notifications. Custom actions represent immediate tasks your app can perform in response to the notification. You define groups of actions and associate the entire group with a given notification. When the corresponding alert is displayed, the system adds buttons for each action you specified. When the user taps the button for one of the actions, the system wakes your app and calls the [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) or [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_for_completionhandler_).md>) method of its app delegate. Use those methods to perform the requested action.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a settings object

- [+ settingsForTypes:categories:](<uiusernotificationsettings/init(types_categories_).md>) — Creates and returns a settings object that you can use to register your requested notification and action types. _(deprecated)_

### Getting the configured settings

- [types](uiusernotificationsettings/types.md) — A bitmask of the notification types that your app is allowed to use. _(deprecated)_
- [categories](uiusernotificationsettings/categories.md) — The app’s registered groups of actions. _(deprecated)_

### Constants

- [UIUserNotificationType](uiusernotificationtype.md) — Constants indicating how the app alerts the user when a local or push notification arrives. _(deprecated)_

### Initializers

- [init(forTypes:categories:)](<uiusernotificationsettings/init(fortypes_categories_).md>) _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
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
