---
title: 'rangeOfComposedCharacterSequences(for:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/rangeofcomposedcharactersequences(for:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/rangeofcomposedcharactersequences(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/rangeofcomposedcharactersequences%28for%3A%29.json'
content_hash: 'sha256:4e52b22864b45c42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# rangeOfComposedCharacterSequences(for:)

<sub>Instance Method</sub>

Returns the range in the string of the composed character sequences for a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfComposedCharacterSequences<R>(for range: R) -> Range<Self.Index> where R : RangeExpression, R.Bound == String.Index
```
