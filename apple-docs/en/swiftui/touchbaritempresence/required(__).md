---
title: 'TouchBarItemPresence.required(_:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/touchbaritempresence/required(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/touchbaritempresence/required(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/touchbaritempresence/required%28_%3A%29.json'
content_hash: 'sha256:c4dd4566ab821c42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TouchBarItemPresence](../touchbaritempresence.md)

# TouchBarItemPresence.required(_:)

<sub>Case</sub>

The Touch Bar view is visible by default and cannot be removed during customization.

<sub>macOS</sub>

```swift
case required(String)
```

## Parameters

- `id` — A globally unique identifier for this item.

## See Also

### Getting presence options

- [TouchBarItemPresence.default(_:)](<default(__).md>) — The Touch Bar view is visible by default, but can be removed during customization.
- [TouchBarItemPresence.optional(_:)](<optional(__).md>) — The Touch Bar view isn’t visible by default, but appears in the customization palette.
