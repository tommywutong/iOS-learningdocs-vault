---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(_:)-1fru0'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(_:)-1fru0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28_%3A%29-1fru0.json'
content_hash: 'sha256:1dca74744c7f5196'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(_:)

<sub>Initializer</sub>

Creates a value-type attributed string from a reference type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ nsStr: NSAttributedString)
```

## Parameters

- `nsStr` — The [NSAttributedString](../nsattributedstring.md) to convert.

## Discussion

This initializer includes all attribute scopes defined by the SDK, such as [FoundationAttributes](../attributescopes/foundationattributes.md), [SwiftUIAttributes](../attributescopes/swiftuiattributes.md), and [AccessibilityAttributes](../attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [init(_:including:)](<init(__including_)-9no47.md>) or [init(_:including:)](<init(__including_)-puv0.md>).

## See Also

### Creating an Attributed String from a Reference Type

- [init(_:including:)](<init(__including_)-9no47.md>) — Creates a value-type attributed string from a reference type, including an attribute scope.
- [init(_:including:)](<init(__including_)-puv0.md>) — Creates a value-type attributed string from a reference type, including an attribute scope that a key path identifies.
