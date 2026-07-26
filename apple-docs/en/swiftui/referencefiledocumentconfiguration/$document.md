---
title: $document
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocumentconfiguration/$document
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/$document'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocumentconfiguration/%24document.json'
content_hash: 'sha256:8987e25b916f64d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocumentConfiguration](../referencefiledocumentconfiguration.md)

# $document

<sub>Instance Property</sub>

> [!warning] Deprecated
> Use Document protocol and URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency var $document: ObservedObject<Document>.Wrapper { get }
```

## See Also

### Getting and setting the document

- [document](document.md) — The current document model. _(deprecated)_
