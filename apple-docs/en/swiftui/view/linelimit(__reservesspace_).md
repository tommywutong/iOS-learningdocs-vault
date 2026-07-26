---
title: 'lineLimit(_:reservesSpace:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/linelimit(_:reservesspace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/linelimit(_:reservesspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/linelimit%28_%3Areservesspace%3A%29.json'
content_hash: 'sha256:c801fd9b2965449f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# lineLimit(_:reservesSpace:)

<sub>Instance Method</sub>

Sets a limit for the number of lines text can occupy in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineLimit(_ limit: Int, reservesSpace: Bool) -> some View

```

## Parameters

- `limit` — The line limit.

- `reservesSpace` — Whether text reserves space so that it always occupies the height required to display the specified number of lines.

## Discussion

Use this modifier to specify a limit to the lines that a [Text](../text.md) or a vertical [TextField](../textfield.md) may occupy. If passed a value of true for the `reservesSpace` parameter, and the text of such views occupies less space than the provided limit, that view expands to occupy the minimum number of lines. When the text occupies more space than the provided limit, a [Text](../text.md) view truncates its content while a [TextField](../textfield.md) becomes scrollable.

```swift
GroupBox {
    Text("Title")
        .font(.headline)
        .lineLimit(2, reservesSpace: true)
    Text("Subtitle")
        .font(.subheadline)
        .lineLimit(4, reservesSpace: true)
}
```

## See Also

### Limiting line count for multiline text

- [lineLimit(_:)](<linelimit(__).md>) — Sets to a closed range the number of lines that text can occupy in this view.
- [lineLimit](../environmentvalues/linelimit.md) — The maximum number of lines that text can occupy in a view.
