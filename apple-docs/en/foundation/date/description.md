---
title: description
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/description
source_url: 'https://developer.apple.com/documentation/foundation/date/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/description.json'
content_hash: 'sha256:d9c2c07ef853fa2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# description

<sub>Instance Property</sub>

The representation is useful for debugging only. There are a number of options to acquire a formatted string for a date including: date formatters (see [NSDateFormatter](//apple_ref/occ/cl/NSDateFormatter) and [Data Formatting Guide](//apple_ref/doc/uid/10000029i)), and the `Date` function `description(locale:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## See Also

### Describing Dates

- [description(with:)](<description(with_).md>) — Returns a string representation of the receiver using the given locale.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the date. _(deprecated)_
