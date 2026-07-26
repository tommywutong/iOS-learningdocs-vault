---
title: 'exportableToServices(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/exportabletoservices(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/exportabletoservices(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/exportabletoservices%28_%3A%29.json'
content_hash: 'sha256:3c13951a7e73ad73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# exportableToServices(_:)

<sub>Instance Method</sub>

Exports items for consumption by shortcuts, quick actions, and services.

<sub>macOS</sub>

```swift
nonisolated func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable

```

## Parameters

- `payload` — A closure that will be called on request of the items by the shortcut or service.

## Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

```swift
var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .exportableToServices([title])
}
```

## See Also

### Importing and exporting transferable items

- [importableFromServices(for:action:)](<importablefromservices(for_action_).md>) — Enables importing items from services, such as Continuity Camera on macOS.
- [exportableToServices(_:onEdit:)](<exportabletoservices(__onedit_).md>) — Exports read-write items for consumption by shortcuts, quick actions, and services.
