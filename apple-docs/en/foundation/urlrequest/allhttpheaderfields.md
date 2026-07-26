---
title: allHTTPHeaderFields
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/allhttpheaderfields
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/allhttpheaderfields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/allhttpheaderfields.json'
content_hash: 'sha256:8f00e999f4eca188'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

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

- [addValue(_:forHTTPHeaderField:)](<addvalue(__forhttpheaderfield_).md>) — Adds a value to the header field.
- [setValue(_:forHTTPHeaderField:)](<setvalue(__forhttpheaderfield_).md>) — Sets a value for the header field.
- [value(forHTTPHeaderField:)](<value(forhttpheaderfield_).md>) — Retrieves a header value.
