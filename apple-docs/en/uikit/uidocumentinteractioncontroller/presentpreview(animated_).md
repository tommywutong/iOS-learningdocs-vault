---
title: 'presentPreview(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/presentpreview(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentpreview(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/presentpreview%28animated%3A%29.json'
content_hash: 'sha256:6ddcdea29ccd58f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# presentPreview(animated:)

<sub>Instance Method</sub>

Displays a full-screen preview of the target document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentPreview(animated: Bool) -> Bool
```

## Parameters

- `animated` — Specify [true](../../swift/true.md) to animate the appearance of the document preview or [false](../../swift/false.md) to display it immediately.

## Return Value

[true](../../swift/true.md) if this method was able to display the document preview or [false](../../swift/false.md) if it was not.

## Discussion

To use this method, you must first provide a delegate object that implements the [- documentInteractionControllerViewControllerForPreview:](<../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(__).md>) method. The view controller returned by that method is used to present the document preview modally.

If your delegate implements the [- documentInteractionControllerViewForPreview:](<../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(__).md>) and [- documentInteractionControllerRectForPreview:](<../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(__).md>) methods, the view and rectangle returned by those methods is used as the starting point for the animation used to display the document preview. If the animated parameter is [true](../../swift/true.md) but your delegate does not implement the [- documentInteractionControllerViewForPreview:](<../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(__).md>) method (or that method returns `nil`), the document preview is animated into place using a crossfade transition.

This method displays the document preview asynchronously. The document interaction controller dismisses the document preview automatically in response to appropriate user interactions. You can also dismiss the preview programmatically using the [- dismissPreviewAnimated:](<dismisspreview(animated_).md>) method.

## See Also

### Presenting and dismissing a document preview

- [- dismissPreviewAnimated:](<dismisspreview(animated_).md>) — Dismisses the currently active document preview.
