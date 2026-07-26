---
title: 'documentInteractionControllerRectForPreview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview%28_%3A%29.json'
content_hash: 'sha256:d3b056459fa0bf97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerRectForPreview(_:)

<sub>Instance Method</sub>

Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerRectForPreview(_ controller: UIDocumentInteractionController) -> CGRect
```

## Parameters

- `controller` — The document interaction controller requesting the starting rectangle.

## Return Value

A rectangle in the coordinate system of the view returned by the [- documentInteractionControllerViewForPreview:](<documentinteractioncontrollerviewforpreview(__).md>) method.

## Discussion

If you do not implement the [- documentInteractionControllerViewForPreview:](<documentinteractioncontrollerviewforpreview(__).md>) method, or if you do implement it but return a `nil` value, this method is not called. If you do not implement this method, the starting rectangle is assumed to be the bounds of the view returned by the [- documentInteractionControllerViewForPreview:](<documentinteractioncontrollerviewforpreview(__).md>) method.

## See Also

### Configuring the parent view controller

- [- documentInteractionControllerViewControllerForPreview:](<documentinteractioncontrollerviewcontrollerforpreview(__).md>) — Called when a document interaction controller needs a view controller for presenting a document preview.
- [- documentInteractionControllerViewForPreview:](<documentinteractioncontrollerviewforpreview(__).md>) — Called when a document interaction controller needs the starting point for animating the display of a document preview.
