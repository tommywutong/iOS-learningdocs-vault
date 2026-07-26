---
title: 'init(viewing:contentType:viewer:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentgroup/init(viewing:contenttype:viewer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:contenttype:viewer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28viewing%3Acontenttype%3Aviewer%3A%29.json'
content_hash: 'sha256:8abda8b9fd02cba4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(viewing:contentType:viewer:)

<sub>Initializer</sub>

Instantiates a document group for viewing documents that store a specific model type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(viewing modelType: any PersistentModel.Type, contentType: UTType, viewer: @escaping () -> Content)
```

## Parameters

- `modelType` — The model type defining the schema used for each document.

- `contentType` — The content type of document your app can view. It should conform to `UTType.package`.

- `viewer` — The viewing UI for the provided document.

## Discussion

```swift
 @main
 struct Todo: App {
     var body: some Scene {
         DocumentGroup(viewing: TodoItem.self, contentType: .todoItem) {
             ContentView()
         }
     }
 }

 extension UTType {
     static var todoItem = UTType(exportedAs: "com.myApp.todoItem")
 }
```

> [!important] Important
> If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [Defining file and data types for your app](../../uniformtypeidentifiers/defining-file-and-data-types-for-your-app.md). Also, remember to specify the supported Document types in the `Info.plist` as well.

## See Also

### Viewing a document backed by a persistent store

- [init(viewing:migrationPlan:viewer:)](<init(viewing_migrationplan_viewer_).md>) — Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.
