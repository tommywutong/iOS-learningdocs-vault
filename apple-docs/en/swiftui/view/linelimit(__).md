---
title: 'lineLimit(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/linelimit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/linelimit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/linelimit%28_%3A%29.json'
content_hash: 'sha256:fc83f18753515890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# lineLimit(_:)

<sub>Instance Method</sub>

Sets to a closed range the number of lines that text can occupy in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineLimit(_ limit: ClosedRange<Int>) -> some View

```

## Parameters

- `limit` — The line limit.

## Discussion

Use this modifier to specify a closed range of lines that a [Text](../text.md) view or a vertical [TextField](../textfield.md) can occupy. When the text of such views occupies more space than the provided limit, a [Text](../text.md) view truncates its content while a [TextField](../textfield.md) becomes scrollable.

```swift
Form {
    TextField("Title", text: $model.title)
    TextField("Notes", text: $model.notes, axis: .vertical)
        .lineLimit(1...3)
}
```

## See Also

### Limiting line count for multiline text

- [lineLimit(_:reservesSpace:)](<linelimit(__reservesspace_).md>) — Sets a limit for the number of lines text can occupy in this view.
- [lineLimit](../environmentvalues/linelimit.md) — The maximum number of lines that text can occupy in a view.
