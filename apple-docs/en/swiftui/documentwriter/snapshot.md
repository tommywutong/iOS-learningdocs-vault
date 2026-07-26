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
doc_path: /documentation/swiftui/documentwriter/snapshot
source_url: 'https://developer.apple.com/documentation/swiftui/documentwriter/snapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentwriter/snapshot.json'
content_hash: 'sha256:da564079334e8cf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentWriter](../documentwriter.md)

# Snapshot

<sub>Associated Type</sub>

The type representing the document’s content to write.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Snapshot
```

## Discussion

This is the same type returned by [snapshot(contentType:)](<../writabledocument/snapshot(contenttype_).md>). It crosses an actor boundary (from main actor to background), so use `sending` annotations or make it `Sendable`.

## See Also

### Writing a document

- [write(snapshot:to:previous:progress:)](<write(snapshot_to_previous_progress_).md>) — Writes the document content to disk. _(beta)_
- [Destination](destination.md) — The type of the destination location to write to. _(beta)_
