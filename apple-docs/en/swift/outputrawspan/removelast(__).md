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
doc_path: '/documentation/swift/outputrawspan/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/removelast%28_%3A%29.json'
content_hash: 'sha256:6e976629ab1b0372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# removeLast(_:)

<sub>Instance Method</sub>

Remove the last n bytes from this span, returning the memory they occupy to the uninitialized state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ n: Int)
```

## Parameters

- `n` — The number of bytes to remove. `n` must not be negative or greater than `byteCount`.

## Discussion

`n` must not be greater than `byteCount`.
