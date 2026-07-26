---
title: 'documentInteractionControllerDidEndPreview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview%28_%3A%29.json'
content_hash: 'sha256:1af33f0c2cad0a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerDidEndPreview(_:)

<sub>Instance Method</sub>

Called when a document interaction controller has dismissed its document preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerDidEndPreview(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that dismissed its document preview.

## Discussion

This method is called after the view containing the document preview has been removed from the application’s key window. You can use this notification to remove any interface elements you set up behind the preview elements.

## See Also

### Presenting the user interface

- [- documentInteractionControllerWillBeginPreview:](<documentinteractioncontrollerwillbeginpreview(__).md>) — Called when a document interaction controller is about to display a preview for its document.
- [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerDidDismissOptionsMenu:](<documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.
