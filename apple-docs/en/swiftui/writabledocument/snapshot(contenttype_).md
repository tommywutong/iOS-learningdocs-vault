---
title: 'snapshot(contentType:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/writabledocument/snapshot(contenttype:)'
source_url: 'https://developer.apple.com/documentation/swiftui/writabledocument/snapshot(contenttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writabledocument/snapshot%28contenttype%3A%29.json'
content_hash: 'sha256:cdfcea997ed700af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WritableDocument](../writabledocument.md)

# snapshot(contentType:)

<sub>Instance Method</sub>

Captures the document’s current state for saving.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor func snapshot(contentType: UTType) async throws -> sending Self.Writer.Snapshot
```

## Parameters

- `contentType` — The format requested (one of [writableContentTypes](writablecontenttypes.md)).

## Discussion

SwiftUI calls this on the main actor when a save is needed. Keep this method lightweight — return a value that represents what to save, and perform actual serialization in [write(snapshot:to:previous:progress:)](<../documentwriter/write(snapshot_to_previous_progress_).md>).

## See Also

### Writing a document

- [writableContentTypes](writablecontenttypes.md) — The content types this document can save or export to. _(beta)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(beta)_
- [Writer](writer.md) — A type that implements writing to disk. _(beta)_
- [writer(configuration:)](<writer(configuration_).md>) — Creates a writer to save this document to disk. _(beta)_
