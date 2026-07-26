---
title: 'init(viewing:migrationPlan:viewer:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/documentgroup/init(viewing:migrationplan:viewer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:migrationplan:viewer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28viewing%3Amigrationplan%3Aviewer%3A%29.json'
content_hash: 'sha256:e63041263f85f369'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(viewing:migrationPlan:viewer:)

<sub>Initializer</sub>

Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(viewing contentType: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: @escaping () -> Content)
```

## Parameters

- `viewing` — The content type of the document. It should conform to `UTType.package`.

- `migrationPlan` — The description of steps required to migrate older document versions so that they can be opened. The last `VersionedSchema` in the plan is considered to be the current application schema.

- `viewer` — The viewing UI for the provided document.

## See Also

### Viewing a document backed by a persistent store

- [init(viewing:contentType:viewer:)](<init(viewing_contenttype_viewer_).md>) — Instantiates a document group for viewing documents that store a specific model type.
