---
title: 'value(forHTTPHeaderField:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpurlresponse/value(forhttpheaderfield:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpurlresponse/value(forhttpheaderfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpurlresponse/value%28forhttpheaderfield%3A%29.json'
content_hash: 'sha256:b16049864901a516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPURLResponse](../httpurlresponse.md)

# value(forHTTPHeaderField:)

<sub>Instance Method</sub>

Returns the value that corresponds to the given header field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forHTTPHeaderField field: String) -> String?
```

## Parameters

- `field` — The name of the header field you want to retrieve. The name is case-insensitive.

## Return Value

The value associated with the given header field, or `nil` if no value is associated with the field.

## Discussion

In keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## See Also

### Getting HTTP response headers

- [allHeaderFields](allheaderfields.md) — All HTTP header fields of the response.
