---
title: 'documentInteractionController(_:willBeginSendingToApplication:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:willbeginsendingtoapplication:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:willbeginsendingtoapplication:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller%28_%3Awillbeginsendingtoapplication%3A%29.json'
content_hash: 'sha256:c4ff6eafd1ad1365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionController(_:willBeginSendingToApplication:)

<sub>Instance Method</sub>

Called when a document interaction controller’s document is about to be opened by the specified application.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String?)
```

## Parameters

- `controller` — The document interaction controller whose document is about to be opened.

- `application` — The bundle identifier of the application that is about to open the document. This value corresponds to the value in the `CFBundleIdentifier` key of the application’s `Info.plist` file.

## Discussion

This method is called when the user chooses to open a document, which could occur from within a document preview. When a document is passed to another application, the contents of the document interaction controller’s [annotation](../uidocumentinteractioncontroller/annotation.md) property are passed with it. You can use this method to configure the contents of that property or prepare your own application for handing off the document.

## See Also

### Opening files

- [- documentInteractionController:didEndSendingToApplication:](<documentinteractioncontroller(__didendsendingtoapplication_).md>) — Called when a document interaction controller’s document has been handed off to the specified application.
