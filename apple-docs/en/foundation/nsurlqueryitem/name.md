---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlqueryitem/name
source_url: 'https://developer.apple.com/documentation/foundation/nsurlqueryitem/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlqueryitem/name.json'
content_hash: 'sha256:47bf76cfabc9843f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLQueryItem](../nsurlqueryitem.md)

# name

<sub>Instance Property</sub>

The name of the query item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String { get }
```

## Discussion

For example, in the URL `http://www.apple.com/search/?q=iPad`, the `name` parameter is `q`.

This string is not percent-encoded.

## See Also

### Related Documentation

- [queryItems](../nsurlcomponents/queryitems.md) — The query URL component as an array of name/value pairs.

### Reading a Query Item’s Name and Value

- [value](value.md) — The value for the query item.
