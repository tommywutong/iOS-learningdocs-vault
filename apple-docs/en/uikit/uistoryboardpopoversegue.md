---
title: UIStoryboardPopoverSegue
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardpopoversegue
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardpopoversegue.json'
content_hash: 'sha256:506d11d06e9ff240'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStoryboardPopoverSegue

<sub>Class</sub>

A specific type of segue for presenting content in a popover.

> [!warning] Deprecated
> Instead, access the [popoverPresentationController](uiviewcontroller/popoverpresentationcontroller.md) property of the [destinationViewController](uistoryboardsegue/destination.md) view controller from [- perform](<uistoryboardsegue/perform().md>).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor class UIStoryboardPopoverSegue
```

## Overview

For popover segues, the destination view controller contains the content to be displayed in the popover. This class provides an additional [popoverController](uistoryboardpopoversegue/popovercontroller.md) property so that your custom code has access to the popover controller object. For example, you might want to store the popover controller elsewhere in your code so that you can dismiss the popover programmatically.

## Relationships

- **Inherits From**: [UIStoryboardSegue](uistoryboardsegue.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the segue attributes

- [popoverController](uistoryboardpopoversegue/popovercontroller.md) — The popover controller used to display the destination view controller. _(deprecated)_

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
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
