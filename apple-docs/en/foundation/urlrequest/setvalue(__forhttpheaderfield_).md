---
title: 'setValue(_:forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlrequest/setvalue(_:forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/setvalue(_:forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/setvalue%28_%3Aforhttpheaderfield%3A%29.json'
content_hash: 'sha256:99514e8032523602'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# setValue(_:forHTTPHeaderField:)

<sub>Instance Method</sub>

Sets a value for the header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setValue(_ value: String?, forHTTPHeaderField field: String)
```

## Parameters

- `value` — The new value for the header field. Any existing value for the field is replaced by the new value.

- `field` — The name of the header field to set. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## Discussion

Certain header fields are reserved. Do not use this method to set such headers. Specifically, there is no need for you to set the `Content-Length` header. See [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers).

## See Also

### Accessing header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
- [addValue(_:forHTTPHeaderField:)](<addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [value(forHTTPHeaderField:)](<value(forhttpheaderfield_).md>) — Retrieves a header value.
