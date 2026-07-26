---
title: 'requiredKeys(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/morphology/custompronoun/requiredkeys(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/morphology/custompronoun/requiredkeys(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/custompronoun/requiredkeys%28forlanguage%3A%29.json'
content_hash: 'sha256:d2c3e788a0f8f5d6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Morphology](../../morphology.md) · [CustomPronoun](../custompronoun.md)

# requiredKeys(forLanguage:)

<sub>Type Method</sub>

Returns a collection of the custom pronoun keys required by this language.

> [!warning] Deprecated
> Use TermOfAddress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func requiredKeys(forLanguage language: String) -> [PartialKeyPath<Morphology.CustomPronoun>]
```

## Parameters

- `language` — The language to create a custom pronoun for.

## Return Value

The keys required for the given language.

## Discussion

If any of the required keys for a given language are unset, calling [setCustomPronoun(_:forLanguage:)](<../setcustompronoun(__forlanguage_).md>) for that language with an incomplete [CustomPronoun](../custompronoun.md) instance throws an error.

## See Also

### Assessing Custom Pronoun Support

- [isSupported(forLanguage:)](<issupported(forlanguage_).md>) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
