---
title: DocumentWriteConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentwriteconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/documentwriteconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentwriteconfiguration.json'
content_hash: 'sha256:9d4333be29f8b43d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentWriteConfiguration

<sub>Structure</sub>

The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DocumentWriteConfiguration
```

## Overview

Contains the [contentType](documentwriteconfiguration/contenttype.md) of the file being written (one of the document’s [writableContentTypes](writabledocument/writablecontenttypes.md)). Use it to choose the correct serialization strategy when a document supports exporting to multiple formats.

Access this type through the [WriteConfiguration](writabledocument/writeconfiguration.md) typealias.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md)

## Topics

### Accessing write properties

- [contentType](documentwriteconfiguration/contenttype.md) — The content type of the file being written. _(beta)_

## See Also

### Reading and writing documents

- [DocumentReadConfiguration](documentreadconfiguration.md) — The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>). _(beta)_
- [DocumentReader](documentreader.md) — A type that reads a document’s content from a file. _(beta)_
- [DocumentWriter](documentwriter.md) — A type that writes a document’s content to a file. _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — A document reader that deserializes a `FileWrapper` into a snapshot. _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — A document writer that serializes a snapshot into a `FileWrapper`. _(beta)_
