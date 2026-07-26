---
title: fileURL
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/urldocumentconfiguration/fileurl
source_url: 'https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/fileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/urldocumentconfiguration/fileurl.json'
content_hash: 'sha256:9009a8d48a866316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [URLDocumentConfiguration](../urldocumentconfiguration.md)

# fileURL

<sub>Instance Property</sub>

A URL of the open document if it is saved to disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor final var fileURL: URL? { get set }
```

## Discussion

Returns `nil` if the document has never been saved.

## See Also

### Accessing document properties

- [lastContentModificationDate](lastcontentmodificationdate.md) — The date on which the contents of the document were last modified, if available. _(beta)_
- [creationSource](creationsource.md) — The source associated with the button that created this document. _(beta)_
