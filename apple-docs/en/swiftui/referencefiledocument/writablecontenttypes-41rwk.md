---
title: writableContentTypes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/referencefiledocument/writablecontenttypes-41rwk
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument/writablecontenttypes-41rwk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument/writablecontenttypes-41rwk.json'
content_hash: 'sha256:2218bf774c611e23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReferenceFileDocument](../referencefiledocument.md)

# writableContentTypes

<sub>Type Property</sub>

The file types that the document supports saving or exporting to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var writableContentTypes: [UTType] { get }
```

## Discussion

By default, SwiftUI assumes that your document reads and writes the same set of content types. Only define this property if you need to indicate a different set of types for writing files. Otherwise, the default implementation of this property returns the list that you specify in your implementation of [readableContentTypes](readablecontenttypes.md).
