---
title: 'font(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/font(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/font(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/font%28_%3A%29.json'
content_hash: 'sha256:b3b1633de4c21133'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# font(_:)

<sub>Instance Method</sub>

Sets the default font for text in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func font(_ font: Font?) -> Text
```

## Parameters

- `font` — The font to use when displaying this text.

## Return Value

Text that uses the font you specify.

## Discussion

Use `font(_:)` to apply a specific font to an individual Text View, or all of the text views in a container.

In the example below, the first text field has a font set directly, while the font applied to the following container applies to all of the text views inside that container:

```swift
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These two text views have the same font")
        Text("applied to their parent view.")
    }
    .font(.system(size: 16, weight: .light, design: .default))
}
```

![Applying a font to a single text view or a view container](../../../../attachments/96bbeed6b182bf19c533efcca8a5fcaa/SwiftUI-view-font@2x.png)

## See Also

### Choosing a font

- [fontWeight(_:)](<fontweight(__).md>) — Sets the font weight of the text.
- [fontDesign(_:)](<fontdesign(__).md>) — Sets the font design of the text.
- [fontWidth(_:)](<fontwidth(__).md>) — Sets the font width of the text.
