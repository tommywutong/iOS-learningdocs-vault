---
title: 'setCustomPronoun:forLanguage:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmorphology/setcustompronoun:forlanguage:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphology/setcustompronoun:forlanguage:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphology/setcustompronoun%3Aforlanguage%3Aerror%3A.json'
content_hash: 'sha256:71bdc0577a4a8e13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphology](../nsmorphology.md)

# setCustomPronoun:forLanguage:error:

<sub>Instance Method</sub>

Sets a custom pronoun behavior for this morphology to apply to the given language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) setCustomPronoun:(NSMorphologyCustomPronoun *) features forLanguage:(NSString *) language error:(NSError **) error;
```

## Parameters

- `features` — A [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md) instance for the morphology to use.

- `language` — The language the morphology applies the custom pronoun to.

- `error` — On return, any error encountered while setting the custom pronoun, or `nil` if no error occurred.

## Return Value

A Boolean value that indicates whether setting the custom pronoun succeeded.

## Discussion

This method throws if the system doesn’t support custom pronouns for the given language, or if any of the required pronoun keys aren’t set.

## See Also

### Related Documentation

- [isSupportedForLanguage:](../nsmorphologycustompronoun/issupportedforlanguage_.md) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
- [requiredKeysForLanguage:](../nsmorphologycustompronoun/requiredkeysforlanguage_.md) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_

### Accessing Per-Language Features

- [customPronounForLanguage:](custompronounforlanguage_.md) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
- [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_
