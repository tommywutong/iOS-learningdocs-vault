---
title: 'callAsFunction(contentType:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/newdocumentaction/callasfunction(contenttype:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentaction/callasfunction(contenttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentaction/callasfunction%28contenttype%3A%29.json'
content_hash: 'sha256:935e30f5c2ac65ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentAction](../newdocumentaction.md)

# callAsFunction(contentType:)

<sub>Instance Method</sub>

Presents a new document window.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(contentType: UTType)
```

## Parameters

- `contentType` — The content type of the document.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [newDocument](../environmentvalues/newdocument.md) action:

```swift
newDocument(contentType: .todoList)

 extension UTType {
     static let todoList = UTType(exportedAs: "com.myApp.todoList")
 }
```

> [!important] Important
> If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist` file. For more information, see [Defining file and data types for your app](../../uniformtypeidentifiers/defining-file-and-data-types-for-your-app.md). Also, remember to specify the supported Document types in the `Info.plist` file as well.

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

## See Also

### Calling the action

- [callAsFunction(_:)](<callasfunction(__).md>) — Presents a new document window for the in-memory document returned by the provided closure. _(beta)_
- [callAsFunction(contentType:prepareDocument:)](<callasfunction(contenttype_preparedocument_).md>) — Presents a new document window with preset contents.
