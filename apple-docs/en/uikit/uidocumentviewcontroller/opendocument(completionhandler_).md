---
title: 'openDocument(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentviewcontroller/opendocument(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/opendocument(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/opendocument%28completionhandler%3A%29.json'
content_hash: 'sha256:50f7f4840d0ccfef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# openDocument(completionHandler:)

<sub>Instance Method</sub>

Opens a document in a document view controller from outside the document view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func openDocument(completionHandler: @escaping (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func openDocument() async -> Bool
```

## Parameters

- `completionHandler` — The function that executes after the document view controller opens the document

## See Also

### Managing the document view

- [document](document.md) — The document that the controller presents or edits.
- [- documentDidOpen](<documentdidopen().md>) — Provides an opportunity to configure the view after the system loads the controller’s document into memory.
