---
title: 'init(nsUnderlineStyle:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/linestyle/init(nsunderlinestyle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/linestyle/init(nsunderlinestyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/linestyle/init%28nsunderlinestyle%3A%29.json'
content_hash: 'sha256:34e0eb6ddbfe7256'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [LineStyle](../linestyle.md)

# init(nsUnderlineStyle:)

<sub>Initializer</sub>

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(nsUnderlineStyle: NSUnderlineStyle)
```

## Parameters

- `nsUnderlineStyle` — A value of `NSUnderlineStyle` to wrap with `Text.LineStyle`.

## Return Value

A new `Text.LineStyle` or `nil` when `nsUnderlineStyle` contains styles not supported by `Text.LineStyle`.

## Discussion

> [!note] Note
> Use this initializer only if you need to convert an existing `NSUnderlineStyle` to a SwiftUI `Text.LineStyle`. Otherwise, create a `Text.LineStyle` using an initializer like [init(pattern:color:)](<init(pattern_color_).md>).

## See Also

### Creating a text line style

- [init(pattern:color:)](<init(pattern_color_).md>) — Creates a line style.
- [Pattern](pattern.md) — The pattern, that the line has.
