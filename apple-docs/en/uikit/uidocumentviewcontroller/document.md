---
title: document
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/document
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/document'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/document.json'
content_hash: 'sha256:158a99871a814a90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# document

<sub>Instance Property</sub>

The document that the controller presents or edits.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var document: UIDocument? { get set }
```

## Discussion

This property represents the document that the document view controller displays. The default value of this property is `nil`. When the value of the `document` property is `nil`, the document view controller presents an empty state view with a message to “Select a document by tapping the ‘Documents’ button at the top.”

When the value of this property is not `nil`, the document view controller displays the document.

## See Also

### Managing the document view

- [- openDocumentWithCompletionHandler:](<opendocument(completionhandler_).md>) — Opens a document in a document view controller from outside the document view controller.
- [- documentDidOpen](<documentdidopen().md>) — Provides an opportunity to configure the view after the system loads the controller’s document into memory.
