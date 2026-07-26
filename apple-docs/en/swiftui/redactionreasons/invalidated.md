---
title: invalidated
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/redactionreasons/invalidated
source_url: 'https://developer.apple.com/documentation/swiftui/redactionreasons/invalidated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/redactionreasons/invalidated.json'
content_hash: 'sha256:e22c7885aa8bbfee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RedactionReasons](../redactionreasons.md)

# invalidated

<sub>Type Property</sub>

Displayed data should appear as invalidated and pending a new update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let invalidated: RedactionReasons
```

## Discussion

Views marked with [invalidatableContent(_:)](<../view/invalidatablecontent(__).md>) will be automatically redacted with a standard styling indicating the content is invalidated and new content will be available soon.

## See Also

### Getting redaction reasons

- [placeholder](placeholder.md) — Displayed data should appear as generic placeholders.
- [privacy](privacy.md) — Displayed data should be obscured to protect private information.
