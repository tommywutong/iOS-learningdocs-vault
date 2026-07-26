---
title: 'documentInteractionControllerViewControllerForPreview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview%28_%3A%29.json'
content_hash: 'sha256:7ccf7e3792c3b73a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerViewControllerForPreview(_:)

<sub>Instance Method</sub>

Called when a document interaction controller needs a view controller for presenting a document preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor optional func documentInteractionControllerViewControllerForPreview(_ controller: UIDocumentInteractionController) -> UIViewController
```

## Parameters

- `controller` — The document interaction controller requesting the parent view controller.

## Return Value

The view controller to use when presenting the document preview. The return value must not be `nil`.

## Discussion

Although technically optional, this method is required if your application attempts to display a preview for a document. The view controller returned by this method is used as the parent for the document preview.

If you return a navigation controller from this method, the document interaction controller is pushed onto the navigation stack using the standard navigation controller animations. If you return any other type of view controller, the document interaction controller is displayed modally, in which case, the view controller you return must be capable of presenting a modal view controller.

## See Also

### Configuring the parent view controller

- [- documentInteractionControllerViewForPreview:](<documentinteractioncontrollerviewforpreview(__).md>) — Called when a document interaction controller needs the starting point for animating the display of a document preview.
- [- documentInteractionControllerRectForPreview:](<documentinteractioncontrollerrectforpreview(__).md>) — Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.
