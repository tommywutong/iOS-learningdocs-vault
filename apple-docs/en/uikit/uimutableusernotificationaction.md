---
title: UIMutableUserNotificationAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction.json'
content_hash: 'sha256:7acd24c1f344e361'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMutableUserNotificationAction

<sub>Class</sub>

A modifiable version of the user notification action class.

> [!warning] Deprecated
> Use [UNNotificationAction](../usernotifications/unnotificationaction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIMutableUserNotificationAction
```

## Overview

When a notification is delivered, the system displays a button for each custom action associated with the notification. Tapping a button launches your app (either in the foreground or background) and gives you a chance to perform the indicated action. You use this class to configure the details about the button that is displayed and the information your app needs to perform the corresponding action.

To associate custom actions with a local or remote notification, create one or more instances of this class and use them to configure one or more UIMutableUserNotificationActionSettings objects. An action settings objects defines the set of actions to associate with a single notification. You register your app’s action settings objects at launch time, along with your app’s preferred notification options, using a [UIUserNotificationSettings](uiusernotificationsettings.md) object.

For each action you define, you must specify whether execution of that action requires the app to be running in the foreground or background. You can also specify whether the device must be unlocked or can remain locked while the action is performed. Unlocking the device may be necessary if the action involves reading or writing files that are encrypted on disk using the system’s data protection mechanism. When the user selects an action, the system puts your app into the appropriate mode and calls your app delegate’s [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) or [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<uiapplicationdelegate/application(__handleactionwithidentifier_for_completionhandler_).md>) method to perform the action.

## Relationships

- **Inherits From**: [UIUserNotificationAction](uiusernotificationaction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the action information

- [identifier](uimutableusernotificationaction/identifier.md) — The string that you use internally to identify the action. _(deprecated)_
- [title](uimutableusernotificationaction/title.md) — The localized string to use as the button title for the action. _(deprecated)_

### Configuring the action’s behavior

- [activationMode](uimutableusernotificationaction/activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [authenticationRequired](uimutableusernotificationaction/isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [destructive](uimutableusernotificationaction/isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [behavior](uimutableusernotificationaction/behavior.md) — The custom behavior (if any) that the action supports. _(deprecated)_
- [parameters](uimutableusernotificationaction/parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
- [UIMenuController](uimenucontroller.md) — The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands. _(deprecated)_
- [UIMenuItem](uimenuitem.md) — A custom item in the editing menu managed by the menu controller. _(deprecated)_
- [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
- [UIPopoverController](uipopovercontroller.md) — An object that manages the presentation of content in a popover. _(deprecated)_
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
