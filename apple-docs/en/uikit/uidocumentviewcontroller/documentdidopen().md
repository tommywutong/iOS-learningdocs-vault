---
title: documentDidOpen()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/documentdidopen()
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/documentdidopen()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/documentdidopen%28%29.json'
content_hash: 'sha256:794f5ed34da1c846'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# documentDidOpen()

<sub>Instance Method</sub>

Provides an opportunity to configure the view after the system loads the controller’s document into memory.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func documentDidOpen()
```

## Discussion

The system calls this method after the document view controller opens its document, or when an object assigns an already opened document to the document view controller’s `document` property. Override this method to customize the views that present your document in the view:

```swift
override func documentDidOpen() {
    configureViewForCurrentDocument()
}
```

Configure the view in its own method and call that method in both `documentDidOpen()` and [- viewDidLoad](<../uiviewcontroller/viewdidload().md>). There is no timing guarantee between when the system calls `documentDidOpen` and when it loads the view controller’s view.

## See Also

### Managing the document view

- [document](document.md) — The document that the controller presents or edits.
- [- openDocumentWithCompletionHandler:](<opendocument(completionhandler_).md>) — Opens a document in a document view controller from outside the document view controller.
