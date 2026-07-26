---
title: 'init(viewing:viewer:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/documentgroup/init(viewing:viewer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:viewer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28viewing%3Aviewer%3A%29.json'
content_hash: 'sha256:9e185df32b775bfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(viewing:viewer:)

<sub>Initializer</sub>

Creates a document group capable of viewing file documents.

> [!warning] Deprecated
> Conform your type to ReadableDocument instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(viewing documentType: Document.Type, @ContentBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

## Parameters

- `documentType` — The type of document your app can view.

- `viewer` — The viewing UI for the provided document.

## Discussion

Use this method to create a document group that can view files of a specific type. The example below creates a new document viewer for `MyImageFormatDocument` and displays them with `MyImageFormatViewer`:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(viewing: MyImageFormatDocument.self) { file in
            MyImageFormatViewer(image: file.document)
        }
    }
}
```

With the `viewing:` initializer, SwiftUI considers your app as a viewer for given content types (readable content types declared on the document type). No File \> New menu item is added on macOS, no New Document button appears in the iOS document browser, and the [isEditable](../filedocumentconfiguration/iseditable.md) property is `false`, preventing accidental writes. Use the [init(newDocument:editor:)](<init(newdocument_editor_).md>) initializer instead if your app needs to create or edit documents.

You tell the system about the app’s role with respect to the document type by setting the [CFBundleTypeRole](../../bundleresources/information-property-list/cfbundledocumenttypes/cfbundletyperole.md) `Info.plist` key with a value of `Viewer`.

## See Also

### Deprecated

- [init(newDocument:editor:)](<init(newdocument_editor_).md>) — Creates a document group for creating and editing file documents. _(deprecated)_
