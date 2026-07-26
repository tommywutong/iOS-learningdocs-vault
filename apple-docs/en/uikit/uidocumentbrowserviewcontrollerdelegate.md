---
title: UIDocumentBrowserViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate.json'
content_hash: 'sha256:4d0f06a3913bae9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentBrowserViewControllerDelegate

<sub>Protocol</sub>

The protocol you implement to respond as the user interacts with the document browser.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIDocumentBrowserViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating new documents

- [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) — Asks the delegate to create a new document.
- [ImportMode](uidocumentbrowserviewcontroller/importmode.md) — The document browser’s import modes.
- [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) — Tells the delegate that a document has been successfully imported.
- [- documentBrowser:failedToImportDocumentAtURL:error:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__failedtoimportdocumentat_error_).md>) — Tells the delegate that the document browser failed to import the specified document.

### Selecting documents

- [- documentBrowser:didPickDocumentsAtURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumentsat_).md>) — Tells the delegate that the user has selected one or more documents.

### Working with the browser’s activity view

- [- documentBrowser:willPresentActivityViewController:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__willpresent_).md>) — Tells the delegate that the document browser will display an activity view.
- [- documentBrowser:applicationActivitiesForDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__applicationactivitiesfordocumenturls_).md>) — Asks the delegate for additional activities when displaying an activity view.

### Deprecated methods

- [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) — Tells the delegate that the user has selected one or more documents. _(deprecated)_

## See Also

### Related Documentation

- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — A view controller for browsing and performing actions on documents that you store locally and in the cloud.

### Responding to browser events

- [delegate](uidocumentbrowserviewcontroller/delegate.md) — The document browser’s delegate.
- [- importDocumentAtURL:nextToDocumentAtURL:mode:completionHandler:](<uidocumentbrowserviewcontroller/importdocument(at_nexttodocumentat_mode_completionhandler_).md>) — Imports a document into the same location as an existing document.
