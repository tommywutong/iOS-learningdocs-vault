---
title: ReadableDocument
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/readabledocument
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument.json'
content_hash: 'sha256:48d08d2a801e4d04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ReadableDocument

<sub>Protocol</sub>

A document type that supports reading from file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol ReadableDocument : AnyObject
```

## Overview

Conform to `ReadableDocument` to build a read-only document viewer, or combine with [WritableDocument](writabledocument.md) (via the [Document](document.md) protocol) for full read-write support.

A readable document is a reference type so that SwiftUI can maintain a stable identity across updates. Use `@Observable` to enable per-property change tracking:

```swift
@Observable
final class MarkdownViewer: ReadableDocument {
    static let readableContentTypes: [UTType] = [.markdown]

    var attributedText = AttributedString()

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data =
                fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        attributedText = try AttributedString(
            markdown: snapshot
        )
    }
}
```

Present a read-only document with [DocumentGroup](documentgroup.md) using the viewer initializer:

```swift
DocumentGroup { document in
    MarkdownView(document: document)
} makeReadableDocument: { configuration, context in
    MarkdownViewer()
}
```

Set `CFBundleTypeRole` to `Viewer` in your Info.plist for read-only document types.

## Relationships

- **Inherited By**: [Document](document.md)

## Topics

### Reading a document

- [readableContentTypes](readabledocument/readablecontenttypes.md) — The content types this document can open. _(beta)_
- [ReadConfiguration](readabledocument/readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [Reader](readabledocument/reader.md) — A type that implements reading from disk. _(beta)_
- [reader(configuration:)](<readabledocument/reader(configuration_).md>) — Creates a reader to load this document from disk. _(beta)_
- [apply(snapshot:previous:)](<readabledocument/apply(snapshot_previous_).md>) — Applies a loaded snapshot to the document model. _(beta)_
- [writableContentTypes](readabledocument/writablecontenttypes.md) — By default, a document that supports reading also supports writing the same content types. _(beta)_

## See Also

### Storing document data in a reference type instance

- [Document](document.md) — A document that supports both reading and writing. _(beta)_
- [WritableDocument](writabledocument.md) — A document type that supports writing to file. _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — The configuration of an open document that stores its file URL, last modification date, and related metadata. _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — Context about how a document was created. _(beta)_
- [DocumentBaseBox](documentbasebox.md) — A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
