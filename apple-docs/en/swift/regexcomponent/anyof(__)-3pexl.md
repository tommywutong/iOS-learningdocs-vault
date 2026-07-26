---
title: 'anyOf(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/anyof(_:)-3pexl'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/anyof(_:)-3pexl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/anyof%28_%3A%29-3pexl.json'
content_hash: 'sha256:806b440ea2ed7fd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# anyOf(_:)

<sub>Type Method</sub>

Returns a character class that matches any Unicode scalar in the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func anyOf<S>(_ s: S) -> CharacterClass where S : Sequence, S.Element == Unicode.Scalar
```

## Discussion

Calling this method with a group of Unicode scalars is equivalent to listing them in a custom character class in regex syntax.

## See Also

### Matching substring sequences

- [anyOf(_:)](<anyof(__)-4xgea.md>) — Returns a character class that matches any character in the given string or sequence.
- [any](any.md) — A character class that matches any element.
- [anyGraphemeCluster](anygraphemecluster.md) — A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [anyNonNewline](anynonnewline.md) — A character class that matches any element that isn’t a newline.
- [digit](digit.md) — A character class that matches any digit.
- [hexDigit](hexdigit.md) — A character class that matches any hexadecimal digit.
- [word](word.md) — A character class that matches any element that is a “word character”.
