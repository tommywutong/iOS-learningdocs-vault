---
title: 'inflected(locale:userTermOfAddress:inflectionConcepts:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/inflected(locale:usertermofaddress:inflectionconcepts:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/inflected(locale:usertermofaddress:inflectionconcepts:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/inflected%28locale%3Ausertermofaddress%3Ainflectionconcepts%3A%29.json'
content_hash: 'sha256:67670dcfda851790'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# inflected(locale:userTermOfAddress:inflectionConcepts:)

<sub>Instance Method</sub>

Process automatic grammar agreement and formatting attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func inflected(locale: Locale = .current, userTermOfAddress: TermOfAddress? = .currentUser, inflectionConcepts: [InflectionConcept] = []) -> AttributedString
```

## Parameters

- `locale` — The locale used for formatting the string. It also specifies the language used for automatic grammar agreement, unless overridden with the `languageIdentifier` attribute.

- `userTermOfAddress` — The user’s preferred term of address, if the user has set one. A value of `nil` indicates no preference, in which case the inflection alternative will be used for strings that address the the user. Default value is `.currentUser`.

- `inflectionConcepts` — A list of objects providing additional hints for automatic grammar agreement, such as terms of address for people who are mentioned, or phrases with which the string has to grammatically agree.

## Discussion

Arguments that were previously formatted in the string must be annotated with the following attributes:

- `replacementIndex`, set to the index of the format specifier.
- `localizedNumericArgument`, if the argument was numeric, must also be set to the original value of the argument. If not all arguments are properly annotated, the `agreeWithArgument` and `inflect` attributes may not work properly and behavior is undefined.
