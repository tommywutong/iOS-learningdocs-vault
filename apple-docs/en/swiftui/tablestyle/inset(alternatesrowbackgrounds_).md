---
title: 'inset(alternatesRowBackgrounds:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 12.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/tablestyle/inset(alternatesrowbackgrounds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle/inset(alternatesrowbackgrounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle/inset%28alternatesrowbackgrounds%3A%29.json'
content_hash: 'sha256:510343a903c91023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableStyle](../tablestyle.md)

# inset(alternatesRowBackgrounds:)

<sub>Type Method</sub>

The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.

> [!warning] Deprecated
> Use the [inset](inset.md) style and add the [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>) view modifier instead.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle
```

## Parameters

- `alternatesRowBackgrounds` — Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## See Also

### Deprecated styles

- [bordered(alternatesRowBackgrounds:)](<bordered(alternatesrowbackgrounds_).md>) — The table style that describes the behavior and appearance of a table with standard border. _(deprecated)_
