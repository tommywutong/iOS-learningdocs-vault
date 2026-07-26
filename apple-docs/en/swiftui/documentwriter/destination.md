---
title: Destination
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentwriter/destination
source_url: 'https://developer.apple.com/documentation/swiftui/documentwriter/destination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentwriter/destination.json'
content_hash: 'sha256:697fb7c54bd5548c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentWriter](../documentwriter.md)

# Destination

<sub>Associated Type</sub>

The type of the destination location to write to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Destination = URL
```

## Discussion

SwiftUI provides the document’s file URL as the destination.

## See Also

### Writing a document

- [write(snapshot:to:previous:progress:)](<write(snapshot_to_previous_progress_).md>) — Writes the document content to disk. _(beta)_
- [Snapshot](snapshot.md) — The type representing the document’s content to write. _(beta)_
