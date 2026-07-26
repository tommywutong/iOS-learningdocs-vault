---
title: anyNonNewline
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent/anynonnewline
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/anynonnewline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/anynonnewline.json'
content_hash: 'sha256:1b03a11a2bf74961'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# anyNonNewline

<sub>Type Property</sub>

A character class that matches any element that isn’t a newline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var anyNonNewline: CharacterClass { get }
```

## Discussion

This character class is unaffected by the `dotMatchesNewlines()` method. To match any character, including newlines, see [any](any.md).

This character class is equivalent to the regex syntax “dot” metacharacter with single-line mode disabled: `(?-s:.)`.

## See Also

### Matching substring sequences

- [anyOf(_:)](<anyof(__)-3pexl.md>) — Returns a character class that matches any Unicode scalar in the given sequence.
- [anyOf(_:)](<anyof(__)-4xgea.md>) — Returns a character class that matches any character in the given string or sequence.
- [any](any.md) — A character class that matches any element.
- [anyGraphemeCluster](anygraphemecluster.md) — A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [digit](digit.md) — A character class that matches any digit.
- [hexDigit](hexdigit.md) — A character class that matches any hexadecimal digit.
- [word](word.md) — A character class that matches any element that is a “word character”.
