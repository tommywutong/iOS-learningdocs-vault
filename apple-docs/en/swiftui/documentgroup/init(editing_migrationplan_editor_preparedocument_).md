---
title: 'init(editing:migrationPlan:editor:prepareDocument:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentgroup/init(editing:migrationplan:editor:preparedocument:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(editing:migrationplan:editor:preparedocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28editing%3Amigrationplan%3Aeditor%3Apreparedocument%3A%29.json'
content_hash: 'sha256:ca386fb68936e82e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(editing:migrationPlan:editor:prepareDocument:)

<sub>Initializer</sub>

Instantiates a document group for creating and editing documents described by the last `Schema` in the migration plan.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(editing contentType: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: @escaping () -> Content, prepareDocument: @escaping (ModelContext) -> Void = { _ in })
```

## Parameters

- `editing` — The content type of the document. It should conform to `UTType.package`.

- `migrationPlan` — The description of steps required to migrate older document versions so that they can be opened and edited. The last `VersionedSchema` in the plan is considered to be the current application schema.

- `editor` — The editing UI for the provided document.

## See Also

### Editing a document backed by a persistent store

- [init(editing:contentType:editor:prepareDocument:)](<init(editing_contenttype_editor_preparedocument_).md>) — Instantiates a document group for creating and editing documents that store a specific model type.
