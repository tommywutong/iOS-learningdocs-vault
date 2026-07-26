---
title: 'transitionController(forDocumentURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（12.0 起废弃）, iPadOS 11.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller%28fordocumenturl%3A%29.json'
content_hash: 'sha256:a91b74efdda2970b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# transitionController(forDocumentURL:)

<sub>Instance Method</sub>

Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

> [!warning] Deprecated
> Use [- transitionControllerForDocumentAtURL:](<transitioncontroller(fordocumentat_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func transitionController(forDocumentURL documentURL: URL) -> UIDocumentBrowserTransitionController
```

## Parameters

- `documentURL` — The URL of a document. Only use URLs provided by the document browser (for example, URLs passed to the delegate’s [- documentBrowser:didRequestDocumentCreationWithHandler:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>)method’s completion block).

## Return Value

Returns a newly instantiated transition controller. Its [loadingProgress](../uidocumentbrowsertransitioncontroller/loadingprogress.md) and [targetView](../uidocumentbrowsertransitioncontroller/targetview.md) properties are both set to `nil`.

## Discussion

For the animations to function properly, you must maintain a strong reference to the transition controller until all the animation sequences are complete.

For more about using the transition controller, see [UIDocumentBrowserTransitionController](../uidocumentbrowsertransitioncontroller.md).

## See Also

### Deprecated symbols

- [- initForOpeningFilesWithContentTypes:](<init(foropeningfileswithcontenttypes_).md>) — Initializes and returns a document browser view controller that can open the specified file types. _(deprecated)_
- [recentDocumentsContentTypes](recentdocumentscontenttypes.md) — Content types for browsing recent documents. _(deprecated)_
- [allowedContentTypes](allowedcontenttypes.md) — The document types that the browser can open. _(deprecated)_
