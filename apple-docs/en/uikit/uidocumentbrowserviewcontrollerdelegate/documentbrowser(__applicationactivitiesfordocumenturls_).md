---
title: 'documentBrowser(_:applicationActivitiesForDocumentURLs:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Aapplicationactivitiesfordocumenturls%3A%29.json'
content_hash: 'sha256:f053d17ae73e3e1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:applicationActivitiesForDocumentURLs:)

<sub>Instance Method</sub>

Asks the delegate for additional activities when displaying an activity view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, applicationActivitiesForDocumentURLs documentURLs: [URL]) -> [UIActivity]
```

## Parameters

- `controller` — The current document browser.

- `documentURLs` — The URL of one or more documents to share.

## Return Value

An array of custom [UIActivity](../uiactivity.md) objects.

## Discussion

The document browser displays an activity view when the user shares a document (for example, when the user long presses a document and then chooses Share from the Edit Menu).

Implement this method to add custom activities to the activity view. Create and return an array containing your custom [UIActivity](../uiactivity.md) subclasses. Your [UIActivity](../uiactivity.md) subclasses should perform actions on the URLs passed to this method.

> [!note] Note
> Do not assume that the URL array contains only one URL. The user can place the document browser into Select mode and select multiple documents to share, even if the document browser’s [allowsPickingMultipleItems](../uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property is [false](../../swift/false.md).

## See Also

### Working with the browser’s activity view

- [- documentBrowser:willPresentActivityViewController:](<documentbrowser(__willpresent_).md>) — Tells the delegate that the document browser will display an activity view.
