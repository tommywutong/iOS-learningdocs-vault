---
title: UIPopoverController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller.json'
content_hash: 'sha256:1cd2c4f6380d6874'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPopoverController

<sub>Class</sub>

An object that manages the presentation of content in a popover.

> [!warning] Deprecated
> In iOS 9 and later, a popover is implemented as a [UIViewController](uiviewcontroller.md) presentation. To create a popover, [UIPopoverPresentationController](uipopoverpresentationcontroller.md) and specify the [UIModalPresentationPopover](uimodalpresentationstyle/popover.md) style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor class UIPopoverController
```

## Overview

The `UIPopoverController` class is used to manage the presentation of content in a popover. You use popovers to present information temporarily. The popover content is layered on top of your existing content and the background is dimmed automatically. The popover remains visible until the user taps outside of the popover window or you explicitly dismiss it. Popover controllers are for use exclusively on iPad devices. Attempting to create one on other devices results in an exception.

To display a popover, create an instance of this class and present it using one of the appropriate methods. When initializing an instance of this class, you must specify the view controller that provides the content for the popover. Popovers normally derive their size from the view controller they present. However, you can change the size of the popover by modifying the value in the [popoverContentSize](uipopovercontroller/contentsize.md) property or by calling the [- setPopoverContentSize:animated:](<uipopovercontroller/setcontentsize(__animated_).md>) method. The latter approach is particularly effective if you need to animate changes to the popover’s size. The size you specify is just the preferred size for the popover’s view. The actual size may be altered to ensure that the popover fits on the screen and does not collide with the keyboard.

When displayed, taps outside of the popover window cause the popover to be dismissed automatically. To allow the user to interact with the specified views and not dismiss the popover, you can assign one or more views to the [passthroughViews](uipopovercontroller/passthroughviews.md) property. Taps inside the popover window do not automatically cause the popover to be dismissed. Your view and view controller code must handle actions and events inside the popover explicitly and call the [- dismissPopoverAnimated:](<uipopovercontroller/dismiss(animated_).md>) method as needed.

If the user rotates the device while a popover is visible, the popover controller hides the popover and then shows it again at the end of the rotation. The popover controller attempts to position the popover appropriately for you but you can also implement the [- popoverController:willRepositionPopoverToRect:inView:](<uipopovercontrollerdelegate/popovercontroller(__willrepositionpopoverto_in_).md>) method in the popover delegate to specify a new position.

You can assign a delegate to the popover to manage interactions with the popover and receive notifications about its dismissal. For information about the methods of the delegate object, see [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIAppearanceContainer](uiappearancecontainer.md)

## Topics

### Initializing the popover

- [- initWithContentViewController:](<uipopovercontroller/init(contentviewcontroller_).md>) — Returns an initialized popover controller object. _(deprecated)_

### Presenting and dismissing the popover

- [- presentPopoverFromRect:inView:permittedArrowDirections:animated:](<uipopovercontroller/present(from_in_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified location in the view. _(deprecated)_
- [- presentPopoverFromBarButtonItem:permittedArrowDirections:animated:](<uipopovercontroller/present(from_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified bar button item. _(deprecated)_
- [- dismissPopoverAnimated:](<uipopovercontroller/dismiss(animated_).md>) — Dismisses the popover programmatically. _(deprecated)_

### Configuring the popover content

- [contentViewController](uipopovercontroller/contentviewcontroller.md) — The view controller responsible for the content portion of the popover. _(deprecated)_
- [- setContentViewController:animated:](<uipopovercontroller/setcontentview(__animated_).md>) — Sets the view controller responsible for the content portion of the popover. _(deprecated)_
- [popoverContentSize](uipopovercontroller/contentsize.md) — The size of the popover’s content view. _(deprecated)_
- [- setPopoverContentSize:animated:](<uipopovercontroller/setcontentsize(__animated_).md>) — Changes the size of the popover’s content view. _(deprecated)_
- [passthroughViews](uipopovercontroller/passthroughviews.md) — An array of views that the user can interact with while the popover is visible. _(deprecated)_

### Getting the popover attributes

- [popoverVisible](uipopovercontroller/ispopovervisible.md) — A Boolean value indicating whether the popover is currently visible. _(deprecated)_
- [popoverArrowDirection](uipopovercontroller/arrowdirection.md) — The direction of the popover’s arrow. _(deprecated)_

### Accessing the delegate

- [delegate](uipopovercontroller/delegate.md) — The delegate you want to receive popover controller messages. _(deprecated)_

### Customizing the popover appearance

- [popoverLayoutMargins](uipopovercontroller/layoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover. _(deprecated)_
- [popoverBackgroundViewClass](uipopovercontroller/backgroundviewclass.md) — The class to use for displaying the popover background content. _(deprecated)_
- [backgroundColor](uipopovercontroller/backgroundcolor.md) — The color of the popover’s backdrop view. _(deprecated)_

### Constants

- [UIPopoverArrowDirection](uipopoverarrowdirection.md) — Constants for specifying the direction of the popover arrow.

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
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
