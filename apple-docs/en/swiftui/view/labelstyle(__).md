---
title: 'labelStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/labelstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/labelstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/labelstyle%28_%3A%29.json'
content_hash: 'sha256:3ec46bfa4e0caaa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# labelStyle(_:)

<sub>Instance Method</sub>

Sets the style for labels within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func labelStyle<S>(_ style: S) -> some View where S : LabelStyle

```

## Discussion

Use this modifier to set a specific style for all labels within a view:

```swift
VStack {
    Label("Fire", systemImage: "flame.fill")
    Label("Lightning", systemImage: "bolt.fill")
}
.labelStyle(MyCustomLabelStyle())
```

## See Also

### Displaying text

- [Text](../text.md) — A view that displays one or more lines of read-only text.
- [Label](../label.md) — A standard label for user interface items, consisting of an icon with a title.
