---
title: edit
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusinteractions/edit
source_url: 'https://developer.apple.com/documentation/swiftui/focusinteractions/edit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusinteractions/edit.json'
content_hash: 'sha256:f8f29ea3a33d9706'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusInteractions](../focusinteractions.md)

# edit

<sub>Type Property</sub>

The view captures input from non-spatial sources like a keyboard or Digital Crown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let edit: FocusInteractions
```

## Discussion

Views that support focus-driven editing interactions become focused when the user taps or clicks on them, or when the user issues a focus movement command.

## See Also

### Creating the interaction types

- [automatic](automatic.md) — The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [activate](activate.md) — The view has a primary action that can be activated via focus gestures.
