---
title: UIDocumentInteractionControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate.json'
content_hash: 'sha256:d576056944117ee4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentInteractionControllerDelegate

<sub>Protocol</sub>

A set of methods you can implement to respond to messages from a document interaction controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIDocumentInteractionControllerDelegate : NSObjectProtocol
```

## Overview

Use this protocol to participate when document previews are displayed and when a document is about to be opened by another application. You can also use this protocol to respond to commands (such as “copy” and “print”) from a document interaction controller’s options menu.

If you use a document interaction controller to display a document preview, your delegate must implement the [- documentInteractionControllerViewControllerForPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(__).md>) method. All other methods of this protocol are optional.

For more information about using a document interaction controller, see [UIDocumentInteractionController](uidocumentinteractioncontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the parent view controller

- [- documentInteractionControllerViewControllerForPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(__).md>) — Called when a document interaction controller needs a view controller for presenting a document preview.
- [- documentInteractionControllerViewForPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(__).md>) — Called when a document interaction controller needs the starting point for animating the display of a document preview.
- [- documentInteractionControllerRectForPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(__).md>) — Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerDidEndPreview:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerWillPresentOptionsMenu:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerDidDismissOptionsMenu:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.

### Opening files

- [- documentInteractionController:willBeginSendingToApplication:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(__willbeginsendingtoapplication_).md>) — Called when a document interaction controller’s document is about to be opened by the specified application.
- [- documentInteractionController:didEndSendingToApplication:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(__didendsendingtoapplication_).md>) — Called when a document interaction controller’s document has been handed off to the specified application.

### Deprecated

- [- documentInteractionController:canPerformAction:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(__canperformaction_).md>) — Called when a document interaction controller needs to know whether the specified action can be performed on the associated document. _(deprecated)_
- [- documentInteractionController:performAction:](<uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(__performaction_).md>) — Called when a document interaction controller wants its delegate to perform a specified action with the associated document. _(deprecated)_

## See Also

### Handling document-related interactions

- [delegate](uidocumentinteractioncontroller/delegate.md) — The delegate you want to receive document interaction notifications.
