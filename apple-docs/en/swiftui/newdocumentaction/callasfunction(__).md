---
title: 'callAsFunction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/newdocumentaction/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentaction/callasfunction%28_%3A%29.json'
content_hash: 'sha256:1c12b946ddb7a256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentAction](../newdocumentaction.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Presents a new document window for the in-memory document returned by the provided closure.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction<D>(_ newDocument: @autoclosure @escaping @Sendable () -> sending D) where D : ReadableDocument
```

## Parameters

- `newDocument` — A closure that produces the in-memory document to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [newDocument](../environmentvalues/newdocument.md) action with a [ReadableDocument](../readabledocument.md) factory.

The factory closure runs when SwiftUI needs the document instance. SwiftUI then injects the instance into the matching [DocumentGroup](../documentgroup.md) and presents its window. The matching document group is the first creatable group whose readable content types overlap with `D.readableContentTypes`.

## See Also

### Calling the action

- [callAsFunction(contentType:)](<callasfunction(contenttype_).md>) — Presents a new document window.
- [callAsFunction(contentType:prepareDocument:)](<callasfunction(contenttype_preparedocument_).md>) — Presents a new document window with preset contents.
