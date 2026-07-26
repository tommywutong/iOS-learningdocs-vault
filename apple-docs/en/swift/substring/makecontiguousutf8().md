---
title: makeContiguousUTF8()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/makecontiguousutf8()
source_url: 'https://developer.apple.com/documentation/swift/substring/makecontiguousutf8()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/makecontiguousutf8%28%29.json'
content_hash: 'sha256:05c97b5f8be35d8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# makeContiguousUTF8()

<sub>Instance Method</sub>

If this string is not contiguous, make it so. If this mutates the substring, it will invalidate any pre-existing indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func makeContiguousUTF8()
```

## Discussion

Complexity: O(n) if non-contiguous, O(1) if already contiguous
