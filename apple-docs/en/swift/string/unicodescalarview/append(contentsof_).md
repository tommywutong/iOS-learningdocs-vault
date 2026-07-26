---
title: 'append(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/unicodescalarview/append(contentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/append(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/append%28contentsof%3A%29.json'
content_hash: 'sha256:87a540ec229a26ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# append(contentsOf:)

<sub>Instance Method</sub>

Appends the Unicode scalar values in the given sequence to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<S>(contentsOf newElements: S) where S : Sequence, S.Element == Unicode.Scalar
```

## Parameters

- `newElements` — A sequence of Unicode scalar values.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the resulting view.
