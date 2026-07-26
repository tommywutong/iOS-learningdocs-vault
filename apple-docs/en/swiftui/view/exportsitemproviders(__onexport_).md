---
title: 'exportsItemProviders(_:onExport:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/exportsitemproviders(_:onexport:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/exportsitemproviders(_:onexport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/exportsitemproviders%28_%3Aonexport%3A%29.json'
content_hash: 'sha256:98f90ec713cc2a1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# exportsItemProviders(_:onExport:)

<sub>Instance Method</sub>

Exports a read-only item provider for consumption by shortcuts, quick actions, and services.

<sub>macOS</sub>

```swift
nonisolated func exportsItemProviders(_ contentTypes: [UTType], onExport: @escaping () -> [NSItemProvider]) -> some View

```

## Parameters

- `contentTypes` — The types of content that the view supports exporting. An empty array means the view does not currently support exporting.

- `onExport` — A closure that will be called on request of the items by the shortcut or service.

## Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

## See Also

### Importing and exporting using item providers

- [importsItemProviders(_:onImport:)](<importsitemproviders(__onimport_).md>) — Enables importing item providers from services, such as Continuity Camera on macOS.
- [exportsItemProviders(_:onExport:onEdit:)](<exportsitemproviders(__onexport_onedit_).md>) — Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
