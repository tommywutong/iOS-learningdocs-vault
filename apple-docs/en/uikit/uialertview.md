---
title: UIAlertView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertview
source_url: 'https://developer.apple.com/documentation/uikit/uialertview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview.json'
content_hash: 'sha256:1cda91a85709f533'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAlertView

<sub>Class</sub>

A view that displays an alert message.

> [!warning] Deprecated
> Instead, use [UIAlertController](uialertcontroller.md) with a [preferredStyle](uialertcontroller/preferredstyle.md) of [UIAlertControllerStyleAlert](uialertcontroller/style/alert.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIAlertView
```

## Overview

In apps that run in versions of iOS prior to iOS 8, use the [UIAlertView](uialertview.md) class to display an alert message to the user. An alert view functions similar to but differs in appearance from an action sheet (an instance of [UIActionSheet](uiactionsheet.md)).

### Using an alert view

Use the properties and methods defined in this class to set the title, message, and delegate of an alert view and configure the buttons in apps that run in versions of iOS prior to iOS 8. You must set a delegate if you add custom buttons. The delegate should conform to the [UIAlertViewDelegate](uialertviewdelegate.md) protocol. Use the [- show](<uialertview/show().md>) method to display an alert view after it’s configured.

### Subclassing notes

The [UIAlertView](uialertview.md) class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating alert views

- [- initWithTitle:message:delegate:cancelButtonTitle:otherButtonTitles:](<uialertview/init(title_message_delegate_cancelbuttontitle_).md>) — Convenience method for initializing an alert view. _(deprecated)_
- [init(title:message:delegate:cancelButtonTitle:otherButtonTitles:_:)](<uialertview/init(title_message_delegate_cancelbuttontitle_otherbuttontitles___).md>) — Creates an alert view with the specified values. _(deprecated)_
- [- initWithFrame:](<uialertview/init(frame_).md>) — Creates an alert view with the specified frame. _(deprecated)_
- [- initWithCoder:](<uialertview/init(coder_).md>) — Creates an alert view from data in an unarchiver. _(deprecated)_

### Setting properties

- [delegate](uialertview/delegate.md) — The receiver’s delegate or `nil` if it doesn’t have a delegate. _(deprecated)_
- [alertViewStyle](uialertview/alertviewstyle.md) — The kind of alert displayed to the user. _(deprecated)_
- [title](uialertview/title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [message](uialertview/message.md) — Descriptive text that provides more details than the title. _(deprecated)_
- [visible](uialertview/isvisible.md) — A Boolean value that indicates whether the receiver is displayed. _(deprecated)_

### Configuring buttons

- [- addButtonWithTitle:](<uialertview/addbutton(withtitle_).md>) — Adds a button to the receiver with the given title. _(deprecated)_
- [numberOfButtons](uialertview/numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- buttonTitleAtIndex:](<uialertview/buttontitle(at_).md>) — Returns the title of the button at the given index. _(deprecated)_
- [- textFieldAtIndex:](<uialertview/textfield(at_).md>) — Returns the text field at the given index _(deprecated)_
- [cancelButtonIndex](uialertview/cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [firstOtherButtonIndex](uialertview/firstotherbuttonindex.md) — The index of the first other button. _(deprecated)_

### Displaying

- [- show](<uialertview/show().md>) — Displays the receiver using animation. _(deprecated)_

### Dismissing

- [- dismissWithClickedButtonIndex:animated:](<uialertview/dismiss(withclickedbuttonindex_animated_).md>) — Dismisses the receiver, optionally with animation. _(deprecated)_

### Constants

- [UIAlertViewStyle](uialertviewstyle.md) — The presentation style of the alert.

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
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
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
