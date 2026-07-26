---
title: UIActionSheet
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet.json'
content_hash: 'sha256:2e477ecb61c84a77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActionSheet

<sub>Class</sub>

A view that presents a set of alternatives for how to proceed with a task.

> [!warning] Deprecated
> Instead, use [UIAlertController](uialertcontroller.md) with a [preferredStyle](uialertcontroller/preferredstyle.md) of [UIAlertControllerStyleActionSheet](uialertcontroller/style/actionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIActionSheet
```

## Overview

In apps that target versions of iOS prior to iOS 8, use the [UIActionSheet](uiactionsheet.md) class to present the user with a set of alternatives for how to proceed with a given task. You can also use action sheets to prompt the user to confirm a potentially dangerous action. The action sheet contains an optional title and one or more buttons, each of which corresponds to an action to take.

Use the properties and methods of this class to configure the action sheet’s message, style, and buttons before presenting it. You should also assign a delegate to your action sheet. Your delegate object is responsible for performing the action associated with any buttons when they’re tapped and should conform to the [UIActionSheetDelegate](uiactionsheetdelegate.md) protocol. For more information about implementing the methods of the delegate, see [UIActionSheetDelegate](uiactionsheetdelegate.md).

You can present an action sheet from a toolbar, tab bar, button bar item, or from a view. This class takes the starting view and current platform into account when determining how to present the action sheet. For applications running on iPhone and iPod touch devices, the action sheet typically slides up from the bottom of the window that owns the view. For applications running on iPad devices, the action sheet is typically displayed in a popover that’s anchored to the starting view in an appropriate way. Taps outside of the popover automatically dismiss the action sheet, as do taps within any custom buttons. You can also dismiss it programmatically.

When presenting an action sheet on an iPad, there are times when you shouldn’t include a cancel button. If you’re presenting just the action sheet, the system displays the action sheet inside a popover without using an animation. Because taps outside the popover dismiss the action sheet without selecting an item, this results in a default way to cancel the sheet. Including a cancel button would therefore only cause confusion. However, if you have an existing popover and are displaying an action sheet on top of other content using an animation, a cancel button is still appropriate. For more information, see [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

> [!important] Important
> In iOS 4 and later, action sheets aren’t dismissed automatically when an application moves to the background. This behavior differs from earlier versions of the operating system, where action sheets were automatically canceled (and their cancellation handler executed) as part of the termination sequence for the application. Now, it’s up to you to decide whether to dismiss the action sheet (and execute its cancellation handler) or leave it visible for when your application moves back to the foreground. Remember that your application can still be terminated while in the background, so some type of action may be necessary in either case.

### Subclassing notes

[UIActionSheet](uiactionsheet.md) isn’t designed to be subclassed, nor should you add views to its hierarchy. If you need to present a sheet with more customization than provided by the [UIActionSheet](uiactionsheet.md) API, you can create your own and present it modally with [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>).

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating action sheets

- [init(title:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:_:)](<uiactionsheet/init(title_delegate_cancelbuttontitle_destructivebuttontitle_otherbuttontitles___).md>) — Creates an action sheet with the specified values. _(deprecated)_
- [- initWithTitle:delegate:cancelButtonTitle:destructiveButtonTitle:otherButtonTitles:](<uiactionsheet/init(title_delegate_cancelbuttontitle_destructivebuttontitle_).md>) — Initializes the action sheet using the specified starting parameters. _(deprecated)_

### Setting properties

- [delegate](uiactionsheet/delegate.md) — The receiver’s delegate or `nil` if it doesn’t have a delegate. _(deprecated)_
- [title](uiactionsheet/title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [visible](uiactionsheet/isvisible.md) — A Boolean value that indicates whether the receiver is displayed. _(deprecated)_
- [actionSheetStyle](uiactionsheet/actionsheetstyle.md) — The receiver’s presentation style. _(deprecated)_

### Configuring buttons

- [- addButtonWithTitle:](<uiactionsheet/addbutton(withtitle_).md>) — Adds a custom button to the action sheet. _(deprecated)_
- [numberOfButtons](uiactionsheet/numberofbuttons.md) — The number of buttons on the action sheet. _(deprecated)_
- [- buttonTitleAtIndex:](<uiactionsheet/buttontitle(at_).md>) — Returns the title of the button at the specified index. _(deprecated)_
- [cancelButtonIndex](uiactionsheet/cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [destructiveButtonIndex](uiactionsheet/destructivebuttonindex.md) — The index number of the destructive button. _(deprecated)_
- [firstOtherButtonIndex](uiactionsheet/firstotherbuttonindex.md) — The index of the first custom button. _(deprecated)_

### Presenting the action sheet

- [- showFromTabBar:](<uiactionsheet/show(from_)-9i3tw.md>) — Displays an action sheet that originates from the specified tab bar. _(deprecated)_
- [- showFromToolbar:](<uiactionsheet/show(from_)-1p4ap.md>) — Displays an action sheet that originates from the specified toolbar. _(deprecated)_
- [- showInView:](<uiactionsheet/show(in_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_
- [- showFromBarButtonItem:animated:](<uiactionsheet/show(from_animated_).md>) — Displays an action sheet that originates from the specified bar button item. _(deprecated)_
- [- showFromRect:inView:animated:](<uiactionsheet/show(from_in_animated_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_

### Dismissing the action sheet

- [- dismissWithClickedButtonIndex:animated:](<uiactionsheet/dismiss(withclickedbuttonindex_animated_).md>) — Dismisses the action sheet immediately using an optional animation. _(deprecated)_

### Constants

- [UIActionSheetStyle](uiactionsheetstyle.md) — Specifies the style of an action sheet. _(deprecated)_

## See Also

### Deprecated classes

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
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
