---
title: 'documentBrowser(_:didImportDocumentAt:toDestinationURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Adidimportdocumentat%3Atodestinationurl%3A%29.json'
content_hash: 'sha256:290936df83873a8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:didImportDocumentAt:toDestinationURL:)

<sub>Instance Method</sub>

Tells the delegate that a document has been successfully imported.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didImportDocumentAt sourceURL: URL, toDestinationURL destinationURL: URL)
```

## Parameters

- `controller` — The document browser that performed the import action.

- `sourceURL` — The document’s original URL.

- `destinationURL` — The document’s URL after the import.

## Discussion

To open the document as soon as it’s imported:

1. Open a new [UIDocument](../uidocument.md) subclass for the document (or use a file presenter and file coordination to access the document).
2. Create a view controller to display the document.
3. Present that view controller modally.

## See Also

### Creating new documents

- [- documentBrowser:didRequestDocumentCreationWithHandler:](<documentbrowser(__didrequestdocumentcreationwithhandler_).md>) — Asks the delegate to create a new document.
- [ImportMode](../uidocumentbrowserviewcontroller/importmode.md) — The document browser’s import modes.
- [- documentBrowser:failedToImportDocumentAtURL:error:](<documentbrowser(__failedtoimportdocumentat_error_).md>) — Tells the delegate that the document browser failed to import the specified document.
