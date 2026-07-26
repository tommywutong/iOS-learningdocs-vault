---
title: 'generalCategory(_:)'
framework: RegexBuilder
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/characterclass/generalcategory(_:)'
source_url: 'https://developer.apple.com/documentation/regexbuilder/characterclass/generalcategory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/characterclass/generalcategory%28_%3A%29.json'
content_hash: 'sha256:1583cf782691e2c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [CharacterClass](../characterclass.md)

# generalCategory(_:)

<sub>Type Method</sub>

Returns a character class that matches any element with the given Unicode general category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func generalCategory(_ category: Unicode.GeneralCategory) -> CharacterClass
```

## Discussion

For example, when passed `.uppercaseLetter`, this method is equivalent to `/\p{Uppercase_Letter}/` or `/\p{Lu}/`.
