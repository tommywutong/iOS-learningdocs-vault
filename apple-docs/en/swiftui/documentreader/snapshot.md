---
title: Snapshot
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentreader/snapshot
source_url: 'https://developer.apple.com/documentation/swiftui/documentreader/snapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentreader/snapshot.json'
content_hash: 'sha256:82df45678ec0dd2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentReader](../documentreader.md)

# Snapshot

<sub>Associated Type</sub>

The type representing the document’s content after reading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Snapshot
```

## Discussion

This can be any type: a `String`, a custom struct, or even the document type itself. SwiftUI delivers it to [apply(snapshot:previous:)](<../readabledocument/apply(snapshot_previous_).md>) on the main actor after reading completes.

## See Also

### Reading a document

- [read(from:progress:)](<read(from_progress_).md>) — Reads the document’s content from disk. _(beta)_
- [Source](source.md) — The type of the source location to read from. _(beta)_
