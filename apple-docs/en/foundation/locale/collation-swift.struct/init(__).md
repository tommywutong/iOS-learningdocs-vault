---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/collation-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/collation-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/collation-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:3c94391090d44b78'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Collation](../collation-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a collation from a BCP 47 identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ identifier: String)
```

## Parameters

- `identifier` — The BCP 47 collation identifier, like `standard` for a language’s standard ordering, or `phonetic` for phonetic ordering.

## See Also

### Creating a collation

- [init(stringLiteral:)](<init(stringliteral_).md>) — Creates a collation from a BCP 47 identifier as a string literal.
