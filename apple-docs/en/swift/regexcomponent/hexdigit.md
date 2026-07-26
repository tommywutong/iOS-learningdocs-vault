---
title: hexDigit
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent/hexdigit
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/hexdigit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/hexdigit.json'
content_hash: 'sha256:bcd397fe77d3516a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# hexDigit

<sub>Type Property</sub>

A character class that matches any hexadecimal digit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hexDigit: CharacterClass { get }
```

## Discussion

`hexDigit` matches the ASCII characters `0` through `9`, and upper- or lowercase `a` through `f`. The corresponding characters in the “Halfwidth and Fullwidth Forms” Unicode block are not matched by this character class.

## See Also

### Matching substring sequences

- [anyOf(_:)](<anyof(__)-3pexl.md>) — Returns a character class that matches any Unicode scalar in the given sequence.
- [anyOf(_:)](<anyof(__)-4xgea.md>) — Returns a character class that matches any character in the given string or sequence.
- [any](any.md) — A character class that matches any element.
- [anyGraphemeCluster](anygraphemecluster.md) — A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [anyNonNewline](anynonnewline.md) — A character class that matches any element that isn’t a newline.
- [digit](digit.md) — A character class that matches any digit.
- [word](word.md) — A character class that matches any element that is a “word character”.
