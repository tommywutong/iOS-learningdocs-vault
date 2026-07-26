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
doc_path: '/documentation/foundation/attributedstring/init(_:including:)-6u3ho'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(_:including:)-6u3ho'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28_%3Aincluding%3A%29-6u3ho.json'
content_hash: 'sha256:89c4b910002495e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(_:including:)

<sub>Initializer</sub>

Creates an attributed string from another attributed string, including an attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S, T>(_ other: T, including scope: S.Type) where S : AttributeScope, T : AttributedStringProtocol
```

## Parameters

- `other` — An attributed string or attributed substring.

- `scope` — An attribute scope to associate with the attributed string.

## See Also

### Creating a Duplicate Attributed String

- [init(_:including:)](<init(__including_)-9ejyj.md>) — Creates an attributed string from another attributed string, including an attribute scope that a key path identifies.
