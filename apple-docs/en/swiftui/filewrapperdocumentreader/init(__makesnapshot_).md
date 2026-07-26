---
title: 'init(_:makeSnapshot:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/filewrapperdocumentreader/init(_:makesnapshot:)'
source_url: 'https://developer.apple.com/documentation/swiftui/filewrapperdocumentreader/init(_:makesnapshot:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filewrapperdocumentreader/init%28_%3Amakesnapshot%3A%29.json'
content_hash: 'sha256:b06aa23ce1543f9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileWrapperDocumentReader](../filewrapperdocumentreader.md)

# init(_:makeSnapshot:)

<sub>Initializer</sub>

Creates a reader that converts a `FileWrapper` into a snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(_ configuration: sending FileWrapperDocumentReader<Snapshot>.ReadConfiguration, makeSnapshot: @escaping (FileWrapper) async throws -> sending Snapshot)
```

## Parameters

- `configuration` — The read configuration passed to [reader(configuration:)](<../readabledocument/reader(configuration_).md>).

- `makeSnapshot` — A closure that deserializes the `FileWrapper` into a snapshot. For flat files, read `regularFileContents`. For packages, navigate `fileWrappers` to find children. Throw an error if the data is malformed.

## See Also

### Creating a reader

- [ReadConfiguration](readconfiguration.md) _(beta)_
