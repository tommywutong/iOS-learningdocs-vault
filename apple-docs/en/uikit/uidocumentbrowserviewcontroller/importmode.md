---
title: UIDocumentBrowserViewController.ImportMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/importmode
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/importmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/importmode.json'
content_hash: 'sha256:d37fcee23873143e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# UIDocumentBrowserViewController.ImportMode

<sub>Enumeration</sub>

The document browser’s import modes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ImportMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDocumentBrowserImportModeCopy](importmode/copy.md) — A mode indicating that the file should be copied into its new location (the original file is left unchanged).
- [UIDocumentBrowserImportModeMove](importmode/move.md) — A mode indicating that the file should be moved to its new location (the original file should be deleted).
- [UIDocumentBrowserImportModeNone](importmode/none.md) — A mode indicating that the document can’t be imported.

### Initializers

- [init(rawValue:)](<importmode/init(rawvalue_).md>)

## See Also

### Creating new documents

- [- documentBrowser:didRequestDocumentCreationWithHandler:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) — Asks the delegate to create a new document.
- [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didimportdocumentat_todestinationurl_).md>) — Tells the delegate that a document has been successfully imported.
- [- documentBrowser:failedToImportDocumentAtURL:error:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__failedtoimportdocumentat_error_).md>) — Tells the delegate that the document browser failed to import the specified document.
