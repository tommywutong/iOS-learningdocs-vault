---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchsuggestionsplacement/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/searchsuggestionsplacement/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchsuggestionsplacement/automatic.json'
content_hash: 'sha256:532ccf765da30d51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchSuggestionsPlacement](../searchsuggestionsplacement.md)

# automatic

<sub>Type Property</sub>

Search suggestions render automatically based on the surrounding context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: SearchSuggestionsPlacement { get }
```

## Discussion

The behavior varies by platform:

- In iOS and iPadOS, suggestions render as a list overlaying the main content of the app.
- In macOS, suggestions render in a menu.
- In tvOS, suggestions render as a row underneath the search field.
- In watchOS, suggestions render in a list pushed onto the containing navigation stack.

## See Also

### Getting placements

- [content](content.md) — Search suggestions render in the main content of the app.
- [menu](menu.md) — Search suggestions render inside of a menu attached to the search field.
