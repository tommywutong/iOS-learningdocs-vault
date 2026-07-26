---
title: allowsDocumentCreation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/allowsdocumentcreation
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowsdocumentcreation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/allowsdocumentcreation.json'
content_hash: 'sha256:85b0b609ed31f970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# allowsDocumentCreation

<sub>Instance Property</sub>

A Boolean value that determines whether the document browser can create new documents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsDocumentCreation: Bool { get set }
```

## Discussion

The browser creates new documents when the user taps the Add (+) button in the navigation bar. The Add button is enabled only if both the [allowsDocumentCreation](allowsdocumentcreation.md) property is set to [true](../../swift/true.md), and the browser delegate implements the [- documentBrowser:didRequestDocumentCreationWithHandler:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method.

By default, this property is set to [true](../../swift/true.md).

## See Also

### Configuring a document browser

- [allowsPickingMultipleItems](allowspickingmultipleitems.md) — A Boolean value that determines whether the user can select and open more than one document at a time.
- [- revealDocumentAtURL:importIfNeeded:completion:](<revealdocument(at_importifneeded_completion_).md>) — Reveals, and optionally imports, the document at the provided URL.
- [contentTypesForRecentDocuments](contenttypesforrecentdocuments.md) — Content types for browsing recent documents.
