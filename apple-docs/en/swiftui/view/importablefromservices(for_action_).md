---
title: 'importableFromServices(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/importablefromservices(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/importablefromservices(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/importablefromservices%28for%3Aaction%3A%29.json'
content_hash: 'sha256:fc79493e58e2f393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# importableFromServices(for:action:)

<sub>Instance Method</sub>

Enables importing items from services, such as Continuity Camera on macOS.

<sub>macOS</sub>

```swift
nonisolated func importableFromServices<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Bool) -> some View where T : Transferable

```

## Parameters

- `payloadType` — The expected type of the imported models.

- `action` — A closure that will be called with the imported service item. Return `false` to indicate that there was a failure to receive the items.

## Discussion

```swift
@State private var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .importableFromServices(for: String.self) { titles
            title = titles.first ?? title
            return !titles.isEmpty
        }
}
```

## See Also

### Importing and exporting transferable items

- [exportableToServices(_:)](<exportabletoservices(__).md>) — Exports items for consumption by shortcuts, quick actions, and services.
- [exportableToServices(_:onEdit:)](<exportabletoservices(__onedit_).md>) — Exports read-write items for consumption by shortcuts, quick actions, and services.
