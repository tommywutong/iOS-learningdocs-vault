---
title: UIAlertViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate.json'
content_hash: 'sha256:ddc7bdef43012ba8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAlertViewDelegate

<sub>Protocol</sub>

The interface for the delegate of an alert view object.

> [!warning] Deprecated
> Use [UIAlertController](uialertcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UIAlertViewDelegate : NSObjectProtocol
```

## Overview

The delegate implements the button actions and any other custom behavior. Some of the methods defined in this protocol are optional.

If you add your own buttons or customize the behavior of an alert view, implement a delegate conforming to this protocol to handle the corresponding delegate messages. Use the [delegate](uialertview/delegate.md) property of an alert view to specify one of your application objects as the delegate.

If you add your own buttons to an alert view, the delegate must implement the [- alertView:clickedButtonAtIndex:](<uialertviewdelegate/alertview(__clickedbuttonat_).md>) message to respond when those buttons are clicked; otherwise, your custom buttons do nothing. The alert view is automatically dismissed after the [- alertView:clickedButtonAtIndex:](<uialertviewdelegate/alertview(__clickedbuttonat_).md>) delegate method is invoked.

Optionally, you can implement the [- alertViewCancel:](<uialertviewdelegate/alertviewcancel(__).md>) method to take the appropriate action when the system cancels your alert view. If the delegate doesn’t implement this method, the default behavior is to simulate the user clicking the cancel button and closing the view.

You can also optionally augment the behavior of presenting and dismissing alert views using the methods in Customizing behavior.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to actions

- [- alertView:clickedButtonAtIndex:](<uialertviewdelegate/alertview(__clickedbuttonat_).md>) — Sent to the delegate when the user clicks a button on an alert view. _(deprecated)_

### Customizing behavior

- [- alertViewShouldEnableFirstOtherButton:](<uialertviewdelegate/alertviewshouldenablefirstotherbutton(__).md>) — Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled. _(deprecated)_
- [- willPresentAlertView:](<uialertviewdelegate/willpresent(__).md>) — Sent to the delegate before a model view is presented to the user. _(deprecated)_
- [- didPresentAlertView:](<uialertviewdelegate/didpresent(__).md>) — Sent to the delegate after an alert view is presented to the user. _(deprecated)_
- [- alertView:willDismissWithButtonIndex:](<uialertviewdelegate/alertview(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an alert view is dismissed. _(deprecated)_
- [- alertView:didDismissWithButtonIndex:](<uialertviewdelegate/alertview(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an alert view is dismissed from the screen. _(deprecated)_

### Canceling

- [- alertViewCancel:](<uialertviewdelegate/alertviewcancel(__).md>) — Sent to the delegate before an alert view is canceled. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
