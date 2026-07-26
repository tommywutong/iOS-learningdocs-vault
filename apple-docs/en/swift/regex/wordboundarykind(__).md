---
title: 'wordBoundaryKind(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/wordboundarykind(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/wordboundarykind(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/wordboundarykind%28_%3A%29.json'
content_hash: 'sha256:c0e6282a65ee4297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# wordBoundaryKind(_:)

<sub>Instance Method</sub>

Returns a regular expression that uses the specified word boundary algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wordBoundaryKind(_ wordBoundaryKind: RegexWordBoundaryKind) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `wordBoundaryKind` — The algorithm to use for determining word boundaries.

## Return Value

The modified regular expression.
