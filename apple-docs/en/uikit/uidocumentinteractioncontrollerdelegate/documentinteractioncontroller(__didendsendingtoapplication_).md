---
title: 'documentInteractionController(_:didEndSendingToApplication:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:didendsendingtoapplication:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:didendsendingtoapplication:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller%28_%3Adidendsendingtoapplication%3A%29.json'
content_hash: 'sha256:1b9aa324b678bbca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionControllerDelegate](../uidocumentinteractioncontrollerdelegate.md)

# documentInteractionController(_:didEndSendingToApplication:)

<sub>Instance Method</sub>

Called when a document interaction controller’s document has been handed off to the specified application.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String?)
```

## Parameters

- `controller` — The document interaction controller whose document is about to be opened.

- `application` — The bundle identifier of the application that is about to open the document. This value corresponds to the value in the `CFBundleIdentifier` key of the application’s `Info.plist` file.

## Discussion

This method is called after the document information has been saved for the specified application.

## See Also

### Opening files

- [- documentInteractionController:willBeginSendingToApplication:](<documentinteractioncontroller(__willbeginsendingtoapplication_).md>) — Called when a document interaction controller’s document is about to be opened by the specified application.
