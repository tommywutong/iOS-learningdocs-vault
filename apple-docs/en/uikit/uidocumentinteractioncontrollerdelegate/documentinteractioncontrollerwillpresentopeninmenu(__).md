---
title: 'documentInteractionControllerWillPresentOpenInMenu(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu%28_%3A%29.json'
content_hash: 'sha256:edf83b5f13b27e8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerWillPresentOpenInMenu(_:)

<sub>Instance Method</sub>

Called when a document interaction controller is about to display an Open In menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerWillPresentOpenInMenu(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that is about to display a menu.

## Discussion

The Open In menu is used to select an application for opening the current file. You can use this method to update your user interface in response to displaying the menu.

## See Also

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerDidEndPreview:](<documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerDidDismissOptionsMenu:](<documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.
