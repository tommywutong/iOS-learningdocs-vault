---
title: 'init(name:value:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlqueryitem/init(name:value:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlqueryitem/init(name:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlqueryitem/init%28name%3Avalue%3A%29.json'
content_hash: 'sha256:7411ffc322e95795'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLQueryItem](../nsurlqueryitem.md)

# init(name:value:)

<sub>Initializer</sub>

Initializes a newly allocated query item with the specified name and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: String, value: String?)
```

## Parameters

- `name` — The name of the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `name` parameter is `q`.

- `value` — The value for the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `value` parameter is `iPad`.

## Return Value

An initialized query item object.

## Discussion

To use the newly initialized query item in composing a URL, add it to the [queryItems](../nsurlcomponents/queryitems.md) array of an [NSURLComponents](../nsurlcomponents.md) instance. Because assigning an array of query items to an [NSURLComponents](../nsurlcomponents.md) instance automatically encodes the name and value properties, you should not percent-encode these strings.
