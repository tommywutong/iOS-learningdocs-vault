---
title: isUppercase
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character/isuppercase
source_url: 'https://developer.apple.com/documentation/swift/character/isuppercase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/isuppercase.json'
content_hash: 'sha256:7277199157989ac8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# isUppercase

<sub>Instance Property</sub>

A Boolean value indicating whether this character is considered uppercase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUppercase: Bool { get }
```

## Discussion

Uppercase characters vary under case-conversion to lowercase, but not when converted to uppercase. The following characters are all uppercase:

- “É” (U+0045 LATIN CAPITAL LETTER E, U+0301 COMBINING ACUTE ACCENT)
- “И” (U+0418 CYRILLIC CAPITAL LETTER I)
- “Π” (U+03A0 GREEK CAPITAL LETTER PI)

## See Also

### Checking a Character’s Case

- [isCased](iscased.md) — A Boolean value indicating whether this character changes under any form of case conversion.
- [uppercased()](<uppercased().md>) — Returns an uppercased version of this character.
- [isLowercase](islowercase.md) — A Boolean value indicating whether this character is considered lowercase.
- [lowercased()](<lowercased().md>) — Returns a lowercased version of this character.
