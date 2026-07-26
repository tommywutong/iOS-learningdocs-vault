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
doc_path: '/documentation/swiftui/liststyle/inset(alternatesrowbackgrounds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle/inset(alternatesrowbackgrounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle/inset%28alternatesrowbackgrounds%3A%29.json'
content_hash: 'sha256:e058147acfb373e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListStyle](../liststyle.md)

# inset(alternatesRowBackgrounds:)

<sub>Type Method</sub>

The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.

> [!warning] Deprecated
> Use the [inset](inset.md) style and add the [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>) view modifier instead.

<sub>macOS</sub>

```swift
@export(implementation) static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle
```

## Parameters

- `alternatesRowBackgrounds` — Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## See Also

### Deprecated styles

- [bordered(alternatesRowBackgrounds:)](<bordered(alternatesrowbackgrounds_).md>) — The list style that describes the behavior and appearance of a list with standard border. _(deprecated)_
