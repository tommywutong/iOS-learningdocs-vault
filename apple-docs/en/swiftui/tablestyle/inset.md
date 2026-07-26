---
title: inset
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablestyle/inset
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle/inset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle/inset.json'
content_hash: 'sha256:236205f88cc3cefb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableStyle](../tablestyle.md)

# inset

<sub>Type Property</sub>

The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var inset: InsetTableStyle { get }
```

## Discussion

To customize whether the rows of the table should alternate their backgrounds, use [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>).

## See Also

### Getting built-in table styles

- [automatic](automatic.md) — The default table style in the current context.
- [bordered](bordered.md) — The table style that describes the behavior and appearance of a table with standard border.
