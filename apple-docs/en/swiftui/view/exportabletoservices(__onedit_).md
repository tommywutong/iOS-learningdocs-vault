---
title: 'exportableToServices(_:onEdit:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/exportabletoservices(_:onedit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/exportabletoservices(_:onedit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/exportabletoservices%28_%3Aonedit%3A%29.json'
content_hash: 'sha256:1076f232752a8ea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# exportableToServices(_:onEdit:)

<sub>Instance Method</sub>

Exports read-write items for consumption by shortcuts, quick actions, and services.

<sub>macOS</sub>

```swift
nonisolated func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T], onEdit: @escaping ([T]) -> Bool) -> some View where T : Transferable

```

## Parameters

- `payload` — A closure that will be called on request of the items by the shortcut or service.

- `onEdit` — A closure that will be called after the shortcut or service completes with its output data. This should replace the selected subpart that was exported with `onExport`. Return `false` to indicate that there was a failure to receive the items.

## Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

```swift
@State private var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .exportableToServices([title]) { editedTitles
            title = editedTitles.first ?? title
            return !editedTitles.isEmpty
        }
}
```

## See Also

### Importing and exporting transferable items

- [importableFromServices(for:action:)](<importablefromservices(for_action_).md>) — Enables importing items from services, such as Continuity Camera on macOS.
- [exportableToServices(_:)](<exportabletoservices(__).md>) — Exports items for consumption by shortcuts, quick actions, and services.
