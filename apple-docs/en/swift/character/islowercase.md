---
title: isLowercase
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/islowercase
source_url: 'https://developer.apple.com/documentation/swift/character/islowercase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/islowercase.json'
content_hash: 'sha256:56b20108e2f067ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isLowercase

<sub>Instance Property</sub>

A Boolean value indicating whether this character is considered lowercase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLowercase: Bool { get }
```

## Discussion

Lowercase characters change when converted to uppercase, but not when converted to lowercase. The following characters are all lowercase:

- “é” (U+0065 LATIN SMALL LETTER E, U+0301 COMBINING ACUTE ACCENT)
- “и” (U+0438 CYRILLIC SMALL LETTER I)
- “π” (U+03C0 GREEK SMALL LETTER PI)

## See Also

### Checking a Character’s Case

- [isCased](iscased.md) — A Boolean value indicating whether this character changes under any form of case conversion.
- [isUppercase](isuppercase.md) — A Boolean value indicating whether this character is considered uppercase.
- [uppercased()](<uppercased().md>) — Returns an uppercased version of this character.
- [lowercased()](<lowercased().md>) — Returns a lowercased version of this character.
