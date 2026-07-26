---
title: 'setValue(_:forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableurlrequest/setvalue(_:forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/setvalue(_:forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/setvalue%28_%3Aforhttpheaderfield%3A%29.json'
content_hash: 'sha256:75098931de53a20e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# setValue(_:forHTTPHeaderField:)

<sub>Instance Method</sub>

Sets a value for the header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: String?, forHTTPHeaderField field: String)
```

## Parameters

- `value` — The new value for the header field. Any existing value for the field is replaced by the new value.

- `field` — The name of the header field to set. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## Discussion

Certain header fields are reserved. Do not use this method to set such headers. Specifically, there is no need for you to set the `Content-Length` header. See [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers).

## See Also

### Related Documentation

- [- valueForHTTPHeaderField:](<../nsurlrequest/value(forhttpheaderfield_).md>) — Returns the value of the specified HTTP header field.

### Accessing header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [- addValue:forHTTPHeaderField:](<addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
