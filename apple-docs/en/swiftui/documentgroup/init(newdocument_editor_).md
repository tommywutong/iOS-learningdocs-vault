---
title: 'init(newDocument:editor:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/documentgroup/init(newdocument:editor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(newdocument:editor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28newdocument%3Aeditor%3A%29.json'
content_hash: 'sha256:6e01e587ca94d725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(newDocument:editor:)

<sub>Initializer</sub>

Creates a document group for creating and editing file documents.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@preconcurrency nonisolated init(newDocument: @autoclosure @escaping @Sendable () -> Document, @ContentBuilder editor: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

## Parameters

- `newDocument` — The initial document to use when a user creates a new document.

- `editor` — The editing UI for the provided document.

## Discussion

Use a [DocumentGroup](../documentgroup.md) scene to tell SwiftUI what kinds of documents your app can open when you declare your app using the [App](../app.md) protocol. You initialize a document group scene by passing in the document model and a view capable of displaying the document’s contents. The document types you supply to [DocumentGroup](../documentgroup.md) must conform to [FileDocument](../filedocument.md) or [ReferenceFileDocument](../referencefiledocument.md). SwiftUI uses the model to add document support to your app. In macOS this includes document-based menu support including the ability to open multiple documents. On iOS this includes a document browser that can navigate to the documents stored on the file system and multiwindow support:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { file in
            ContentView(document: file.$document)
        }
    }
}
```

The document types you supply to [DocumentGroup](../documentgroup.md) must conform to [FileDocument](../filedocument.md) or [ReferenceFileDocument](../referencefiledocument.md). Your app can support multiple document types by adding additional [DocumentGroup](../documentgroup.md) scenes.

With the `newDocument:` initializer, SwiftUI considers your app as an editor of documents of given content types (`FileDocument.writableContentTypes`). On macOS, this adds a File \> New menu item and enables the standard document commands.

On iOS, it shows a New Document button in the document browser. The [isEditable](../filedocumentconfiguration/iseditable.md) property is `true`. Use the `DocumentGroup/init(viewing:editor:)` initializer instead if your app should only display documents without modifying them.

## See Also

### Deprecated

- [init(viewing:viewer:)](<init(viewing_viewer_).md>) — Creates a document group capable of viewing file documents. _(deprecated)_
