---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/unicodescalarview/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:f0bedbaa75ee712f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Reserves enough space in the view’s underlying storage to store the specified number of ASCII characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ n: Int)
```

## Parameters

- `n` — The minimum number of ASCII character’s worth of storage to allocate.

## Discussion

Because a Unicode scalar value can require more than a single ASCII character’s worth of storage, additional allocation may be necessary when adding to a Unicode scalar view after a call to `reserveCapacity(_:)`.

> [!abstract] Complexity
> O(_n_), where _n_ is the capacity being reserved.
