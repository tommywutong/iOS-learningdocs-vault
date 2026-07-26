---
title: FileWrapperDocumentReader
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/filewrapperdocumentreader
source_url: 'https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filewrapperdocumentreader.json'
content_hash: 'sha256:2fae7fabc6667c6b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FileWrapperDocumentReader

<sub>Structure</sub>

A document reader that deserializes a `FileWrapper` into a snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FileWrapperDocumentReader<Snapshot>
```

## Overview

This is the recommended reader for most documents. Provide a closure that converts a `FileWrapper` into your snapshot type, and `FileWrapperDocumentReader` handles file coordination and loading.

```swift
func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
    FileWrapperDocumentReader(configuration) { fileWrapper in
        guard let data =
            fileWrapper.regularFileContents else {
            throw CocoaError(.fileReadCorruptFile)
        }
        return String(decoding: data, as: UTF8.self)
    }
}
```

For package documents, navigate the `FileWrapper` hierarchy:

```swift
FileWrapperDocumentReader(configuration) { directory in
    let children = directory.fileWrappers ?? [:]
    guard let metadataData = children["metadata.json"]?
        .regularFileContents else {
        throw CocoaError(.fileReadCorruptFile)
    }
    return try JSONDecoder().decode(
        Metadata.self, from: metadataData
    )
}
```

> [!important] Important
> `FileWrapper` loads file contents on demand. A child file may be gone by the time you call `regularFileContents`. Always handle errors when reading children of a package.

The closure does not receive a `Subprogress`. To report progress during reads, use a custom [DocumentReader](documentreader.md) instead.

## Relationships

- **Conforms To**: [DocumentReader](documentreader.md)

## Topics

### Creating a reader

- [init(_:makeSnapshot:)](<filewrapperdocumentreader/init(__makesnapshot_).md>) — Creates a reader that converts a `FileWrapper` into a snapshot. _(beta)_
- [ReadConfiguration](filewrapperdocumentreader/readconfiguration.md) _(beta)_

## See Also

### Reading and writing documents

- [DocumentReadConfiguration](documentreadconfiguration.md) — The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>). _(beta)_
- [DocumentWriteConfiguration](documentwriteconfiguration.md) — The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>). _(beta)_
- [DocumentReader](documentreader.md) — A type that reads a document’s content from a file. _(beta)_
- [DocumentWriter](documentwriter.md) — A type that writes a document’s content to a file. _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — A document writer that serializes a snapshot into a `FileWrapper`. _(beta)_
