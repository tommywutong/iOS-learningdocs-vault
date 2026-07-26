---
title: allHTTPHeaderFields
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest/allhttpheaderfields
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allhttpheaderfields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/allhttpheaderfields.json'
content_hash: 'sha256:3d0534a237e9c46f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# allHTTPHeaderFields

<sub>Instance Property</sub>

A dictionary containing all of the HTTP header fields for a request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allHTTPHeaderFields: [String : String]? { get set }
```

## Discussion

Certain header fields are reserved (see [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers)). Do not use this property to set such headers.

## See Also

### Accessing header fields

- [- addValue:forHTTPHeaderField:](<addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [- setValue:forHTTPHeaderField:](<setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
