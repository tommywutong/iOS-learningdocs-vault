---
title: 'headerProminence(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/headerprominence(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/headerprominence(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/headerprominence%28_%3A%29.json'
content_hash: 'sha256:4a5766b4a8894ef2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# headerProminence(_:)

<sub>Instance Method</sub>

Sets the header prominence for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func headerProminence(_ prominence: Prominence) -> some View

```

## Parameters

- `prominence` — The prominence to apply.

## Discussion

In the following example, the section header appears with increased prominence:

```swift
List {
    Section(header: Text("Header")) {
        Text("Row")
    }
    .headerProminence(.increased)
}
.listStyle(.insetGrouped)
```

## See Also

### Configuring headers

- [headerProminence](../environmentvalues/headerprominence.md) — The prominence to apply to section headers within a view.
- [Prominence](../prominence.md) — A type indicating the prominence of a view hierarchy.
