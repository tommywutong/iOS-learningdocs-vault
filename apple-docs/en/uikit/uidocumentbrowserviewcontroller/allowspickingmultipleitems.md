---
title: allowsPickingMultipleItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/allowspickingmultipleitems
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowspickingmultipleitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/allowspickingmultipleitems.json'
content_hash: 'sha256:dd553ea0f4e84a3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# allowsPickingMultipleItems

<sub>Instance Property</sub>

A Boolean value that determines whether the user can select and open more than one document at a time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsPickingMultipleItems: Bool { get set }
```

## Discussion

By default, this property is set to [false](../../swift/false.md).

## See Also

### Configuring a document browser

- [allowsDocumentCreation](allowsdocumentcreation.md) — A Boolean value that determines whether the document browser can create new documents.
- [- revealDocumentAtURL:importIfNeeded:completion:](<revealdocument(at_importifneeded_completion_).md>) — Reveals, and optionally imports, the document at the provided URL.
- [contentTypesForRecentDocuments](contenttypesforrecentdocuments.md) — Content types for browsing recent documents.
