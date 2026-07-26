---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/subscript%28_%3A%29.json'
content_hash: 'sha256:01ceaf57d8625f75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@objc override dynamic subscript(key: Any) -> Any? { get set }
```

## Parameters

- `key` — The key whose value you want to retrieve.

## Return Value

The value associated with the key, or `nil` if no value is associated with the key.
