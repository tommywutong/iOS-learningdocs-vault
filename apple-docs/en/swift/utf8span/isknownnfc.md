---
title: isKnownNFC
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/isknownnfc
source_url: 'https://developer.apple.com/documentation/swift/utf8span/isknownnfc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/isknownnfc.json'
content_hash: 'sha256:f09415d45c84a20b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# isKnownNFC

<sub>Instance Property</sub>

Returns whether the contents are known to be NFC. This is not always checked at initialization time and is set by `checkForNFC`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isKnownNFC: Bool { get }
```

## Discussion

> [!abstract] Complexity
> O(1)
