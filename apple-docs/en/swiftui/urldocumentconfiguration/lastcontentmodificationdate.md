---
title: lastContentModificationDate
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/urldocumentconfiguration/lastcontentmodificationdate
source_url: 'https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/lastcontentmodificationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/urldocumentconfiguration/lastcontentmodificationdate.json'
content_hash: 'sha256:7b34fb14b072913b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [URLDocumentConfiguration](../urldocumentconfiguration.md)

# lastContentModificationDate

<sub>Instance Property</sub>

The date on which the contents of the document were last modified, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor final var lastContentModificationDate: Date? { get set }
```

## See Also

### Accessing document properties

- [fileURL](fileurl.md) — A URL of the open document if it is saved to disk. _(beta)_
- [creationSource](creationsource.md) — The source associated with the button that created this document. _(beta)_
