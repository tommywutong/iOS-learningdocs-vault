---
title: 'transitionController(forDocumentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller%28fordocumentat%3A%29.json'
content_hash: 'sha256:a6d78e63b6a75fd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# transitionController(forDocumentAt:)

<sub>Instance Method</sub>

Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func transitionController(forDocumentAt documentURL: URL) -> UIDocumentBrowserTransitionController
```

## Parameters

- `documentURL` — The URL of a document. Only use URLs provided by the document browser (for example, URLs passed to the delegate’s [- documentBrowser:didRequestDocumentCreationWithHandler:](<../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>)method’s completion block).

## Return Value

Returns a newly instantiated transition controller. Its [loadingProgress](../uidocumentbrowsertransitioncontroller/loadingprogress.md) and [targetView](../uidocumentbrowsertransitioncontroller/targetview.md) properties are both set to `nil`.

## Discussion

For the animations to function properly, you must maintain a strong reference to the transition controller until all the animation sequences are complete.

For more about using the transition controller, see [UIDocumentBrowserTransitionController](../uidocumentbrowsertransitioncontroller.md).

> [!note] Note
> In Mac apps built with Mac Catalyst, the transition controller doesn’t generate animations. macOS doesn’t use animations when opening or closing documents.

## See Also

### Animating transitions

- [UIDocumentBrowserTransitionController](../uidocumentbrowsertransitioncontroller.md) — An object that implements the standard loading and transition animations for a document browser.
