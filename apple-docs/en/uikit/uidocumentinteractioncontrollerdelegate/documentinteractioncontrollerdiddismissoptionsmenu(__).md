---
title: 'documentInteractionControllerDidDismissOptionsMenu(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu%28_%3A%29.json'
content_hash: 'sha256:16e93d65aea7be79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerDidDismissOptionsMenu(_:)

<sub>Instance Method</sub>

Called when a document interaction controller has dismissed its options menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerDidDismissOptionsMenu(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that dismissed its options menu.

## Discussion

You can use this method to remove any additional views or content you placed underneath the options menu in your [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) method.

## See Also

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerDidEndPreview:](<documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.
