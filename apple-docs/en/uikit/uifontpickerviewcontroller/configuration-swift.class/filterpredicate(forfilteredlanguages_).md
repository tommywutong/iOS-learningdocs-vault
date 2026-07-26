---
title: 'filterPredicate(forFilteredLanguages:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filterpredicate(forfilteredlanguages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filterpredicate%28forfilteredlanguages%3A%29.json'
content_hash: 'sha256:43c947391e5cb2fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontPickerViewController](../../uifontpickerviewcontroller.md) · [Configuration](../configuration-swift.class.md)

# filterPredicate(forFilteredLanguages:)

<sub>Type Method</sub>

Creates a font picker filter based on language support.

> [!warning] Deprecated
> Use [languageFilter](languagefilter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func filterPredicate(forFilteredLanguages filteredLanguages: [String]) -> NSPredicate?
```

## Parameters

- `filteredLanguages` — Identifiers for the languages the font picker should include.

## Return Value

A predicate that is [true](../../../swift/true.md) when at least one of the provided strings is present.

## Discussion

Use this method to construct a predicate for [filteredLanguagesPredicate](filteredlanguagespredicate.md) that restricts the font picker’s list to only include fonts that support the filtered languages. Provide language identifiers in the same format [CFLocale](../../../corefoundation/cflocale.md) uses.

## See Also

### Filtering available fonts

- [includeFaces](includefaces.md) — A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [filteredTraits](filteredtraits.md) — A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [filteredLanguagesPredicate](filteredlanguagespredicate.md) — A predicate to filter fonts based on the languages they support. _(deprecated)_
