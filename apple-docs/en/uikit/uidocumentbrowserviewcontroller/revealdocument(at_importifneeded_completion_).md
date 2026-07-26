---
title: 'revealDocument(at:importIfNeeded:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/revealdocument%28at%3Aimportifneeded%3Acompletion%3A%29.json'
content_hash: 'sha256:caea159ed61e7b1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# revealDocument(at:importIfNeeded:completion:)

<sub>Instance Method</sub>

Reveals, and optionally imports, the document at the provided URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func revealDocument(at url: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func revealDocument(at url: URL, importIfNeeded: Bool) async throws -> URL
```

## Parameters

- `url` — The URL of the document to reveal.

- `importIfNeeded` — A Boolean value that determines whether the document browser should import the document.

- `completion` — A completion block with the following parameters: - **url** — The new URL of an imported document. Set to `nil` if `shouldImport` is [false](../../swift/false.md), or if an error occurs. - **error** — If an error occurs, this parameter contains the error information; otherwise, set to `nil`.

## Discussion

Call this method to display a document in the document browser.

If `importIfNeeded` is [true](../../swift/true.md), the document browser calls its delegate’s [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) method (or its [- documentBrowser:failedToImportDocumentAtURL:error:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__failedtoimportdocumentat_error_).md>) method, if an error occurred) before calling the completion handler.

## See Also

### Configuring a document browser

- [allowsDocumentCreation](allowsdocumentcreation.md) — A Boolean value that determines whether the document browser can create new documents.
- [allowsPickingMultipleItems](allowspickingmultipleitems.md) — A Boolean value that determines whether the user can select and open more than one document at a time.
- [contentTypesForRecentDocuments](contenttypesforrecentdocuments.md) — Content types for browsing recent documents.
