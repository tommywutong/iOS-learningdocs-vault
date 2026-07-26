---
title: whitespace
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent/whitespace
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/whitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/whitespace.json'
content_hash: 'sha256:25d95a0b0e84db4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# whitespace

<sub>Type Property</sub>

A character class that matches any element that is classified as whitespace.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var whitespace: CharacterClass { get }
```

## Discussion

This character class is equivalent to `\s` in regex syntax.

## See Also

### Matching whitespace and line endings

- [horizontalWhitespace](horizontalwhitespace.md) — A character class that matches any element that is classified as horizontal whitespace.
- [newlineSequence](newlinesequence.md) — A character class that matches any newline sequence.
- [verticalWhitespace](verticalwhitespace.md) — A character class that matches any element that is classified as vertical whitespace.
