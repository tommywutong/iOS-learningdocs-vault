---
title: 'importsItemProviders(_:onImport:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/importsitemproviders(_:onimport:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/importsitemproviders(_:onimport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/importsitemproviders%28_%3Aonimport%3A%29.json'
content_hash: 'sha256:39761812632a824d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# importsItemProviders(_:onImport:)

<sub>Instance Method</sub>

Enables importing item providers from services, such as Continuity Camera on macOS.

<sub>macOS</sub>

```swift
nonisolated func importsItemProviders(_ contentTypes: [UTType], onImport: @escaping ([NSItemProvider]) -> Bool) -> some View

```

## Parameters

- `contentTypes` — The types of content that the view supports importing. An empty array means the view does not currently support importing.

- `onImport` — A closure that will be called with the imported service item. Return `false` to indicate that there was a failure to receive the items.

## See Also

### Importing and exporting using item providers

- [exportsItemProviders(_:onExport:)](<exportsitemproviders(__onexport_).md>) — Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [exportsItemProviders(_:onExport:onEdit:)](<exportsitemproviders(__onexport_onedit_).md>) — Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
