---
title: 'badge(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/badge(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/badge(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/badge%28_%3A%29.json'
content_hash: 'sha256:5480d49d92fd5e2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# badge(_:)

<sub>Instance Method</sub>

Generates a badge for the view from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func badge(_ resource: LocalizedStringResource?) -> some View

```

## Parameters

- `resource` — An optional string resource to display as a badge. Set the value to `nil` to hide the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a [Text](../text.md) view on your behalf. For more information about localizing strings, see [Text](../text.md). The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.isDefault ? "Default" : nil)
    }
    .navigationTitle("Servers")
}
```

![A table with the navigation title Servers and four rows: North 1,](../../../../attachments/b5f34f4ffdb5ba98e88b91513e2da519/View-badge-3@2x.png)

## See Also

### Displaying a badge on a list item

- [badgeProminence(_:)](<badgeprominence(__).md>) — Specifies the prominence of badges created by this view.
- [badgeProminence](../environmentvalues/badgeprominence.md) — The prominence to apply to badges associated with this environment.
- [BadgeProminence](../badgeprominence.md) — The visual prominence of a badge.
