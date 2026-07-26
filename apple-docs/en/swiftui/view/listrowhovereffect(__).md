---
title: 'listRowHoverEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowhovereffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowhovereffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowhovereffect%28_%3A%29.json'
content_hash: 'sha256:1903629b1c84b9e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowHoverEffect(_:)

<sub>Instance Method</sub>

Requests that the containing list row use the provided hover effect.

<sub>visionOS</sub>

```swift
nonisolated func listRowHoverEffect(_ effect: HoverEffect?) -> some View

```

## Parameters

- `effect` — The hover effect applied to the entire list row.

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list row’s default effect be replaced by the provided effect. If the view is not contained within a `List` or if the view does not support hover effects in this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should not be modified.

[lift](../hovereffect/lift.md) is not supported for list rows.

## See Also

### Configuring interaction

- [swipeActions(edge:allowsFullSwipe:content:)](<swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a row in a list.
- [selectionDisabled(_:)](<selectiondisabled(__).md>) — Adds a condition that controls whether users can select this view.
- [listRowHoverEffectDisabled(_:)](<listrowhovereffectdisabled(__).md>) — Requests that the containing list row have its hover effect disabled.
