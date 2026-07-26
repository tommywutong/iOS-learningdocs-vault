---
title: UIPopoverControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontrollerdelegate.json'
content_hash: 'sha256:a86faa8e5690bcb9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPopoverControllerDelegate

<sub>Protocol</sub>

The interface for the delegate of a popover controller object.

> [!warning] Deprecated
> In iOS 9 and later, a popover is implemented as a [UIViewController](uiviewcontroller.md) presentation. To create a popover, use [UIPopoverPresentationController](uipopoverpresentationcontroller.md) and specify the [UIModalPresentationPopover](uimodalpresentationstyle/popover.md) style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIPopoverControllerDelegate : NSObjectProtocol
```

## Overview

Popover controllers notify their delegate whenever user interactions would cause the dismissal of the popover and, in some cases, give the user a chance to prevent that dismissal.

For more information about the [UIPopoverController](uipopovercontroller.md) class, see [UIPopoverController](uipopovercontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to popover position changes

- [- popoverController:willRepositionPopoverToRect:inView:](<uipopovercontrollerdelegate/popovercontroller(__willrepositionpopoverto_in_).md>) — Tells the delegate that the popover controller needs to change the popover’s location in its view. _(deprecated)_

### Managing the popover’s dismissal

- [- popoverControllerShouldDismissPopover:](<uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(__).md>) — Asks the delegate if the popover should be dismissed. _(deprecated)_
- [- popoverControllerDidDismissPopover:](<uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(__).md>) — Tells the delegate that the popover was dismissed. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
