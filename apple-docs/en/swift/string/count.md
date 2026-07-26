---
title: count
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/count
source_url: 'https://developer.apple.com/documentation/swift/string/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/count.json'
content_hash: 'sha256:a45ffa2b310c8045'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# count

<sub>Instance Property</sub>

The number of characters in a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether a string is empty, use its `isEmpty` property instead of comparing `count` to zero.

> [!abstract] Complexity
> O(n), where n is the length of the string.

## See Also

### Inspecting a String

- [isEmpty](isempty.md) — A Boolean value indicating whether a string has no characters.
