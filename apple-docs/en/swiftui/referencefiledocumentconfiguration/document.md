---
title: document
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocumentconfiguration/document
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/document'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocumentconfiguration/document.json'
content_hash: 'sha256:705d8fe0e0d0f519'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocumentConfiguration](../referencefiledocumentconfiguration.md)

# document

<sub>Instance Property</sub>

The current document model.

> [!warning] Deprecated
> Use Document protocol and URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ObservedObject<Document> @MainActor @preconcurrency var document: Document { get set }
```

## Discussion

Changes to the document dirty the document state, indicating that it needs to be saved. SwiftUI doesn’t automatically register undo actions.

## See Also

### Getting and setting the document

- [$document]($document.md) _(deprecated)_
