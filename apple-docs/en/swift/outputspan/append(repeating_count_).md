---
title: 'append(repeating:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputspan/append(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/swift/outputspan/append(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan/append%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:c82e806e8f6158a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputSpan](../outputspan.md)

# append(repeating:count:)

<sub>Instance Method</sub>

Repeatedly append an element to this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(repeating repeatedValue: Element, count: Int)
```

## Parameters

- `repeatedValue` — The element to append repeatedly.

- `count` — The number of times to append `repeatedValue`. `count` must not exceed `freeCapacity`.
