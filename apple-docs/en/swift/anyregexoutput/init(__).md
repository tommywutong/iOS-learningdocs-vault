---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyregexoutput/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/init%28_%3A%29.json'
content_hash: 'sha256:0465e0d611ce3c19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRegexOutput](../anyregexoutput.md)

# init(_:)

<sub>Initializer</sub>

Creates a dynamic regular expression match output from an existing match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Output>(_ match: Regex<Output>.Match)
```

## Discussion

You can use this initializer when you need an `AnyRegexOutput` instance instead of the output type of a strongly-typed `Regex.Match`.
