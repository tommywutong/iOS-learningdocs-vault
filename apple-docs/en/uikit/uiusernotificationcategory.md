---
title: UIUserNotificationCategory
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationcategory
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationcategory.json'
content_hash: 'sha256:206169c3f6519781'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationCategory

<sub>Class</sub>

Information about custom actions that your app can perform in response to a local or push notification.

> [!warning] Deprecated
> Use [UNNotificationCategory](../usernotifications/unnotificationcategory.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIUserNotificationCategory
```

## Overview

Each instance of `UIUserNotificationCategory` represents a group of actions to display in conjunction with a single notification. The title of each action is uses as the title of a button in the alert displayed to the user. When the user taps a button, the system reports the selected action to your app delegate.

Typically, you create an instance of the [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md) class instead of this class. You use the mutable object to add actions and specify a category name before registering them with a [UIUserNotificationSettings](uiusernotificationsettings.md) object.

To display a group of actions for a specific notification, configure the local or push notification with the category name of the group. For local notifications, you specify this name when configuring your [UILocalNotification](uilocalnotification.md) object. For push notifications, your server specifies a group of actions by adding a `category` key (whose value is the [identifier](uiusernotificationcategory/identifier.md) of the group) to the push notification’s payload.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating the action group

- [- init](<uiusernotificationcategory/init().md>) — Creates an action group. _(deprecated)_
- [- initWithCoder:](<uiusernotificationcategory/init(coder_).md>) — Creates an action group from data in an unarchiver. _(deprecated)_

### Getting the group configuration

- [identifier](uiusernotificationcategory/identifier.md) — The name of the action group. _(deprecated)_
- [- actionsForContext:](<uiusernotificationcategory/actions(for_).md>) — Returns the actions to be displayed for the given notification context. _(deprecated)_

### Constants

- [UIUserNotificationActionContext](uiusernotificationactioncontext.md) — Constants indicating the amount of space available for displaying actions in a notification. _(deprecated)_

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
