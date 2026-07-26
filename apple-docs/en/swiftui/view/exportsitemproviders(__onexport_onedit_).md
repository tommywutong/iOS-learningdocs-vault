---
title: 'exportsItemProviders(_:onExport:onEdit:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/exportsitemproviders(_:onexport:onedit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/exportsitemproviders(_:onexport:onedit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/exportsitemproviders%28_%3Aonexport%3Aonedit%3A%29.json'
content_hash: 'sha256:6e9d8d5eaac3ff26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# exportsItemProviders(_:onExport:onEdit:)

<sub>Instance Method</sub>

Exports a read-write item provider for consumption by shortcuts, quick actions, and services.

<sub>macOS</sub>

```swift
nonisolated func exportsItemProviders(_ contentTypes: [UTType], onExport: @escaping () -> [NSItemProvider], onEdit: @escaping ([NSItemProvider]) -> Bool) -> some View

```

## Parameters

- `contentTypes` — The types of content that the view supports exporting and importing. An empty array means the view does not currently support exporting.

- `onExport` — A closure that will be called on request of the items by the shortcut or service.

- `onEdit` — A closure that will be called after the shortcut or service completes with its output data. This should replace the selected subpart that was exported with `onExport`. Return `false` to indicate that there was a failure to receive the items.

## Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

## See Also

### Importing and exporting using item providers

- [importsItemProviders(_:onImport:)](<importsitemproviders(__onimport_).md>) — Enables importing item providers from services, such as Continuity Camera on macOS.
- [exportsItemProviders(_:onExport:)](<exportsitemproviders(__onexport_).md>) — Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
