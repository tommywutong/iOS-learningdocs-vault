---
title: 'removeLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputspan/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/outputspan/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan/removelast%28_%3A%29.json'
content_hash: 'sha256:af4b2b797159859b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputSpan](../outputspan.md)

# removeLast(_:)

<sub>Instance Method</sub>

Remove the last n elements of this span, returning the memory they occupy to the uninitialized state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ n: Int)
```

## Parameters

- `n` — The number of elements to remove. `n` must not be negative or greater than `count`.

## Discussion

`n` must not be greater than `count`.
