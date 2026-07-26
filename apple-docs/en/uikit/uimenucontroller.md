---
title: UIMenuController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller.json'
content_hash: 'sha256:974623e47790f3de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMenuController

<sub>Class</sub>

The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.

> [!warning] Deprecated
> Use [UIEditMenuInteraction](uieditmenuinteraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIMenuController
```

## Overview

The singleton [UIMenuController](uimenucontroller.md) instance is referred to as the editing menu. When you make this menu visible, [UIMenuController](uimenucontroller.md) positions it relative to a target rectangle on the screen; this rectangle usually defines a selection. The menu appears above the target rectangle or, if there isn’t enough space for it, below it. The menu’s pointer is placed at the center of the top or bottom of the target rectangle, as appropriate. Be sure to set the tracking rectangle before you make the menu visible. You’re also responsible for detecting, tracking, and displaying selections.

The [UIResponderStandardEditActions](uiresponderstandardeditactions.md) informal protocol declares methods that are invoked when the user taps a menu command. The [- canPerformAction:withSender:](<uiresponder/canperformaction(__withsender_).md>) method of [UIResponder](uiresponder.md) is also related to the editing menu. A responder implements this method to enable and disable commands of the editing menu just before the menu is displayed. You can force the menu commands enabled state to update by calling the [- update](<uimenucontroller/update().md>) method.

You can also provide your own menu items via the [menuItems](uimenucontroller/menuitems.md) property. When you modify the menu items, you can use the [- update](<uimenucontroller/update().md>) method to force the menu to update its display.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the menu controller instance

- [sharedMenuController](uimenucontroller/shared.md) — Returns the menu controller. _(deprecated)_

### Showing and hiding the menu

- [- showMenuFromView:rect:](<uimenucontroller/showmenu(from_rect_).md>) _(deprecated)_
- [- hideMenuFromView:](<uimenucontroller/hidemenu(from_).md>) _(deprecated)_
- [- hideMenu](<uimenucontroller/hidemenu().md>) _(deprecated)_
- [menuVisible](uimenucontroller/ismenuvisible.md) — The visibility of the editing menu. _(deprecated)_
- [- setMenuVisible:animated:](<uimenucontroller/setmenuvisible(__animated_).md>) — Shows or hides the editing menu, optionally animating the action. _(deprecated)_

### Positioning the menu

- [menuFrame](uimenucontroller/menuframe.md) — Returns the frame of the editing menu. _(deprecated)_
- [arrowDirection](uimenucontroller/arrowdirection-swift.property.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [ArrowDirection](uimenucontroller/arrowdirection-swift.enum.md) — The direction the arrow of the editing menu is pointing. _(deprecated)_
- [- setTargetRect:inView:](<uimenucontroller/settargetrect(__in_).md>) — Sets the area in a view above or below which the editing menu is positioned. _(deprecated)_

### Updating the menu

- [- update](<uimenucontroller/update().md>) — Updates the appearance and enabled state of menu commands. _(deprecated)_

### Customizing menu items

- [menuItems](uimenucontroller/menuitems.md) — The custom menu items for the editing menu. _(deprecated)_

### Notifications

- [UIMenuControllerWillShowMenuNotification](uimenucontroller/willshowmenunotification.md) — Posted by the menu controller just before it shows the menu. _(deprecated)_
- [UIMenuControllerDidShowMenuNotification](uimenucontroller/didshowmenunotification.md) — Posted by the menu controller just after it shows the menu. _(deprecated)_
- [UIMenuControllerWillHideMenuNotification](uimenucontroller/willhidemenunotification.md) — Posted by the menu controller just before it hides the menu. _(deprecated)_
- [UIMenuControllerDidHideMenuNotification](uimenucontroller/didhidemenunotification.md) — Posted by the menu controller just after it hides the menu. _(deprecated)_
- [UIMenuControllerMenuFrameDidChangeNotification](uimenucontroller/menuframedidchangenotification.md) — Posted when the frame of a visible menu changes. _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
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
