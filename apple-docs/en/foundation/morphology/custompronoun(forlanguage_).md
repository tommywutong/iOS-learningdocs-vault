---
title: 'customPronoun(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/morphology/custompronoun(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/morphology/custompronoun(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/custompronoun%28forlanguage%3A%29.json'
content_hash: 'sha256:7d2a672afcd85a1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# customPronoun(forLanguage:)

<sub>Instance Method</sub>

Returns any custom pronoun behavior this morphology applies to the given language.

> [!warning] Deprecated
> Use TermOfAddress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func customPronoun(forLanguage language: String) -> Morphology.CustomPronoun?
```

## Parameters

- `language` — The language to query for any custom pronoun behavior.

## Return Value

A [CustomPronoun](custompronoun.md) behavior this morphology uses for the given language, or `nil` if the morphology doesn’t have a custom pronoun behavior set.

## See Also

### Accessing Per-Language Features

- [setCustomPronoun(_:forLanguage:)](<setcustompronoun(__forlanguage_).md>) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [CustomPronoun](custompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_
