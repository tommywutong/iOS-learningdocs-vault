---
title: 'init(_:makeFileWrapper:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/filewrapperdocumentwriter/init(_:makefilewrapper:)'
source_url: 'https://developer.apple.com/documentation/swiftui/filewrapperdocumentwriter/init(_:makefilewrapper:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filewrapperdocumentwriter/init%28_%3Amakefilewrapper%3A%29.json'
content_hash: 'sha256:3173c048c6b313ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileWrapperDocumentWriter](../filewrapperdocumentwriter.md)

# init(_:makeFileWrapper:)

<sub>Initializer</sub>

Creates a writer that converts a snapshot into a `FileWrapper`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(_ configuration: sending FileWrapperDocumentWriter<Snapshot>.WriteConfiguration, makeFileWrapper: @escaping (Snapshot, FileWrapper?) async throws -> FileWrapper)
```

## Parameters

- `configuration` — Properties required to write a document to disk.

- `makeFileWrapper` — Serializes a `Snapshot` into a `FileWrapper`. The closure takes the following parameters: - `snapshot`: The snapshot to serialize into a `FileWrapper`. - `previous`: The previous file wrapper that can be reused to optimize writing. If the latest operation for the document was writing, it is the file wrapper used for writing. If the latest operation was reading, SwiftUI passes the file wrapper read by a companion `FileWrapperDocumentReader`.

## See Also

### Creating a writer

- [WriteConfiguration](writeconfiguration.md) _(beta)_
