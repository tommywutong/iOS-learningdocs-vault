---
title: 'requiredKeysForLanguage:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmorphologycustompronoun/requiredkeysforlanguage:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun/requiredkeysforlanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphologycustompronoun/requiredkeysforlanguage%3A.json'
content_hash: 'sha256:45845f3d7ad6d59a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md)

# requiredKeysForLanguage:

<sub>Type Method</sub>

Returns a collection of the custom pronoun keys required by this language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSArray<NSString *> *) requiredKeysForLanguage:(NSString *) language;
```

## Parameters

- `language` — The language to create a custom pronoun for.

## Return Value

The keys required for the given language.

## Discussion

If any of the required keys for a given language are unset, calling [setCustomPronoun:forLanguage:error:](../nsmorphology/setcustompronoun_forlanguage_error_.md) for that language with an incomplete [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md) results in an error.

## See Also

### Assessing Custom Pronoun Support

- [isSupportedForLanguage:](issupportedforlanguage_.md) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
