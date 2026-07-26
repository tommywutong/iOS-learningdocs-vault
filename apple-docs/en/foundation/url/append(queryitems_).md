---
title: 'append(queryItems:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/append(queryitems:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/append(queryitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/append%28queryitems%3A%29.json'
content_hash: 'sha256:a7b8794cd8d5e64a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# append(queryItems:)

<sub>Instance Method</sub>

Appends a list of query items to the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(queryItems: [URLQueryItem])
```

## Parameters

- `queryItems` — An array of [URLQueryItem](../urlqueryitem.md) instances to append to the URL.

## See Also

### Adding query items

- [appending(queryItems:)](<appending(queryitems_).md>) — Returns a new URL formed by appending a list of query items to the URL.
- [URLQueryItem](../urlqueryitem.md) — A single name-value pair from the query portion of a URL.
