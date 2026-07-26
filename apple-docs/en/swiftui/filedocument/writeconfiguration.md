---
title: FileDocument.WriteConfiguration
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocument/writeconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/filedocument/writeconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocument/writeconfiguration.json'
content_hash: 'sha256:2588982b5ea47a21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocument](../filedocument.md)

# FileDocument.WriteConfiguration

<sub>Type Alias</sub>

The configuration for writing document contents.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
typealias WriteConfiguration = FileDocumentWriteConfiguration
```

## Discussion

This type is an alias for [FileDocumentWriteConfiguration](../filedocumentwriteconfiguration.md), which contains a content type and a file wrapper that you use to access the contents of a document file, if one already exists. You get a value of this type as an input to the [fileWrapper(configuration:)](<filewrapper(configuration_).md>) method.

## See Also

### Writing a document

- [fileWrapper(configuration:)](<filewrapper(configuration_).md>) — Serializes a document snapshot to a file wrapper. _(deprecated)_
- [writableContentTypes](writablecontenttypes.md) — The file types that the document supports saving or exporting to. _(deprecated)_
