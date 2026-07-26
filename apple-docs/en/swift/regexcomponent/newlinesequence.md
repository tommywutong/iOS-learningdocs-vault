---
title: newlineSequence
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent/newlinesequence
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/newlinesequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/newlinesequence.json'
content_hash: 'sha256:2c29bf8ded541f2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# newlineSequence

<sub>Type Property</sub>

A character class that matches any newline sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var newlineSequence: CharacterClass { get }
```

## Discussion

This character class is equivalent to `\R` or `\n` in regex syntax.

## See Also

### Matching whitespace and line endings

- [horizontalWhitespace](horizontalwhitespace.md) — A character class that matches any element that is classified as horizontal whitespace.
- [verticalWhitespace](verticalwhitespace.md) — A character class that matches any element that is classified as vertical whitespace.
- [whitespace](whitespace.md) — A character class that matches any element that is classified as whitespace.
