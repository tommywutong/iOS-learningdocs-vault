---
title: 'read(from:progress:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/documentreader/read(from:progress:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentreader/read(from:progress:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentreader/read%28from%3Aprogress%3A%29.json'
content_hash: 'sha256:5a12ea6ad47fafb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentReader](../documentreader.md)

# read(from:progress:)

<sub>Instance Method</sub>

Reads the document’s content from disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@concurrent func read(from source: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot
```

## Parameters

- `source` — The file URL to read from.

- `progress` — A `Subprogress` value to report reading progress. Consume it once with `reporter(totalCount:)` and call `complete(count:)` as units finish.

## Return Value

A snapshot representing the document’s content.

## Discussion

SwiftUI calls this method in the background with coordinated file access. Perform all deserialization and disk access here — the returned snapshot is delivered to [apply(snapshot:previous:)](<../readabledocument/apply(snapshot_previous_).md>) on the main actor.

For most documents, use [FileWrapperDocumentReader](../filewrapperdocumentreader.md) instead of implementing a custom reader. Only implement `read` yourself when you need capabilities `FileWrapperDocumentReader` doesn’t provide — such as direct URL access for Core Graphics, AVFoundation, or other frameworks that operate on file paths:

```swift
@concurrent
func read(from source: URL, progress: consuming Subprogress)
    async throws -> sending CGImage {
    guard let imageSource =
        CGImageSourceCreateWithURL(source as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(
              imageSource, 0, nil
          ) else {
        throw CocoaError(.fileReadCorruptFile)
    }
    return image
}
```

## See Also

### Reading a document

- [Snapshot](snapshot.md) — The type representing the document’s content after reading. _(beta)_
- [Source](source.md) — The type of the source location to read from. _(beta)_
