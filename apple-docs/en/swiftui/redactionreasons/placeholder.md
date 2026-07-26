---
title: placeholder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/redactionreasons/placeholder
source_url: 'https://developer.apple.com/documentation/swiftui/redactionreasons/placeholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/redactionreasons/placeholder.json'
content_hash: 'sha256:9c5156f299eca745'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RedactionReasons](../redactionreasons.md)

# placeholder

<sub>Type Property</sub>

Displayed data should appear as generic placeholders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let placeholder: RedactionReasons
```

## Discussion

Text and images will be automatically masked to appear as generic placeholders, though maintaining their original size and shape. Use this to create a placeholder UI without directly exposing placeholder data to users.

## See Also

### Getting redaction reasons

- [invalidated](invalidated.md) — Displayed data should appear as invalidated and pending a new update.
- [privacy](privacy.md) — Displayed data should be obscured to protect private information.
