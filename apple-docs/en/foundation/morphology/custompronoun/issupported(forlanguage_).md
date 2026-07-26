---
title: 'isSupported(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/morphology/custompronoun/issupported(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/morphology/custompronoun/issupported(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/custompronoun/issupported%28forlanguage%3A%29.json'
content_hash: 'sha256:3ec782546f970589'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Morphology](../../morphology.md) · [CustomPronoun](../custompronoun.md)

# isSupported(forLanguage:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the given language supports setting custom pronouns.

> [!warning] Deprecated
> Use TermOfAddress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func isSupported(forLanguage language: String) -> Bool
```

## Parameters

- `language` — The language to query.

## Return Value

`true` if the language supports custom pronouns; otherwise, `false`.

## Discussion

If this value is `false` for a given language, calling [setCustomPronoun(_:forLanguage:)](<../setcustompronoun(__forlanguage_).md>) for that language throws an error.

## See Also

### Assessing Custom Pronoun Support

- [requiredKeys(forLanguage:)](<requiredkeys(forlanguage_).md>) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_
