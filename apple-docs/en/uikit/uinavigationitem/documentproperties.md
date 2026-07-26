---
title: documentProperties
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/documentproperties
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/documentproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/documentproperties.json'
content_hash: 'sha256:877a5e31c9fb48b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# documentProperties

<sub>Instance Property</sub>

An object that provides the document header for the title menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var documentProperties: UIDocumentProperties? { get set }
```

## Discussion

Assign a non-`nil` value to this property to display a document header at the top of the title menu, which appears when a person taps the navigation item’s title. The document header displays information about the current document, such as its title, file type, and size. Additionally, you can configure a set of sharing capabilities that allow people to share or drag and drop the document content from the document header.

## See Also

### Customizing the title menu

- [titleMenuProvider](titlemenuprovider.md) — A closure that generates the navigation item’s title menu.
- [UIDocumentProperties](../uidocumentproperties.md) — Information that UIKit uses to generate a document header for a navigation item’s title menu.
