---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28_%3A%29.json'
content_hash: 'sha256:f6d4df7c5b260261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(_:)

<sub>Initializer</sub>

Creates a reference-type attributed string from the specified value-type attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(_ attrStr: AttributedString)
```

## Parameters

- `attrStr` — The value type attributed string that provides the text and attributes of the new object.

## Discussion

This initializer includes all attribute scopes defined by the SDK, such as [FoundationAttributes](../attributescopes/foundationattributes.md), [SwiftUIAttributes](../attributescopes/swiftuiattributes.md), and [AccessibilityAttributes](../attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [init(_:including:)](<init(__including_)-9gogq.md>) or [init(_:including:)](<init(__including_)-8iy4i.md>).

## See Also

### Creating a formatted string

- [init(_:including:)](<init(__including_)-9gogq.md>) — Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
- [init(_:including:)](<init(__including_)-8iy4i.md>) — Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.
