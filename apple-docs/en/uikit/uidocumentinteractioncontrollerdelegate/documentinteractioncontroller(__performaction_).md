---
title: 'documentInteractionController(_:performAction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（6.0 起废弃）, iPadOS 3.2+（6.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller%28_%3Aperformaction%3A%29.json'
content_hash: 'sha256:d5c71f6a325da415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionController(_:performAction:)

<sub>Instance Method</sub>

Called when a document interaction controller wants its delegate to perform a specified action with the associated document.

> [!warning] Deprecated
> Apps should use [UIActivityViewController](../uiactivityviewcontroller.md) for actions.

<sub>visionOS</sub>

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, performAction action: Selector?) -> Bool
```

## Parameters

- `controller` — The document interaction controller managing an associated document.

- `action` — The selector representing the action to perform. You can invoke this selector directly on the object responsible for performing the action or use it to call the appropriate method.

## Return Value

[true](../../swift/true.md) if the action was performed successfully or [false](../../swift/false.md) if it was not.

## Discussion

The supported `action` selectors for this method are `copy:` and `print:`. (The `print:` selector is available in iOS 4.2 and later. Printing is supported only on devices that support multitasking.)

To implement a `copy:` action, write the contents of the document—directly, or modified according to the intent of your app—to the pasteboard.

To implement a `print:` action, use the shared print interaction controller object. Assign the [URL](../uidocumentinteractioncontroller/url.md) property of the document interaction controller to the print interaction controller’s [printingItem](../uiprintinteractioncontroller/printingitem.md) property. Then present the printing user interface. For details, refer to [UIPrintInteractionController](../uiprintinteractioncontroller.md) and to [Printing](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Printing/Printing.html#//apple_ref/doc/uid/TP40010156-CH12) in [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

Instead of implementing printing code in this method, you can rely on the built-in printing support of the Quick Look framework. For document types that can be previewed, the options menu of a document interaction controller always contains a Quick Look item. If the user chooses that item, the resulting Quick Look view includes an action button in the navigation bar that, when tapped, offers a Print button. In this case, the system automatically handles printing. For details, refer to [QLPreviewController](../../quicklook/qlpreviewcontroller.md) and to [Using the Quick Look Framework](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/UsingtheQuickLookFramework.html#//apple_ref/doc/uid/TP40010413) in [Document Interaction Programming Topics for iOS](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010403).

## See Also

### Deprecated

- [- documentInteractionController:canPerformAction:](<documentinteractioncontroller(__canperformaction_).md>) — Called when a document interaction controller needs to know whether the specified action can be performed on the associated document. _(deprecated)_
