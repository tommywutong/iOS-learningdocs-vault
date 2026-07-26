---
title: 'documentInteractionControllerViewForPreview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview%28_%3A%29.json'
content_hash: 'sha256:a2351d75c2174b3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerViewForPreview(_:)

<sub>Instance Method</sub>

Called when a document interaction controller needs the starting point for animating the display of a document preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerViewForPreview(_ controller: UIDocumentInteractionController) -> UIView?
```

## Parameters

- `controller` — The document interaction controller requesting the starting view.

## Return Value

The view to use as the starting point for the animation or `nil` if you want the document preview to fade into place.

## Discussion

By default, the starting rectangle for the animation is set to the bounds of the returned view. To specify a different starting rectangle, you must also override the [- documentInteractionControllerRectForPreview:](<documentinteractioncontrollerrectforpreview(__).md>) method.

## See Also

### Configuring the parent view controller

- [- documentInteractionControllerViewControllerForPreview:](<documentinteractioncontrollerviewcontrollerforpreview(__).md>) — Called when a document interaction controller needs a view controller for presenting a document preview.
- [- documentInteractionControllerRectForPreview:](<documentinteractioncontrollerrectforpreview(__).md>) — Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.
