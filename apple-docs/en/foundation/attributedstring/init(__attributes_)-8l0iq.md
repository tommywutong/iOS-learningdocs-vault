---
title: 'init(_:attributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(_:attributes:)-8l0iq'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(_:attributes:)-8l0iq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28_%3Aattributes%3A%29-8l0iq.json'
content_hash: 'sha256:074fe346ffc3548d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(_:attributes:)

<sub>Initializer</sub>

Creates an attributed string from a character sequence and an attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ elements: S, attributes: AttributeContainer = .init()) where S : Sequence, S.Element == Character
```

## Parameters

- `elements` — A character sequence that provides the textual content for the attributed string.

- `attributes` — Attributes to apply to the textual content.

## See Also

### Creating an Attributed String

- [init()](<init().md>) — Creates an empty attributed string.
- [init(_:)](<init(__)-8tnoq.md>) — Creates an attributed string from an attributed substring.
- [init(_:attributes:)](<init(__attributes_)-2a45h.md>) — Creates an attributed string from a string and an attribute container.
- [init(_:attributes:)](<init(__attributes_)-8jqhp.md>) — Creates an attributed string from a substring and an attribute container.
- [AttributeContainer](../attributecontainer.md) — A container for attribute keys and values.
