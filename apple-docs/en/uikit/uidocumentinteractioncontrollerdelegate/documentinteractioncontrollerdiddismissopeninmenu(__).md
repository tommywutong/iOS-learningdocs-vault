---
title: 'documentInteractionControllerDidDismissOpenInMenu(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu%28_%3A%29.json'
content_hash: 'sha256:0c1563ad2e4d91c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerDidDismissOpenInMenu(_:)

<sub>Instance Method</sub>

Called when a document interaction controller has dismissed its Open In menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerDidDismissOpenInMenu(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that dismissed its menu.

## Discussion

You can use this method to remove any additional views or content you placed underneath the Open In menu in your [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) method.

## See Also

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerDidEndPreview:](<documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerDidDismissOptionsMenu:](<documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
