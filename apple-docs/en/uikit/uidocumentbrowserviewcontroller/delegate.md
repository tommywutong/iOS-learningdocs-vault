---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/delegate.json'
content_hash: 'sha256:14c152f6b4d6764e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The document browser’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIDocumentBrowserViewControllerDelegate)? { get set }
```

## Discussion

The delegate object must implement the [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md) protocol.

## See Also

### Responding to browser events

- [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md) — The protocol you implement to respond as the user interacts with the document browser.
- [- importDocumentAtURL:nextToDocumentAtURL:mode:completionHandler:](<importdocument(at_nexttodocumentat_mode_completionhandler_).md>) — Imports a document into the same location as an existing document.
