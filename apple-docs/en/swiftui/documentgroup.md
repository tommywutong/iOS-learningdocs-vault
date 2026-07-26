---
title: DocumentGroup
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentgroup
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup.json'
content_hash: 'sha256:ff090c6af61a364b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentGroup

<sub>Structure</sub>

A scene that enables support for opening, creating, and saving documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct DocumentGroup<Document, Content> where Content : View
```

## Overview

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app can open when you declare your app using the [App](app.md) protocol.

Initialize a document group scene by passing in the document model and a view capable of displaying the document type. The document types you supply to `DocumentGroup` must conform to [FileDocument](filedocument.md) or [ReferenceFileDocument](referencefiledocument.md). SwiftUI uses the model to add document support to your app. In macOS this includes document-based menu support, including the ability to open multiple documents. On iOS this includes a document browser that can navigate to the documents stored on the file system and multiwindow support:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(document: configuration.$document)
        }
    }
}
```

Any time the configuration changes, SwiftUI updates the contents with that new configuration, similar to other parameterized builders.

### Viewing documents

If your app only needs to display but not modify a specific document type, you can use the file viewer document group scene. You supply the file type of the document, and a view that displays the document type that you provide:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(viewing: MyImageFormatDocument.self) {
            MyImageFormatViewer(image: $0.document)
        }
    }
}
```

### Supporting multiple document types

Your app can support multiple document types by adding additional document group scenes:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { group in
            ContentView(document: group.$document)
        }
        DocumentGroup(viewing: MyImageFormatDocument.self) { group in
            MyImageFormatViewer(image: group.document)
        }
    }
}
```

### Opening documents

When a person opens a file — for example, by double-clicking it in macOS Finder or tapping it in the iOS Files app — the system looks through the list of registered Uniform Type Identifiers (or _content types_) to find one that corresponds to the file extension.

The operating system learns about new content types from information property list files of installed apps. Your app’s information property list can include several keys depending on your needs:

- The _Document Types_ key (`CFBundleDocumentTypes`) lists the content type identifiers your app can open. Every document-based app must include this key.
- The _Exported Type Identifiers_ key (`UTExportedTypeDeclarations`) declares a custom content type that your app defines. Include a file extension so the system knows which files correspond to that type.
- The _Imported Type Identifiers_ key (`UTImportedTypeDeclarations`) registers a content type that another app defines. If the person doesn’t have that app installed, your declaration is what the system uses to identify the type and its associated files. If they do have it installed, the app’s exported declaration takes precedence instead.

  For example, if your app works with `xcresult` bundles, declare `com.apple.xcode.resultbundle` as an imported type. If someone doesn’t have Xcode installed, your declaration tells the system that `.xcresult` files belong to this type. Once they install Xcode, its exported declaration takes over.

  You don’t need to declare content types the operating system defines, like `UTType.utf8PlainText`.

You can configure these property list keys in the Info pane of your app target in Xcode. Document types that correspond to regular files on disk must conform to `UTType/data`; packages must conform to `UTType/package`.

For more information on how the `UTType` system works, including its hierarchical structure and when to export versus import a type, refer to [A Reintroduction to Uniform Type Identifiers](https://developer.apple.com/videos/play/tech-talks/10696/).

When multiple apps can open the same file type, the system also considers the _Handler Rank_ you set in the Document Types key, which indicates whether your app is the default handler or an alternative.

For example, to declare a custom plain-text format, extend `UTType` with your app’s reverse-DNS identifier and declare its conformance and associated file extension in your app’s information property list:

```swift
extension UTType {
    static let customTextFormat = UTType(
        exportedAs: "com.myApp.customTextFormat")
}

struct MyDocument: FileDocument {
    static let readableContentTypes = [UTType.customTextFormat]
    // ...
}
```

SwiftUI then checks each `DocumentGroup` in your scene body from top to bottom and uses the first one whose document’s `readableContentTypes` static array property includes a `UTType` the file conforms to. Content types form a hierarchy — for example, HTML is a kind of plain text, so a document group that declares `UTType/plainText` also matches HTML files.

If multiple document groups can match the same file, SwiftUI uses the first one declared. Declare more specific types before broader ones to match each file to the correct document group:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        // Checked first; matches only this custom format.
        DocumentGroup(newDocument: MyDocument()) { configuration in
            MyDocumentView(document: configuration.$document)
        }
        // Checked second; matches any remaining plain-text files.
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(document: configuration.$document)
        }
    }
}
```

### Document life cycle

Once SwiftUI selects the matching `DocumentGroup`, it loads the file’s contents into the document type and presents the view with the loaded document.

For a value-type document, like a `struct`, SwiftUI tracks edits through the document binding. For a reference-type document, like a `class`, it tracks changes you register with `EnvironmentValues.undoManager`. SwiftUI writes the document back to disk when needed — for example, in response to a Save command.

### Accessing the document’s URL

If your app needs to know the document’s URL, you can read it from the `editor` closure’s `configuration` parameter, along with the binding to the document. When you create a new document, the configuration’s `fileURL` property is `nil`. Every time it changes, it is passed over to the `DocumentGroup` builder in the updated `configuration`. This ensures that the view you define in the closure always knows the URL of the document it hosts.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(
                document: configuration.$document,
                fileURL: configuration.fileURL
            )
        }
    }
}
```

The URL can be used, for example, to present the file path of the file name in the user interface. Don’t access the document’s contents or metadata using the URL because that can conflict with the management of the file that SwiftUI performs. Instead, use the methods that [FileDocument](filedocument.md) and [ReferenceFileDocument](referencefiledocument.md) provide to perform read and write operations.

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Creating a document group

- [init(allowCreating:editor:makeDocument:)](<documentgroup/init(allowcreating_editor_makedocument_).md>) — Creates a document group capable of creating, viewing, and editing documents. _(beta)_
- [init(viewer:makeReadableDocument:)](<documentgroup/init(viewer_makereadabledocument_).md>) — Creates a document group capable of opening and viewing read-only documents. _(beta)_

### Editing a document backed by a persistent store

- [init(editing:contentType:editor:prepareDocument:)](<documentgroup/init(editing_contenttype_editor_preparedocument_).md>) — Instantiates a document group for creating and editing documents that store a specific model type.
- [init(editing:migrationPlan:editor:prepareDocument:)](<documentgroup/init(editing_migrationplan_editor_preparedocument_).md>) — Instantiates a document group for creating and editing documents described by the last `Schema` in the migration plan.

### Viewing a document backed by a persistent store

- [init(viewing:contentType:viewer:)](<documentgroup/init(viewing_contenttype_viewer_).md>) — Instantiates a document group for viewing documents that store a specific model type.
- [init(viewing:migrationPlan:viewer:)](<documentgroup/init(viewing_migrationplan_viewer_).md>) — Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.

### Deprecated

- [init(newDocument:editor:)](<documentgroup/init(newdocument_editor_).md>) — Creates a document group for creating and editing file documents. _(deprecated)_
- [init(viewing:viewer:)](<documentgroup/init(viewing_viewer_).md>) — Creates a document group capable of viewing file documents. _(deprecated)_

## See Also

### Creating a document

- [Creating a document-based app](creating-a-document-based-app.md) — Build apps that people can use to open, edit, and save files using coordinated file access.
- [Handling advanced document scenarios](handling-advanced-document-scenarios.md) — Extend your document-based app to support custom file formats, on-demand file access, and progress reporting.
- [Updating your document-based app](updating-your-document-based-app.md) — Migrate an existing app to adopt URL-based document reading and writing with Swift concurrency.
- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md) — Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
