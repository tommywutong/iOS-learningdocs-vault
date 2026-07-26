---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/delegate.json'
content_hash: 'sha256:46cbaf2fcfb02a38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate you want to receive document interaction notifications.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIDocumentInteractionControllerDelegate)? { get set }
```

## Discussion

You can implement a delegate object to track user interactions with menu items displayed by the document interaction controller. For more information, see [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md).

The default value of this property is `nil`.

## See Also

### Handling document-related interactions

- [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md) — A set of methods you can implement to respond to messages from a document interaction controller.
