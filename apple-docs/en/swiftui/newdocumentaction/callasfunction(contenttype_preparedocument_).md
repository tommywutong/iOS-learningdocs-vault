---
title: 'callAsFunction(contentType:prepareDocument:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/newdocumentaction/callasfunction(contenttype:preparedocument:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(contenttype:preparedocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentaction/callasfunction%28contenttype%3Apreparedocument%3A%29.json'
content_hash: 'sha256:52bf34b44097a970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentAction](../newdocumentaction.md)

# callAsFunction(contentType:prepareDocument:)

<sub>Instance Method</sub>

Presents a new document window with preset contents.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(contentType: UTType, prepareDocument: @escaping (ModelContext) -> Void)
```

## Parameters

- `contentType` — The content type of the document.

- `prepareDocument` — The closure that accepts `ModelContext` associated with the new document. Use this closure to set the document’s initial contents before it is displayed: insert preconfigured models in the provided `ModelContext`.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [newDocument](../environmentvalues/newdocument.md) action.

For example, a Todo app might have a way to create a sample prepopulated Todo list as a part of onboarding experience:

```swift
newDocument(contentType: .todoList) { modelContext in
    let todoList = TodoList(
        title: "🎬 Movie night",
        items: [
            TodoItem(title: "🍿 Buy popcorn"),
            TodoItem(title: "🍨 Make some ice cream",
            TodoItem(title: "💡 Hang a string of lights")
        ]
    )
    modelContext.insert(todoList)
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(_:)](<callasfunction(__).md>) — Presents a new document window for the in-memory document returned by the provided closure. _(beta)_
- [callAsFunction(contentType:)](<callasfunction(contenttype_).md>) — Presents a new document window.
