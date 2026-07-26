---
title: ordinal
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/ordinal
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/ordinal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/ordinal.json'
content_hash: 'sha256:508adc6396a61236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# ordinal

<sub>Instance Property</sub>

The number for an item in an ordered list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger ordinal;
```

## Discussion

If the intent is not a list, the value of this property is `0`.

## See Also

### Getting list information

- [indentationLevel](indentationlevel.md) — The indentation level of the intent.
