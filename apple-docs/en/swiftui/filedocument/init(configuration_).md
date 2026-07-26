---
title: 'init(configuration:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/filedocument/init(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/filedocument/init(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocument/init%28configuration%3A%29.json'
content_hash: 'sha256:85009b50a2db1a59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocument](../filedocument.md)

# init(configuration:)

<sub>Initializer</sub>

Creates a document and initializes it with the contents of a file.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(configuration: Self.ReadConfiguration) throws
```

## Parameters

- `configuration` — Information about the file that you read document data from.

## Discussion

SwiftUI calls this initializer when someone opens a file type that matches one of those that your document type supports. Use the [file](../filedocumentreadconfiguration/file.md) property of the `configuration` input to get document’s data. Deserialize the data, and store it in your document’s data structure:

```swift
init(configuration: ReadConfiguration) throws {
    guard let data = configuration.file.regularFileContents
    else { /* Throw an error. */ }
    model = try JSONDecoder().decode(Model.self, from: data)
}
```

The above example assumes that you define `Model` to contain the document’s data, that `Model` conforms to the [Codable](../../swift/codable.md) protocol, and that you store a `model` property of that type inside your document.

> [!note] Note
> SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## See Also

### Reading a document

- [readableContentTypes](readablecontenttypes.md) — The file and data types that the document reads from. _(deprecated)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(deprecated)_
