---
title: makeFileCoordinator()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/urldocumentconfiguration/makefilecoordinator()
source_url: 'https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/makefilecoordinator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/urldocumentconfiguration/makefilecoordinator%28%29.json'
content_hash: 'sha256:78bcd726a87db4e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [URLDocumentConfiguration](../urldocumentconfiguration.md)

# makeFileCoordinator()

<sub>Instance Method</sub>

Creates a file coordinator for coordinated disk access outside the normal read/write flow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor final func makeFileCoordinator() -> sending NSFileCoordinator
```

## Discussion

Call this every time to get a new coordinator for each separate read or write operation. SwiftUI coordinates file access for [read(from:progress:)](<../documentreader/read(from_progress_).md>) and [write(snapshot:to:previous:progress:)](<../documentwriter/write(snapshot_to_previous_progress_).md>) automatically. Use this method when you need to access the document’s file at other times — for example, to read a single sub-file of a package on demand.

Do not reuse coordinators across operations since `NSFileCoordinator` does not conform to `Sendable`.
