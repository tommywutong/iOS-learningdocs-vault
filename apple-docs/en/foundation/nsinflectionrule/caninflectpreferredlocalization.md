---
title: canInflectPreferredLocalization
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinflectionrule/caninflectpreferredlocalization
source_url: 'https://developer.apple.com/documentation/foundation/nsinflectionrule/caninflectpreferredlocalization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinflectionrule/caninflectpreferredlocalization.json'
content_hash: 'sha256:2c22d85852763766'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInflectionRule](../nsinflectionrule.md)

# canInflectPreferredLocalization

<sub>Type Property</sub>

A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (class, readonly) BOOL canInflectPreferredLocalization;
```

## Discussion

This value doesn’t change throughout the lifetime of a process.

## See Also

### Determining Availability

- [canInflectLanguage:](caninflectlanguage_.md) — Returns a Boolean value that indicates whether the rule can inflect a given language.
