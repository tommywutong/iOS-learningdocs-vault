---
title: dragItemsProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentproperties/dragitemsprovider
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentproperties/dragitemsprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentproperties/dragitemsprovider.json'
content_hash: 'sha256:8d4ef7159f33d8a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentProperties](../uidocumentproperties.md)

# dragItemsProvider

<sub>Instance Property</sub>

A closure that provides drag items that represent the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dragItemsProvider: ((any UIDragSession) -> [UIDragItem])? { get set }
```

## Discussion

To support drag and drop, assign a closure that returns an array of drag items that represent the document contents. When you set this property, a person can drag and drop the document from the navigation item’s title menu.
