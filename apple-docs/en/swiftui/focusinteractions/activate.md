---
title: activate
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusinteractions/activate
source_url: 'https://developer.apple.com/documentation/swiftui/focusinteractions/activate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusinteractions/activate.json'
content_hash: 'sha256:d2561b19b219bba3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusInteractions](../focusinteractions.md)

# activate

<sub>Type Property</sub>

The view has a primary action that can be activated via focus gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let activate: FocusInteractions
```

## Discussion

On macOS and iOS, focus-driven activation interactions are only possible when all-controls keyboard navigation is enabled. On tvOS and watchOS, focus-driven activation interactions are always possible.

## See Also

### Creating the interaction types

- [automatic](automatic.md) — The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [edit](edit.md) — The view captures input from non-spatial sources like a keyboard or Digital Crown.
