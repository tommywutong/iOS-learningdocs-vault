---
title: checkForASCII()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/checkforascii()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/checkforascii()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/checkforascii%28%29.json'
content_hash: 'sha256:2c7914aca95637fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# checkForASCII()

<sub>Instance Method</sub>

Do a scan checking for whether the contents are all-ASCII.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func checkForASCII() -> Bool
```

## Discussion

Updates the `isKnownASCII` bit if contents are all-ASCII.

> [!abstract] Complexity
> O(n)
