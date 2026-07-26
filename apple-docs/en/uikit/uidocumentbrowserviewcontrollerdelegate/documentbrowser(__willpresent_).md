---
title: 'documentBrowser(_:willPresent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:willpresent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:willpresent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Awillpresent%3A%29.json'
content_hash: 'sha256:5b3dff617df9eda9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:willPresent:)

<sub>Instance Method</sub>

Tells the delegate that the document browser will display an activity view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, willPresent activityViewController: UIActivityViewController)
```

## Parameters

- `controller` — The current document browser.

- `activityViewController` — The activity view controller to be displayed.

## Discussion

The document browser displays an activity view when the user shares a document (for example, when the user long presses a document and then chooses Share from the Edit Menu).

Implement this method to customize the activity view before it is displayed. For example, you could exclude any system-provided activities that are inappropriate for your app (see the [UIActivityViewController](../uiactivityviewcontroller.md) class’s [excludedActivityTypes](../uiactivityviewcontroller/excludedactivitytypes.md) property).

## See Also

### Working with the browser’s activity view

- [- documentBrowser:applicationActivitiesForDocumentURLs:](<documentbrowser(__applicationactivitiesfordocumenturls_).md>) — Asks the delegate for additional activities when displaying an activity view.
