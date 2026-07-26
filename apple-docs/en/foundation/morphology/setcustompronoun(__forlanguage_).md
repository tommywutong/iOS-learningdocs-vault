---
title: 'setCustomPronoun(_:forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/morphology/setcustompronoun(_:forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/morphology/setcustompronoun(_:forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/setcustompronoun%28_%3Aforlanguage%3A%29.json'
content_hash: 'sha256:4a6ba1cb2fd328a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# setCustomPronoun(_:forLanguage:)

<sub>Instance Method</sub>

Sets a custom pronoun behavior for this morphology to apply to the given language.

> [!warning] Deprecated
> Use TermOfAddress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setCustomPronoun(_ pronoun: Morphology.CustomPronoun?, forLanguage language: String) throws
```

## Parameters

- `pronoun` — A [CustomPronoun](custompronoun.md) instance for the morphology to use.

- `language` — The language the morphology should apply the custom pronoun to.

## Discussion

This method throws if the system doesn’t support custom pronouns for the given language, or if any of the required pronoun keys aren’t set.

## See Also

### Related Documentation

- [isSupported(forLanguage:)](<custompronoun/issupported(forlanguage_).md>) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
- [requiredKeys(forLanguage:)](<custompronoun/requiredkeys(forlanguage_).md>) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_

### Accessing Per-Language Features

- [customPronoun(forLanguage:)](<custompronoun(forlanguage_).md>) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
- [CustomPronoun](custompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_
