---
title: 'callAsFunction(at:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/opendocumentaction/callasfunction(at:)'
source_url: 'https://developer.apple.com/documentation/swiftui/opendocumentaction/callasfunction(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/opendocumentaction/callasfunction%28at%3A%29.json'
content_hash: 'sha256:0a4c764c3b6fe210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenDocumentAction](../opendocumentaction.md)

# callAsFunction(at:)

<sub>Instance Method</sub>

Opens the document at the specified file URL.

<sub>macOS</sub>

```swift
@MainActor func callAsFunction(at url: URL) async throws
```

## Parameters

- `url` — A file URL that points at an existing document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [openDocument](../environmentvalues/opendocument.md) action:

```swift
do {
    try await openDocument(at: url)
} catch {
    // Handle error
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
