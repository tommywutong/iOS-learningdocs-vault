---
title: 'checkForNFC(quickCheck:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/checkfornfc(quickcheck:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/checkfornfc(quickcheck:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/checkfornfc%28quickcheck%3A%29.json'
content_hash: 'sha256:12a769d93e9d04bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# checkForNFC(quickCheck:)

<sub>Instance Method</sub>

Do a scan checking for whether the contents are in Normal Form C. When the contents are in NFC, canonical equivalence checks are much faster.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func checkForNFC(quickCheck: Bool) -> Bool
```

## Discussion

`quickCheck` will check for a subset of NFC contents using the NFCQuickCheck algorithm, which is faster than the full normalization algorithm. However, it cannot detect all NFC contents.

Updates the `isKnownNFC` bit.

> [!abstract] Complexity
> O(n)
