---
title: DocumentReader
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentreader
source_url: 'https://developer.apple.com/documentation/swiftui/documentreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentreader.json'
content_hash: 'sha256:a49a97f070d11721'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentReader

<sub>Protocol</sub>

A type that reads a document’s content from a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol DocumentReader<Snapshot>
```

## Overview

SwiftUI calls your document’s [reader(configuration:)](<readabledocument/reader(configuration_).md>) method to obtain a `DocumentReader`, then invokes [read(from:progress:)](<documentreader/read(from_progress_).md>) in the background with coordinated file access. The returned snapshot is delivered to [apply(snapshot:previous:)](<readabledocument/apply(snapshot_previous_).md>) on the main actor.

Use [FileWrapperDocumentReader](filewrapperdocumentreader.md) for cases that don’t require custom file read logic. Implement a `DocumentReader` when you need direct URL access for frameworks like Core Graphics, AVFoundation, or PDFKit:

```swift
struct ImageReader: DocumentReader {
    @concurrent
    func read(from source: URL, progress: consuming Subprogress)
        async throws -> sending CGImage {
        guard let provider =
            CGDataProvider(url: source as CFURL),
              let image = CGImage(
                  jpegDataProviderSource: provider,
                  decode: nil, shouldInterpolate: true,
                  intent: .defaultIntent
              ) else {
            throw CocoaError(.fileReadCorruptFile)
        }
        return image
    }
}
```

SwiftUI provides the document’s file URL as the reader’s source.

## Relationships

- **Conforming Types**: [FileWrapperDocumentReader](filewrapperdocumentreader.md)

## Topics

### Reading a document

- [read(from:progress:)](<documentreader/read(from_progress_).md>) — Reads the document’s content from disk. _(beta)_
- [Snapshot](documentreader/snapshot.md) — The type representing the document’s content after reading. _(beta)_
- [Source](documentreader/source.md) — The type of the source location to read from. _(beta)_

## See Also

### Reading and writing documents

- [DocumentReadConfiguration](documentreadconfiguration.md) — The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>). _(beta)_
- [DocumentWriteConfiguration](documentwriteconfiguration.md) — The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>). _(beta)_
- [DocumentWriter](documentwriter.md) — A type that writes a document’s content to a file. _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — A document reader that deserializes a `FileWrapper` into a snapshot. _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — A document writer that serializes a snapshot into a `FileWrapper`. _(beta)_
