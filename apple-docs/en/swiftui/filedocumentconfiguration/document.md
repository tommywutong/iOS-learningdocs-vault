---
title: document
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentconfiguration/document
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentconfiguration/document'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentconfiguration/document.json'
content_hash: 'sha256:3278474ec1fc58ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocumentConfiguration](../filedocumentconfiguration.md)

# document

<sub>Instance Property</sub>

The current document model.

> [!warning] Deprecated
> Conform your type to Document and use URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@Binding var document: Document { get nonmutating set }
```

## Discussion

Setting a new value marks the document as having changes for later saving and registers an undo action to restore the model to its previous value.

If [isEditable](iseditable.md) is `false`, setting a new value has no effect because the document is in viewing mode.

## See Also

### Getting and setting the document

- [$document]($document.md) _(deprecated)_
