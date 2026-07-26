---
title: range
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyregexoutput/element/range
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/element/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/element/range.json'
content_hash: 'sha256:7aa422e137602226'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AnyRegexOutput](../../anyregexoutput.md) · [Element](../element.md)

# range

<sub>Instance Property</sub>

The range over which a value was captured, if there was a capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var range: Range<String.Index>? { get }
```

## Discussion

If nothing was captured, `range` is `nil`.
