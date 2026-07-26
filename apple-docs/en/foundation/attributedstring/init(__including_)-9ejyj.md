---
title: 'init(_:including:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(_:including:)-9ejyj'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(_:including:)-9ejyj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28_%3Aincluding%3A%29-9ejyj.json'
content_hash: 'sha256:0e5df06e9196e01b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(_:including:)

<sub>Initializer</sub>

Creates an attributed string from another attributed string, including an attribute scope that a key path identifies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S, T>(_ other: T, including scope: KeyPath<AttributeScopes, S.Type>) where S : AttributeScope, T : AttributedStringProtocol
```

## Parameters

- `other` — An attributed string or attributed substring.

- `scope` — An [AttributeScopes](../attributescopes.md) key path that identifies an attribute scope to associate with the attributed string.

## See Also

### Creating a Duplicate Attributed String

- [init(_:including:)](<init(__including_)-6u3ho.md>) — Creates an attributed string from another attributed string, including an attribute scope.
