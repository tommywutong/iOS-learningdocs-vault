---
title: 'documentInteractionControllerWillBeginPreview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview%28_%3A%29.json'
content_hash: 'sha256:0bcdadad3b582505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionControllerWillBeginPreview(_:)

<sub>Instance Method</sub>

Called when a document interaction controller is about to display a preview for its document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionControllerWillBeginPreview(_ controller: UIDocumentInteractionController)
```

## Parameters

- `controller` — The document interaction controller that is about to preview its document.

## Discussion

This method is called shortly before the view containing the document preview is presented modally. You can use this notification to set up any additional interface elements behind the preview elements.

## See Also

### Presenting the user interface

- [- documentInteractionControllerDidEndPreview:](<documentinteractioncontrollerdidendpreview(__).md>) — Called when a document interaction controller has dismissed its document preview.
- [- documentInteractionControllerWillPresentOptionsMenu:](<documentinteractioncontrollerwillpresentoptionsmenu(__).md>) — Called when a document interaction controller is about to display an options menu.
- [- documentInteractionControllerDidDismissOptionsMenu:](<documentinteractioncontrollerdiddismissoptionsmenu(__).md>) — Called when a document interaction controller has dismissed its options menu.
- [- documentInteractionControllerWillPresentOpenInMenu:](<documentinteractioncontrollerwillpresentopeninmenu(__).md>) — Called when a document interaction controller is about to display an Open In menu.
- [- documentInteractionControllerDidDismissOpenInMenu:](<documentinteractioncontrollerdiddismissopeninmenu(__).md>) — Called when a document interaction controller has dismissed its Open In menu.
