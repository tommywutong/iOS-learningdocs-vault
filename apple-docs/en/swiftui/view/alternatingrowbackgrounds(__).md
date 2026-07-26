---
title: 'alternatingRowBackgrounds(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/alternatingrowbackgrounds(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alternatingrowbackgrounds(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alternatingrowbackgrounds%28_%3A%29.json'
content_hash: 'sha256:d865f9116e2d1bfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# alternatingRowBackgrounds(_:)

<sub>Instance Method</sub>

Overrides whether lists and tables in this view have alternating row backgrounds.

<sub>macOS</sub>

```swift
nonisolated func alternatingRowBackgrounds(_ behavior: AlternatingRowBackgroundBehavior = .enabled) -> some View

```

## Parameters

- `behavior` — Whether alternating row backgrounds are enabled or not.

## Discussion

This can be used in conjunction with an explicit list or table style or used by itself to customize the row backgrounds of the automatic style. The only list style this has no effect on is `.sidebar.`

```swift
List(recipe.ingredients) {
    Text($0.name)
}
.listStyle(.bordered)
.alternatingRowBackgrounds()
```

This is able to be combined with `scrollContentBackground(_:)` and applies an alternating row background on top of the overall list or table background.

This can also be combined with `listRowBackground`, which overrides the background for a specific list row, replacing the automatic alternating background for that row.

## See Also

### Configuring backgrounds

- [listRowBackground(_:)](<listrowbackground(__).md>) — Places a custom background view behind a list row item.
- [AlternatingRowBackgroundBehavior](../alternatingrowbackgroundbehavior.md) — The styling of views with respect to alternating row backgrounds.
- [backgroundProminence](../environmentvalues/backgroundprominence.md) — The prominence of the background underneath views associated with this environment.
- [BackgroundProminence](../backgroundprominence.md) — The prominence of backgrounds underneath other views.
