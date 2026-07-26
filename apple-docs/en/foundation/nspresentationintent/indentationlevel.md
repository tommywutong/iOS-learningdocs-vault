---
title: indentationLevel
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/indentationlevel
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/indentationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/indentationlevel.json'
content_hash: 'sha256:5f6285e3e05f5338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# indentationLevel

<sub>Instance Property</sub>

The indentation level of the intent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger indentationLevel;
```

## Discussion

The initial list has an indentation level of `0`. Each time you nest a new list, the indentation level for new list increases by `1`. All elements within the same list have the same indentation level.

## See Also

### Getting list information

- [ordinal](ordinal.md) — The number for an item in an ordered list.
