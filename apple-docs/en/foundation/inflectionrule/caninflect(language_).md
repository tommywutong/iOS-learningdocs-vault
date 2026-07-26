---
title: 'canInflect(language:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inflectionrule/caninflect(language:)'
source_url: 'https://developer.apple.com/documentation/foundation/inflectionrule/caninflect(language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inflectionrule/caninflect%28language%3A%29.json'
content_hash: 'sha256:8fd9135d023f1db5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InflectionRule](../inflectionrule.md)

# canInflect(language:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the rule can inflect a given language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func canInflect(language: String) -> Bool
```

## Parameters

- `language` — The language to apply inflection to, specified as a BCP 47 language code.

## Return Value

`true` if the rule can inflect the given language; otherwise, `false`.

## See Also

### Determining Availability

- [canInflectPreferredLocalization](caninflectpreferredlocalization.md) — A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.
