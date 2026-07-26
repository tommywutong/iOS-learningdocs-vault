---
title: 'bordered(alternatesRowBackgrounds:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 12.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/liststyle/bordered(alternatesrowbackgrounds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle/bordered(alternatesrowbackgrounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle/bordered%28alternatesrowbackgrounds%3A%29.json'
content_hash: 'sha256:77b3db7867510a81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListStyle](../liststyle.md)

# bordered(alternatesRowBackgrounds:)

<sub>Type Method</sub>

The list style that describes the behavior and appearance of a list with standard border.

> [!warning] Deprecated
> Use the [bordered](bordered.md) style and add the [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>) view modifier instead.

<sub>macOS</sub>

```swift
@export(implementation) static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle
```

## Parameters

- `alternatesRowBackgrounds` — Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

## See Also

### Deprecated styles

- [inset(alternatesRowBackgrounds:)](<inset(alternatesrowbackgrounds_).md>) — The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds. _(deprecated)_
