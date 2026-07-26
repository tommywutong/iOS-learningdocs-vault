---
title: 'value(forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlrequest/value(forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/value(forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/value%28forhttpheaderfield%3A%29.json'
content_hash: 'sha256:9f739e1a51d697c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# value(forHTTPHeaderField:)

<sub>Instance Method</sub>

Retrieves a header value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forHTTPHeaderField field: String) -> String?
```

## Parameters

- `field` — The header field name to use for the lookup (case-insensitive).

## Return Value

The value associated with the header field field,  or `nil` if there is no corresponding header field.

## Discussion

Note that, in keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## See Also

### Accessing header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [addValue(_:forHTTPHeaderField:)](<addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [setValue(_:forHTTPHeaderField:)](<setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
