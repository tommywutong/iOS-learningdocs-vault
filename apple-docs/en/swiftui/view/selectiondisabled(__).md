---
title: 'selectionDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/selectiondisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/selectiondisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/selectiondisabled%28_%3A%29.json'
content_hash: 'sha256:2767e36c5810dbeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# selectionDisabled(_:)

<sub>Instance Method</sub>

Adds a condition that controls whether users can select this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func selectionDisabled(_ isDisabled: Bool = true) -> some View

```

## Parameters

- `isDisabled` — A Boolean value that determines whether users can select this view.

## Discussion

Use this modifier to control the selectability of views in selectable containers like [List](../list.md) or [Table](../table.md). In the example, below, the user can’t select the first item in the list.

```swift
@Binding var selection: Item.ID?
@Binding var items: [Item]

var body: some View {
    List(selection: $selection) {
        ForEach(items) { item in
            ItemView(item: item)
                .selectionDisabled(item.id == items.first?.id)
        }
    }
}
```

You can also use this modifier to specify the selectability of views within a `Picker`. The following example represents a flavor picker that disables selection on flavors that are unavailable.

```swift
Picker("Flavor", selection: $selectedFlavor) {
    ForEach(Flavor.allCases) { flavor in
        Text(flavor.rawValue.capitalized)
            .selectionDisabled(isSoldOut(flavor))
    }
}
```

## See Also

### Configuring interaction

- [swipeActions(edge:allowsFullSwipe:content:)](<swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a row in a list.
- [listRowHoverEffect(_:)](<listrowhovereffect(__).md>) — Requests that the containing list row use the provided hover effect.
- [listRowHoverEffectDisabled(_:)](<listrowhovereffectdisabled(__).md>) — Requests that the containing list row have its hover effect disabled.
