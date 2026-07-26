---
title: 'TouchBarItemPresence.default(_:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/touchbaritempresence/default(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/touchbaritempresence/default(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/touchbaritempresence/default%28_%3A%29.json'
content_hash: 'sha256:0c4e830ab108871a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TouchBarItemPresence](../touchbaritempresence.md)

# TouchBarItemPresence.default(_:)

<sub>Case</sub>

The Touch Bar view is visible by default, but can be removed during customization.

<sub>macOS</sub>

```swift
case `default`(String)
```

## Parameters

- `id` — A globally unique identifier for this item.

## See Also

### Getting presence options

- [TouchBarItemPresence.optional(_:)](<optional(__).md>) — The Touch Bar view isn’t visible by default, but appears in the customization palette.
- [TouchBarItemPresence.required(_:)](<required(__).md>) — The Touch Bar view is visible by default and cannot be removed during customization.
