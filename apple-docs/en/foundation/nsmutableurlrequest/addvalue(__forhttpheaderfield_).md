---
title: 'addValue(_:forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableurlrequest/addvalue(_:forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/addvalue(_:forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/addvalue%28_%3Aforhttpheaderfield%3A%29.json'
content_hash: 'sha256:7de88b90dd99a41f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# addValue(_:forHTTPHeaderField:)

<sub>Instance Method</sub>

Adds a value to the header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addValue(_ value: String, forHTTPHeaderField field: String)
```

## Parameters

- `value` — The value for the header field.

- `field` — The name of the header field. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## Discussion

This method provides the ability to add values to header fields incrementally. If a value was previously set for the specified field, the supplied value is appended to the existing value using the appropriate field delimiter (a comma).

Certain header fields are reserved (see [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers)). Do not use this method to change such headers.

## See Also

### Related Documentation

- [- valueForHTTPHeaderField:](<../nsurlrequest/value(forhttpheaderfield_).md>) — Returns the value of the specified HTTP header field.

### Accessing header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [- setValue:forHTTPHeaderField:](<setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
