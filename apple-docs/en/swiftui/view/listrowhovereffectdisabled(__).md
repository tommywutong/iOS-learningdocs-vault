---
title: 'listRowHoverEffectDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowhovereffectdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowhovereffectdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowhovereffectdisabled%28_%3A%29.json'
content_hash: 'sha256:8b526bfdf72870e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowHoverEffectDisabled(_:)

<sub>Instance Method</sub>

Requests that the containing list row have its hover effect disabled.

<sub>visionOS</sub>

```swift
nonisolated func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View

```

## Parameters

- `disabled` — A Boolean value that determines whether the containing list row should display its default hover effect.

## Return Value

A view that requests the default hover effect on its containing list row to conditionally be disabled.

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some cases, it is useful to disable the default hover effect.

## See Also

### Configuring interaction

- [swipeActions(edge:allowsFullSwipe:content:)](<swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a row in a list.
- [selectionDisabled(_:)](<selectiondisabled(__).md>) — Adds a condition that controls whether users can select this view.
- [listRowHoverEffect(_:)](<listrowhovereffect(__).md>) — Requests that the containing list row use the provided hover effect.
