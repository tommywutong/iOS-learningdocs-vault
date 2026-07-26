---
title: 'createDocumentAction(withIntent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction(withintent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction(withintent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/createdocumentaction%28withintent%3A%29.json'
content_hash: 'sha256:d624769eda86d45c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocumentViewController](../../uidocumentviewcontroller.md) · [LaunchOptions](../launchoptions-swift.class.md)

# createDocumentAction(withIntent:)

<sub>Type Method</sub>

Creates an action that uses the specified intent.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func createDocumentAction(withIntent intent: UIDocument.CreationIntent) -> UIAction
```

## Parameters

- `intent` — An intent that defines how your app creates the document.

## Discussion

Use this method to create an action that you can assign to your [primaryAction](primaryaction.md) or [secondaryAction](secondaryaction.md). When the system triggers the action, it calls your [UIDocumentBrowserViewControllerDelegate](../../uidocumentbrowserviewcontrollerdelegate.md) object’s [- documentBrowser:didRequestDocumentCreationWithHandler:](<../../uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method. For more information, see [Customizing a document-based app’s launch experience](../../customizing-a-document-based-app-s-launch-experience.md).
