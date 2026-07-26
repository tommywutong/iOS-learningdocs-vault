---
title: DocumentWriter
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentwriter
source_url: 'https://developer.apple.com/documentation/swiftui/documentwriter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentwriter.json'
content_hash: 'sha256:ab8ffc396a3d961b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentWriter

<sub>Protocol</sub>

A type that writes a document’s content to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol DocumentWriter<Snapshot>
```

## Overview

SwiftUI calls your document’s [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>) on the main actor to capture the current state, then obtains a `DocumentWriter` from [writer(configuration:)](<writabledocument/writer(configuration_).md>) and invokes `write(content:to:previous:progress:)` in the background with coordinated file access.

Use [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) for cases cases that don’t require custom file write logic. Implement a `DocumentWriter` when you need direct URL access or streaming writes:

```swift
struct ImageWriter: DocumentWriter {
    @concurrent
    func write(content image: sending CGImage, to destination: URL,
        previous: sending CGImage?, progress: consuming Subprogress
    ) async throws {
        guard let imageDestination =
            CGImageDestinationCreateWithURL(
                destination as CFURL,
                UTType.jpeg.identifier as CFString,
                1, nil
            ) else {
            throw CocoaError(.fileWriteUnknown)
        }
        CGImageDestinationAddImage(
            imageDestination, image, nil
        )
        guard CGImageDestinationFinalize(
            imageDestination
        ) else {
            throw CocoaError(.fileWriteUnknown)
        }
    }
}
```

## Relationships

- **Conforming Types**: [FileWrapperDocumentWriter](filewrapperdocumentwriter.md)

## Topics

### Writing a document

- [write(snapshot:to:previous:progress:)](<documentwriter/write(snapshot_to_previous_progress_).md>) — Writes the document content to disk. _(beta)_
- [Snapshot](documentwriter/snapshot.md) — The type representing the document’s content to write. _(beta)_
- [Destination](documentwriter/destination.md) — The type of the destination location to write to. _(beta)_

## See Also

### Reading and writing documents

- [DocumentReadConfiguration](documentreadconfiguration.md) — The context SwiftUI passes to [reader(configuration:)](<readabledocument/reader(configuration_).md>). _(beta)_
- [DocumentWriteConfiguration](documentwriteconfiguration.md) — The context SwiftUI passes to [writer(configuration:)](<writabledocument/writer(configuration_).md>). _(beta)_
- [DocumentReader](documentreader.md) — A type that reads a document’s content from a file. _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — A document reader that deserializes a `FileWrapper` into a snapshot. _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — A document writer that serializes a snapshot into a `FileWrapper`. _(beta)_
