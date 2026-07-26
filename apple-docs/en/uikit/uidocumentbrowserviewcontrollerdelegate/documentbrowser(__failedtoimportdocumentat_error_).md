---
title: 'documentBrowser(_:failedToImportDocumentAt:error:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Afailedtoimportdocumentat%3Aerror%3A%29.json'
content_hash: 'sha256:72043d6fdeb1e592'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:failedToImportDocumentAt:error:)

<sub>Instance Method</sub>

Tells the delegate that the document browser failed to import the specified document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, failedToImportDocumentAt documentURL: URL, error: (any Error)?)
```

## Parameters

- `controller` — The document browser that attempted the import action.

- `documentURL` — The document’s original URL.

- `error` — An object describing the error, or `nil`.

## See Also

### Creating new documents

- [- documentBrowser:didRequestDocumentCreationWithHandler:](<documentbrowser(__didrequestdocumentcreationwithhandler_).md>) — Asks the delegate to create a new document.
- [ImportMode](../uidocumentbrowserviewcontroller/importmode.md) — The document browser’s import modes.
- [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<documentbrowser(__didimportdocumentat_todestinationurl_).md>) — Tells the delegate that a document has been successfully imported.
