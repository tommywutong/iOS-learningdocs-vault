---
title: unicodeScalar
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexsemanticlevel/unicodescalar
source_url: 'https://developer.apple.com/documentation/swift/regexsemanticlevel/unicodescalar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexsemanticlevel/unicodescalar.json'
content_hash: 'sha256:a40d4b4e73fe2acc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexSemanticLevel](../regexsemanticlevel.md)

# unicodeScalar

<sub>Type Property</sub>

Match at the Unicode scalar level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var unicodeScalar: RegexSemanticLevel { get }
```

## Discussion

At this semantic level, the string’s `UnicodeScalarView` is used for matching, and each matched element is a `UnicodeScalar` value.
