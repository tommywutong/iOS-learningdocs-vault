---
title: 'appending(queryItems:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/appending(queryitems:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appending(queryitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appending%28queryitems%3A%29.json'
content_hash: 'sha256:9708f92bf582a101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appending(queryItems:)

<sub>Instance Method</sub>

Returns a new URL formed by appending a list of query items to the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appending(queryItems: [URLQueryItem]) -> URL
```

## Parameters

- `queryItems` — An array of [URLQueryItem](../urlqueryitem.md) instances to append to the URL.

## See Also

### Adding query items

- [append(queryItems:)](<append(queryitems_).md>) — Appends a list of query items to the URL.
- [URLQueryItem](../urlqueryitem.md) — A single name-value pair from the query portion of a URL.
