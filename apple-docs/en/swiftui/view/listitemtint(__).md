---
title: 'listItemTint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listitemtint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listitemtint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listitemtint%28_%3A%29.json'
content_hash: 'sha256:1b6b2ed3af10bec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listItemTint(_:)

<sub>Instance Method</sub>

Sets a fixed tint color for content in a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func listItemTint(_ tint: Color?) -> some View

```

## Parameters

- `tint` — The color to use to tint the content. Use `nil` to avoid overriding the inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example, watchOS uses the tint color for its background platter appearance. Sidebars on iOS and macOS apply the tint color to their [Label](../label.md) icons, which otherwise use the accent color by default.

> [!note] Note
> This modifier is equivalent to using the version of the modifier that takes a [ListItemTint](../listitemtint.md) value and specifying the `tint` color in the corresponding [fixed(_:)](<../listitemtint/fixed(__).md>) input.

## See Also

### Configuring rows

- [ListItemTint](../listitemtint.md) — A tint effect configuration that you can apply to content in a list.
