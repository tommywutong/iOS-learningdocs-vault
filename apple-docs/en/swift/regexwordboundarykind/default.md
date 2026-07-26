---
title: default
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexwordboundarykind/default
source_url: 'https://developer.apple.com/documentation/swift/regexwordboundarykind/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexwordboundarykind/default.json'
content_hash: 'sha256:fb792ff3db1fa404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexWordBoundaryKind](../regexwordboundarykind.md)

# default

<sub>Type Property</sub>

A word boundary algorithm that implements the “default word boundary” Unicode recommendation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var `default`: RegexWordBoundaryKind { get }
```

## Discussion

Default word boundaries use a Unicode algorithm that handles some cases better than simple word boundaries, such as words with internal punctuation, changes in script, and Emoji.
