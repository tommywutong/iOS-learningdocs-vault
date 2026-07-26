---
title: 'init(document:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentviewcontroller/init(document:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/init(document:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/init%28document%3A%29.json'
content_hash: 'sha256:b5b325c0864f2bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# init(document:)

<sub>Initializer</sub>

Creates a document view controller with a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(document: UIDocument?)
```

## Parameters

- `document` — The document that the view controller presents.

## Return Value

A newly initialized [UIDocumentViewController](../uidocumentviewcontroller.md) object.

## Discussion

The document view controller opens and displays the document that you specify. If you don’t provide custom values, the new view controller gets its title and other information from the document itself.
