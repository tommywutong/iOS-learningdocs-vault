---
title: UIViewControllerPreviewingDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewingdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewingdelegate.json'
content_hash: 'sha256:cd69d834f84e4af5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerPreviewingDelegate

<sub>Protocol</sub>

A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.

> [!warning] Deprecated
> Use [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerPreviewingDelegate : NSObjectProtocol
```

## Overview

To learn about 3D Touch, read [Adopting 3D Touch on iPhone](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/index.html#//apple_ref/doc/uid/TP40016543).

> [!note] Terminology Note
> The end-user terminology for the views presented during the phases of force-based touches includes _peek_ and _pop_. For clarity here, and to align with the API names, this document uses the corresponding terms _preview_ and _commit view_.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing preview and commit views for 3D Touch

- [- previewingContext:viewControllerForLocation:](<uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>) — Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available. _(deprecated)_
- [- previewingContext:commitViewController:](<uiviewcontrollerpreviewingdelegate/previewingcontext(__commit_).md>) — Called to let you prepare the presentation of a commit (pop) view from your commit view controller. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
