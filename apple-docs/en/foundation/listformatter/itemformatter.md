---
title: itemFormatter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatter/itemformatter
source_url: 'https://developer.apple.com/documentation/foundation/listformatter/itemformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatter/itemformatter.json'
content_hash: 'sha256:c15660b2ba62a1d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatter](../listformatter.md)

# itemFormatter

<sub>Instance Property</sub>

An object that formats each item in the list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var itemFormatter: Formatter? { get set }
```

## Discussion

If this property isn’t set, the list formatter falls back to the item’s [- descriptionWithLocale:](<../nsarray/description(withlocale_).md>) or [localizedDescription](../progress/localizeddescription.md) methods if implemented. If those methods aren’t implemented, the formatter uses [description](../../objectivec/nsobjectprotocol/description.md) instead.

## See Also

### Configuring Formatter Options

- [locale](locale.md) — The locale to use when formatting items in the list.
