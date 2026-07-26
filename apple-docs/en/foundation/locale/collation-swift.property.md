---
title: collation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/collation-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/collation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/collation-swift.property.json'
content_hash: 'sha256:3b25ad43aecf5035'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# collation

<sub>Instance Property</sub>

The string sort order of the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var collation: Locale.Collation { get }
```

## Discussion

This property corresponds to the `co` key of the Unicode BCP 47 extension.

For locale instances created with the `co` specifier (such as `en-US@co=phonetic`), or with a custom [Components](components.md), this property represents the custom collation. Otherwise, it represents the locale’s default sort order.

## See Also

### Getting ordering components

- [Collation](collation-swift.struct.md) — A type that represents the string sort order used by the locale.
