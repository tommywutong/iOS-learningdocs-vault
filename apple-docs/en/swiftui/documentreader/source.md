---
title: Source
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentreader/source
source_url: 'https://developer.apple.com/documentation/swiftui/documentreader/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentreader/source.json'
content_hash: 'sha256:0af34738d9961c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentReader](../documentreader.md)

# Source

<sub>Associated Type</sub>

The type of the source location to read from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Source = URL
```

## Discussion

SwiftUI provides the document’s file URL as the source.

## See Also

### Reading a document

- [read(from:progress:)](<read(from_progress_).md>) — Reads the document’s content from disk. _(beta)_
- [Snapshot](snapshot.md) — The type representing the document’s content after reading. _(beta)_
