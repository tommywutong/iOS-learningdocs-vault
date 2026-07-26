---
title: ReferenceFileDocument
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocument
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocument.json'
content_hash: 'sha256:e743cd58421256c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ReferenceFileDocument

<sub>Protocol</sub>

A type that you use to serialize reference type documents to and from file.

> [!warning] Deprecated
> Use Document protocol instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@preconcurrency protocol ReferenceFileDocument : ObservableObject, Sendable
```

## Overview

To store a document as a reference type — like a class — create a type that conforms to the `ReferenceFileDocument` protocol and implement the required methods and properties. Your implementation:

- Provides a list of the content types that the document can read from and write to by defining [readableContentTypes](referencefiledocument/readablecontenttypes.md). If the list of content types that the document can write to is different from those that it reads from, you can optionally also define [writableContentTypes](referencefiledocument/writablecontenttypes.md).
- Loads documents from file in the [init(configuration:)](<referencefiledocument/init(configuration_).md>) initializer.
- Stores documents to file by providing a snapshot of the document’s content in the [snapshot(contentType:)](<referencefiledocument/snapshot(contenttype_).md>) method, and then serializing that content in the [fileWrapper(snapshot:configuration:)](<referencefiledocument/filewrapper(snapshot_configuration_).md>) method.

Ensure that types that conform to this protocol are `Sendable`. In particular, SwiftUI calls the protocol’s methods from different isolation domains. Don’t perform serialization and deserialization on `MainActor`.

```swift
final class PDFDocument: ReferenceFileDocument {
    struct Storage {
        var contents: Data
    }

    static let readableContentTypes: [UTType] = [.pdf]
    let storage: Mutex<Storage>

    required init(configuration: ReadConfiguration) throws {
       guard let data = configuration.file.regularFileContents else {
           throw CocoaError(.fileReadCorruptFile)
       }
        self.storage = .init(.init(contents: data))
    }

    func snapshot(contentType: UTType) throws -> Data {
        storage.withLock { $0.contents }
    }

    func fileWrapper(snapshot: Data, configuration: WriteConfiguration) throws -> FileWrapper {
        return FileWrapper(regularFileWithContents: snapshot)
    }
}
```

> [!important] Important
> If you store your document as a value type — like a structure — use [FileDocument](filedocument.md) instead.

## Relationships

- **Inherits From**: [ObservableObject](../combine/observableobject.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reading a document

- [init(configuration:)](<referencefiledocument/init(configuration_).md>) — Creates a document and initializes it with the contents of a file. _(deprecated)_
- [readableContentTypes](referencefiledocument/readablecontenttypes.md) — The file and data types that the document reads from. _(deprecated)_
- [ReadConfiguration](referencefiledocument/readconfiguration.md) — The configuration for reading document contents. _(deprecated)_

### Getting a snapshot

- [snapshot(contentType:)](<referencefiledocument/snapshot(contenttype_).md>) — Creates a snapshot that represents the current state of the document. _(deprecated)_
- [Snapshot](referencefiledocument/snapshot.md) — A type that represents the document’s stored content. _(deprecated)_

### Writing a document

- [fileWrapper(snapshot:configuration:)](<referencefiledocument/filewrapper(snapshot_configuration_).md>) — Serializes a document snapshot to a file wrapper. _(deprecated)_
- [writableContentTypes](referencefiledocument/writablecontenttypes.md) — The file types that the document supports saving or exporting to. _(deprecated)_
- [WriteConfiguration](referencefiledocument/writeconfiguration.md) — The configuration for writing document contents. _(deprecated)_

## See Also

### Deprecated

- [FileDocument](filedocument.md) — A type that you use to serialize documents to and from file. _(deprecated)_
- [FileDocumentConfiguration](filedocumentconfiguration.md) — The properties of an open file document. _(deprecated)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — The configuration for reading file contents. _(deprecated)_
- [FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md) — The configuration for serializing file contents. _(deprecated)_
- [NewDocumentAction](newdocumentaction.md) — An action that presents a new document. _(deprecated)_
- [ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md) — The properties of an open reference file document. _(deprecated)_
