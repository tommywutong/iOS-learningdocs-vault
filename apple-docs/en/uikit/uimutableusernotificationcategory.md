---
title: UIMutableUserNotificationCategory
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationcategory
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationcategory.json'
content_hash: 'sha256:063b3b468fcdf237'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMutableUserNotificationCategory

<sub>Class</sub>

Information about custom actions that your app can perform in response to a local or push notification.

> [!warning] Deprecated
> Use [UNNotificationCategory](../usernotifications/unnotificationcategory.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIMutableUserNotificationCategory
```

## Overview

Use instances of this class to customize the actions included in an alert when space onscreen is constrained.

After creating an instance of this class using the standard alloc/init pattern, use it to modify the actions or category name as needed. The most common use of this class is to specify the subset of actions to display when the size of the alert is relatively small.

## Relationships

- **Inherits From**: [UIUserNotificationCategory](uiusernotificationcategory.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Modifying the action settings

- [identifier](uimutableusernotificationcategory/identifier.md) — The name of the action group. _(deprecated)_
- [- setActions:forContext:](<uimutableusernotificationcategory/setactions(__for_).md>) — Sets the actions to display for different alert styles. _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
- [UIMenuController](uimenucontroller.md) — The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands. _(deprecated)_
- [UIMenuItem](uimenuitem.md) — A custom item in the editing menu managed by the menu controller. _(deprecated)_
- [UIMutableUserNotificationAction](uimutableusernotificationaction.md) — A modifiable version of the user notification action class. _(deprecated)_
- [UIPopoverController](uipopovercontroller.md) — An object that manages the presentation of content in a popover. _(deprecated)_
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
