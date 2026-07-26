---
title: collation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/collation
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/collation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/collation.json'
content_hash: 'sha256:5a7b67e46accafac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# collation

<sub>Instance Property</sub>

The string sort order of the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var collation: Locale.Collation?
```

## Discussion

Set this property to override the locale’s default string sort order. To request the collation used by the locale, use the [Locale](../../locale.md) property [collation](../collation-swift.property.md).

This property corresponds to the `co` key of the Unicode BCP 47 extension.

## See Also

### Specifying ordering components

- [Collation](../collation-swift.struct.md) — A type that represents the string sort order used by the locale.
