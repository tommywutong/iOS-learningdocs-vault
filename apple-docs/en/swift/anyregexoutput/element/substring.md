---
title: substring
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyregexoutput/element/substring
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/element/substring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/element/substring.json'
content_hash: 'sha256:472b4b2993d5b309'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AnyRegexOutput](../../anyregexoutput.md) · [Element](../element.md)

# substring

<sub>Instance Property</sub>

The slice of the input which was captured, if there was a capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var substring: Substring? { get }
```

## Discussion

If nothing was captured, `substring` is `nil`.
