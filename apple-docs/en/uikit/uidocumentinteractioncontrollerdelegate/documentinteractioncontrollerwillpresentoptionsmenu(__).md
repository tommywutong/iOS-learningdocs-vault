---
title: 'documentInteractionControllerWillPresentOptionsMenu(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu%28_%3A%29.json'
content_hash: 'sha256:f8e07632d87afbac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerWillPresentOptionsMenu(_:)

<sub>Instance Method</sub>

Called when a document interaction controller is about to display an options menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerWillPresentOptionsMenu(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that is about to display an options menu.

## Discussion

The options menu is used to present the user with options for previewing the document, opening it in an application, or copying its contents. You can use this method to update your user interface in response to displaying the menu.

## See Also

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerDidEndPreview:](<documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerDidDismissOptionsMenu:](<documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.
