---
title: 'isSupportedForLanguage:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmorphologycustompronoun/issupportedforlanguage:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun/issupportedforlanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphologycustompronoun/issupportedforlanguage%3A.json'
content_hash: 'sha256:59f07f65143e4e7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphologyCustomPronoun](../nsmorphologycustompronoun.md)

# isSupportedForLanguage:

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the given language supports setting custom pronouns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (BOOL) isSupportedForLanguage:(NSString *) language;
```

## Parameters

- `language` — The language to query.

## Return Value

`true` if the language supports custom pronouns; otherwise, `false`.

## See Also

### Assessing Custom Pronoun Support

- [requiredKeysForLanguage:](requiredkeysforlanguage_.md) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_
