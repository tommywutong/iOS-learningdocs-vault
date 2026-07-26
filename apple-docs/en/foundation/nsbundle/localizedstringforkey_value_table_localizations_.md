---
title: 'localizedStringForKey:value:table:localizations:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsbundle/localizedstringforkey:value:table:localizations:'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundle/localizedstringforkey:value:table:localizations:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundle/localizedstringforkey%3Avalue%3Atable%3Alocalizations%3A.json'
content_hash: 'sha256:ee9dfbcafe1d7c03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# localizedStringForKey:value:table:localizations:

<sub>Instance Method</sub>

Look up a localized string given a list of available localizations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSString *) localizedStringForKey:(NSString *) key value:(NSString *) value table:(NSString *) tableName localizations:(NSArray<NSString *> *) localizations;
```

## Parameters

- `key` — The key for the localized string to retrieve.

- `value` — A default value to return if a localized string for `key` cannot be found.

- `tableName` — The name of the strings file to search. If `nil`, the method uses tables in `Localizable.strings`.

- `localizations` — An array of BCP 47 language codes corresponding to available localizations. Bundle compares the array against its available localizations, and uses the best result to retrieve the localized string. If empty, we treat it as no localization is available, and may return a fallback.

## Return Value

A localized version of the string designated by `key` in table `tableName`.
