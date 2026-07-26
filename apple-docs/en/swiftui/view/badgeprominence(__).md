---
title: 'badgeProminence(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/badgeprominence(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/badgeprominence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/badgeprominence%28_%3A%29.json'
content_hash: 'sha256:b0f48b7a18abc927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# badgeProminence(_:)

<sub>Instance Method</sub>

Specifies the prominence of badges created by this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func badgeProminence(_ prominence: BadgeProminence) -> some View

```

## Parameters

- `prominence` — The prominence to apply to badges.

## Discussion

Badges can be used for different kinds of information, from the passive number of items in a container to the number of required actions. The prominence of badges in Lists can be adjusted to reflect this and be made to draw more or less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a [List](../list.md) displaying a list of folders with an informational badge with lower prominence, showing the number of items in the folder.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## See Also

### Displaying a badge on a list item

- [badge(_:)](<badge(__).md>) — Generates a badge for the view from a localized string resource.
- [badgeProminence](../environmentvalues/badgeprominence.md) — The prominence to apply to badges associated with this environment.
- [BadgeProminence](../badgeprominence.md) — The visual prominence of a badge.
