---
title: skipsTranslation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/translationattributes/skipstranslation
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/translationattributes/skipstranslation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/translationattributes/skipstranslation.json'
content_hash: 'sha256:f66a3fd41b868633'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [TranslationAttributes](../translationattributes.md)

# skipsTranslation

<sub>Instance Property</sub>

An attribute that marks portions of an attributed string to be excluded from translation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let skipsTranslation: AttributeScopes.TranslationAttributes.SkipTranslationAttribute
```

## Discussion

Use this to exclude specific text ranges within an [AttributedString](../../attributedstring.md) from translation, such as proper nouns, brand names, technical terms, or other content that should remain unchanged across different languages.

When translating formatted text, you can mark specific ranges to skip translation:

```swift
var text = AttributedString("Welcome to Apple Park")
let range = text.range(of: "Apple Park")!
text[range].skipsTranslation = true
```

When translated the string, “Welcome to” changes to the target language, but “Apple Park” remains unchanged.

## See Also

### Handling translation behavior

- [SkipTranslationAttribute](skiptranslationattribute.md) — The attribute key for skipping translation.
