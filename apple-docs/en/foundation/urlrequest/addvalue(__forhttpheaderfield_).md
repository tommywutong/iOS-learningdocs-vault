---
title: 'addValue(_:forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlrequest/addvalue(_:forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/addvalue(_:forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/addvalue%28_%3Aforhttpheaderfield%3A%29.json'
content_hash: 'sha256:38f87c1ae60dd07f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# addValue(_:forHTTPHeaderField:)

<sub>Instance Method</sub>

Adds a value to the header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addValue(_ value: String, forHTTPHeaderField field: String)
```

## Parameters

- `value` — The value for the header field.

- `field` — The name of the header field. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## Discussion

This method provides the ability to add values to header fields incrementally. If a value was previously set for the specified field, the supplied value is appended to the existing value using the appropriate field delimiter (a comma).

Certain header fields are reserved (see [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers)). Do not use this method to change such headers.

## See Also

### Accessing header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [setValue(_:forHTTPHeaderField:)](<setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
- [value(forHTTPHeaderField:)](<value(forhttpheaderfield_).md>) — Retrieves a header value.
