---
title: 'applyListOrder(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/array/applylistorder(_:)-33po6'
source_url: 'https://developer.apple.com/documentation/swift/array/applylistorder(_:)-33po6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/applylistorder%28_%3A%29-33po6.json'
content_hash: 'sha256:def68803af14bc65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# applyListOrder(_:)

<sub>Instance Method</sub>

Reorders elements in place to match `order`, preserving elements not in `order`. Implements USD’s “ordered” list-op semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func applyListOrder(_ order: [String])
```

## Parameters

- `order` — The desired ordering for elements that appear in both `self` and `order`.
