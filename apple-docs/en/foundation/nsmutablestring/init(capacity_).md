---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/init%28capacity%3A%29.json'
content_hash: 'sha256:b1bf27df74bf924a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# init(capacity:)

<sub>Initializer</sub>

Returns an `NSMutableString` object initialized with initial storage for a given number of characters,

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity: Int)
```

## Parameters

- `capacity` — The number of characters the string is expected to initially contain.

## Return Value

An initialized `NSMutableString` object with initial storage for `capacity` characters. The returned object might be different than the original receiver.

## Discussion

The number of characters indicated by `capacity` is simply a hint to increase the efficiency of data storage. The value does _not_ limit the length of the string.
