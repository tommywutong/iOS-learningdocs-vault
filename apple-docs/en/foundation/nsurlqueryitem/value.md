---
title: value
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlqueryitem/value
source_url: 'https://developer.apple.com/documentation/foundation/nsurlqueryitem/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlqueryitem/value.json'
content_hash: 'sha256:e9a4a3bdb56077af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLQueryItem](../nsurlqueryitem.md)

# value

<sub>Instance Property</sub>

The value for the query item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: String? { get }
```

## Discussion

For example, in the URL `http://www.apple.com/search/?q=iPad`, the `value` parameter is `iPad`.

This string is not percent-encoded.

## See Also

### Related Documentation

- [queryItems](../nsurlcomponents/queryitems.md) — The query URL component as an array of name/value pairs.

### Reading a Query Item’s Name and Value

- [name](name.md) — The name of the query item.
