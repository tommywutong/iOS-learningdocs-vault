---
title: 'init(pattern:color:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/linestyle/init(pattern:color:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/linestyle/init(pattern:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/linestyle/init%28pattern%3Acolor%3A%29.json'
content_hash: 'sha256:e9c2b234cb396874'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [LineStyle](../linestyle.md)

# init(pattern:color:)

<sub>Initializer</sub>

Creates a line style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil)
```

## Parameters

- `pattern` — The pattern of the line.

- `color` — The color of the line. If not provided, the foreground color of text is used.

## See Also

### Creating a text line style

- [init(nsUnderlineStyle:)](<init(nsunderlinestyle_).md>) — Creates a `Text.LineStyle` from `NSUnderlineStyle`.
- [Pattern](pattern.md) — The pattern, that the line has.
