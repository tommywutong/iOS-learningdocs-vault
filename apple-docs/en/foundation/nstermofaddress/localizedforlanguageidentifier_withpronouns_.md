---
title: 'localizedForLanguageIdentifier:withPronouns:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstermofaddress/localizedforlanguageidentifier:withpronouns:'
source_url: 'https://developer.apple.com/documentation/foundation/nstermofaddress/localizedforlanguageidentifier:withpronouns:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstermofaddress/localizedforlanguageidentifier%3Awithpronouns%3A.json'
content_hash: 'sha256:d4c49c621581158c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTermOfAddress](../nstermofaddress.md)

# localizedForLanguageIdentifier:withPronouns:

<sub>Type Method</sub>

A term of address restricted to a given language

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) localizedForLanguageIdentifier:(NSString *) language withPronouns:(NSArray<NSMorphologyPronoun *> *) pronouns;
```

## Parameters

- `language` — ISO language code identifier for the language

- `pronouns` — A list of pronouns in the target language that can be used to refer to the person.
