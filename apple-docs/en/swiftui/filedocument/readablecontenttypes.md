---
title: readableContentTypes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocument/readablecontenttypes
source_url: 'https://developer.apple.com/documentation/swiftui/filedocument/readablecontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocument/readablecontenttypes.json'
content_hash: 'sha256:e92e3588750c94dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocument](../filedocument.md)

# readableContentTypes

<sub>Type Property</sub>

The file and data types that the document reads from.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var readableContentTypes: [UTType] { get }
```

## Discussion

Define this list to indicate the content types that your document can read. By default, SwiftUI assumes that your document can also write the same set of content types. If you need to indicate a different set of types for writing files, define the [writableContentTypes](writablecontenttypes.md) property in addition to this property.

## See Also

### Reading a document

- [init(configuration:)](<init(configuration_).md>) — Creates a document and initializes it with the contents of a file. _(deprecated)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(deprecated)_
