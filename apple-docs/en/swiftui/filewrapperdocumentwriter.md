---
title: FileWrapperDocumentWriter
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/filewrapperdocumentwriter
source_url: 'https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filewrapperdocumentwriter.json'
content_hash: 'sha256:e440054420340687'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FileWrapperDocumentWriter

<sub>Structure</sub>

A document writer that serializes a snapshot into a `FileWrapper`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FileWrapperDocumentWriter<Snapshot>
```

## Overview

The `makeFileWrapper` closure in [init(_:makeFileWrapper:)](<filewrapperdocumentwriter/init(__makefilewrapper_).md>) turns the document’s snapshot into a `FileWrapper` that SwiftUI writes to disk. It receives the current snapshot and, when available, the `FileWrapper` from the document’s last read or write. For documents written as a single file, ignore `previous` and return a freshly built wrapper:

```swift
extension TextDocument: WritableDocument {
    func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(regularFileWithContents: Data(snapshot.utf8))
        }
    }

    // ...
}
```

## Relationships

- **Conforms To**: [DocumentWriter](documentwriter.md)

## Topics

### Creating a writer

- [init(_:makeFileWrapper:)](<filewrapperdocumentwriter/init(__makefilewrapper_).md>) — Creates a writer that converts a snapshot into a `FileWrapper`. _(beta)_
- [WriteConfiguration](filewrapperdocumentwriter/writeconfiguration.md) _(beta)_

## See Also

### Reading and writing documents

- [DocumentReadConfiguration](documentreadconfiguration.md) — The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>). _(beta)_
- [DocumentWriteConfiguration](documentwriteconfiguration.md) — The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>). _(beta)_
- [DocumentReader](documentreader.md) — A type that reads a document’s content from a file. _(beta)_
- [DocumentWriter](documentwriter.md) — A type that writes a document’s content to a file. _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — A document reader that deserializes a `FileWrapper` into a snapshot. _(beta)_
