---
title: 'canInflectLanguage:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinflectionrule/caninflectlanguage:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinflectionrule/caninflectlanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinflectionrule/caninflectlanguage%3A.json'
content_hash: 'sha256:a1c68a334b38b68a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInflectionRule](../nsinflectionrule.md)

# canInflectLanguage:

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the rule can inflect a given language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (BOOL) canInflectLanguage:(NSString *) language;
```

## Parameters

- `language` — The language to apply inflection to, specified as a BCP 47 language code.

## See Also

### Determining Availability

- [canInflectPreferredLocalization](caninflectpreferredlocalization.md) — A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.
