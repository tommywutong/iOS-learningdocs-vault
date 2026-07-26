---
title: 'write(snapshot:to:previous:progress:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/documentwriter/write(snapshot:to:previous:progress:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentwriter/write(snapshot:to:previous:progress:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentwriter/write%28snapshot%3Ato%3Aprevious%3Aprogress%3A%29.json'
content_hash: 'sha256:7baecd56f66f744f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentWriter](../documentwriter.md)

# write(snapshot:to:previous:progress:)

<sub>Instance Method</sub>

Writes the document content to disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@concurrent func write(snapshot: sending Self.Snapshot, to destination: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws
```

## Parameters

- `snapshot` — The snapshot to write to disk.

- `destination` — The file URL to write to.

- `previous` — The last successfully written snapshot, or `nil` on the first save. Compare to `content` to write only what changed in package documents.

- `progress` — A `Subprogress` value to report writing progress. Consume it once with `reporter(totalCount:)` and call `complete(count:)` as units finish.

## Discussion

SwiftUI calls this method in the background after obtaining a snapshot via [snapshot(contentType:)](<../writabledocument/snapshot(contenttype_).md>). Perform all serialization and disk access here.

For most documents, use [FileWrapperDocumentWriter](../filewrapperdocumentwriter.md) instead of implementing a custom writer. Only implement `write` yourself when you need capabilities `FileWrapperDocumentWriter` doesn’t provide — such as direct URL access for Core Graphics, AVFoundation, or other frameworks that operate on file paths:

```swift
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
```

## See Also

### Writing a document

- [Snapshot](snapshot.md) — The type representing the document’s content to write. _(beta)_
- [Destination](destination.md) — The type of the destination location to write to. _(beta)_
