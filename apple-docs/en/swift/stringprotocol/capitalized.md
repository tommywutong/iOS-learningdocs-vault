---
title: capitalized
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stringprotocol/capitalized
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/capitalized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/capitalized.json'
content_hash: 'sha256:df01b2a1f334ed4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# capitalized

<sub>Instance Property</sub>

A copy of the string with each word changed to its corresponding capitalized spelling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var capitalized: String { get }
```

## Discussion

This property performs the canonical (non-localized) mapping. It is suitable for programming operations that require stable results not depending on the current locale.

A capitalized string is a string with the first character in each word changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values. A “word” is any sequence of characters delimited by spaces, tabs, or line terminators. Some common word delimiting punctuation isn’t considered, so this property may not generally produce the desired results for multiword strings. See the `getLineStart(_:end:contentsEnd:for:)` method for additional information.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals.
