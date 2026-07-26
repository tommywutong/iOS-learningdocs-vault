---
title: 'customPronounForLanguage:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmorphology/custompronounforlanguage:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphology/custompronounforlanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphology/custompronounforlanguage%3A.json'
content_hash: 'sha256:2b0d4b8bd9e906a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphology](../nsmorphology.md)

# customPronounForLanguage:

<sub>Instance Method</sub>

Returns any custom pronoun behavior this morphology applies to the given language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMorphologyCustomPronoun *) customPronounForLanguage:(NSString *) language;
```

## Parameters

- `language` — The language to query for any custom pronoun behavior.

## Return Value

A [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md) behavior this morphology uses for the given language, or `nil` if the morphology doesn’t have a custom pronoun behavior set.

## See Also

### Accessing Per-Language Features

- [setCustomPronoun:forLanguage:error:](setcustompronoun_forlanguage_error_.md) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_
