---
title: DocumentReadConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentreadconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/documentreadconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentreadconfiguration.json'
content_hash: 'sha256:4dad0bc151792a32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentReadConfiguration

<sub>Structure</sub>

The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DocumentReadConfiguration
```

## Overview

Contains the [contentType](documentreadconfiguration/contenttype.md) of the file being read (one of the document’s [readableContentTypes](readabledocument/readablecontenttypes.md)). Use it to choose the correct deserialization strategy when a document supports multiple formats.

Access this type through the [ReadConfiguration](readabledocument/readconfiguration.md) typealias.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md)

## Topics

### Accessing read properties

- [contentType](documentreadconfiguration/contenttype.md) — The content type of the file being read. _(beta)_

## See Also

### Reading and writing documents

- [DocumentWriteConfiguration](documentwriteconfiguration.md) — The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>). _(beta)_
- [DocumentReader](documentreader.md) — A type that reads a document’s content from a file. _(beta)_
- [DocumentWriter](documentwriter.md) — A type that writes a document’s content to a file. _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — A document reader that deserializes a `FileWrapper` into a snapshot. _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — A document writer that serializes a snapshot into a `FileWrapper`. _(beta)_
