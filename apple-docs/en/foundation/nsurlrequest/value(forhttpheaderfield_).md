---
title: 'value(forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlrequest/value(forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/value(forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/value%28forhttpheaderfield%3A%29.json'
content_hash: 'sha256:63396299f90325bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# value(forHTTPHeaderField:)

<sub>Instance Method</sub>

Returns the value of the specified HTTP header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forHTTPHeaderField field: String) -> String?
```

## Parameters

- `field` — The name of the header field whose value is to be returned. In keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## Return Value

The value associated with the header field `field`, or `nil` if there is no corresponding header field.

## See Also

### Related Documentation

- [- addValue:forHTTPHeaderField:](<../nsmutableurlrequest/addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [- setValue:forHTTPHeaderField:](<../nsmutableurlrequest/setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.

### Getting header fields

- [allHTTPHeaderFields](allhttpheaderfields.md) — A dictionary containing all of the HTTP header fields for a request.
