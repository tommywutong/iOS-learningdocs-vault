---
title: UIViewControllerPreviewing
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewing
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewing.json'
content_hash: 'sha256:ed761dcf7027eae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerPreviewing

<sub>Protocol</sub>

A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.

> [!warning] Deprecated
> Use [UIContextMenuInteraction](uicontextmenuinteraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerPreviewing : NSObjectProtocol
```

## Overview

The system returns a context object conforming to this protocol when you call a view controller’s [- registerForPreviewingWithDelegate:sourceView:](<uiviewcontroller/registerforpreviewing(with_sourceview_).md>) method. This method registers the view controller to participate in 3D Touch preview (peek) and commit (pop) behaviors.

> [!note] Terminology Note
> The end-user terminology for the views presented during the phases of force-based touches includes _peek_ and _pop_. For clarity here, and to align with the API names, this document uses the corresponding terms _preview_ and _commit view_.

To learn about 3D Touch, read [Adopting 3D Touch on iPhone](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/index.html#//apple_ref/doc/uid/TP40016543).

> [!important] Important
> Don’t adopt this protocol in custom classes.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a source view for a 3D Touch previewing view controller

- [sourceRect](uiviewcontrollerpreviewing/sourcerect.md) — The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs. _(deprecated)_
- [previewingGestureRecognizerForFailureRelationship](uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship.md) — A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures. _(deprecated)_

### Accessing properties of a 3D Touch previewing view controller

- [delegate](uiviewcontrollerpreviewing/delegate.md) — The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers. _(deprecated)_
- [sourceView](uiviewcontrollerpreviewing/sourceview.md) — A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UISearchDisplayDelegate](uisearchdisplaydelegate.md) — The interface for the delegate of a search display controller. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
