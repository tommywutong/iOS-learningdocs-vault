---
title: simple
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexwordboundarykind/simple
source_url: 'https://developer.apple.com/documentation/swift/regexwordboundarykind/simple'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexwordboundarykind/simple.json'
content_hash: 'sha256:2b7e6786e1fb19bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexWordBoundaryKind](../regexwordboundarykind.md)

# simple

<sub>Type Property</sub>

A word boundary algorithm that implements the “simple word boundary” Unicode recommendation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var simple: RegexWordBoundaryKind { get }
```

## Discussion

A simple word boundary is a position in the input between two characters that match `/\w\W/` or `/\W\w/`, or between the start or end of the input and a `\w` character. Word boundaries therefore depend on the option- defined behavior of `\w`.
