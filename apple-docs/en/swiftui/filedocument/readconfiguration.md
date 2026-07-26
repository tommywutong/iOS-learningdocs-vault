---
title: FileDocument.ReadConfiguration
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocument/readconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/filedocument/readconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocument/readconfiguration.json'
content_hash: 'sha256:75b02f08945f64f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocument](../filedocument.md)

# FileDocument.ReadConfiguration

<sub>Type Alias</sub>

The configuration for reading document contents.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
typealias ReadConfiguration = FileDocumentReadConfiguration
```

## Discussion

This type is an alias for [FileDocumentReadConfiguration](../filedocumentreadconfiguration.md), which contains a content type and a file wrapper that you use to access the contents of a document file. You get a value of this type as an input to the [init(configuration:)](<init(configuration_).md>) initializer. Use it to load a document from a file.

## See Also

### Reading a document

- [init(configuration:)](<init(configuration_).md>) — Creates a document and initializes it with the contents of a file. _(deprecated)_
- [readableContentTypes](readablecontenttypes.md) — The file and data types that the document reads from. _(deprecated)_
