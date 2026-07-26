---
title: UIActionSheetDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheetdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheetdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheetdelegate.json'
content_hash: 'sha256:7ef28fd5454868b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActionSheetDelegate

<sub>Protocol</sub>

The interface for the delegate of an action sheet object.

> [!warning] Deprecated
> Use [UIAlertController](uialertcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIActionSheetDelegate : NSObjectProtocol
```

## Overview

The delegate implements the button actions and any other custom behavior. Some of the methods defined in this protocol are optional.

If you add your own buttons or customize the behavior of an action sheet, implement a delegate conforming to this protocol to handle the corresponding delegate messages. Use the [delegate](uiactionsheet/delegate.md) property of the action sheet object to specify one of your application objects as the delegate.

If you add your own buttons to an action sheet, the delegate must implement the [- actionSheet:clickedButtonAtIndex:](<uiactionsheetdelegate/actionsheet(__clickedbuttonat_).md>) message to respond when those buttons are clicked; otherwise, your custom buttons do nothing. The action sheet is automatically dismissed after the [- actionSheet:clickedButtonAtIndex:](<uiactionsheetdelegate/actionsheet(__clickedbuttonat_).md>) delegate method is invoked.

Optionally, you can implement the [- actionSheetCancel:](<uiactionsheetdelegate/actionsheetcancel(__).md>) method to take the appropriate action when the system cancels your action sheet. If the delegate does not implement this method, the default behavior is to simulate the user clicking the cancel button and closing the view.

You can also optionally augment the behavior of presenting and dismissing action sheets using the methods in Customizing behavior.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIDocumentInteractionController](uidocumentinteractioncontroller.md)

## Topics

### Responding to actions

- [- actionSheet:clickedButtonAtIndex:](<uiactionsheetdelegate/actionsheet(__clickedbuttonat_).md>) — Sent to the delegate when the user clicks a button on an action sheet. _(deprecated)_

### Customizing behavior

- [- willPresentActionSheet:](<uiactionsheetdelegate/willpresent(__).md>) — Sent to the delegate before an action sheet is presented to the user. _(deprecated)_
- [- didPresentActionSheet:](<uiactionsheetdelegate/didpresent(__).md>) — Sent to the delegate after an action sheet is presented to the user. _(deprecated)_
- [- actionSheet:willDismissWithButtonIndex:](<uiactionsheetdelegate/actionsheet(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an action sheet is dismissed. _(deprecated)_
- [- actionSheet:didDismissWithButtonIndex:](<uiactionsheetdelegate/actionsheet(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an action sheet is dismissed from the screen. _(deprecated)_

### Canceling

- [- actionSheetCancel:](<uiactionsheetdelegate/actionsheetcancel(__).md>) — Sent to the delegate before an action sheet is canceled. _(deprecated)_

## See Also

### Deprecated protocols

- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
