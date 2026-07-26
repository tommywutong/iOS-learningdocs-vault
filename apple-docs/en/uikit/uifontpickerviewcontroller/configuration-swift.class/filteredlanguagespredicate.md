---
title: filteredLanguagesPredicate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredlanguagespredicate.json'
content_hash: 'sha256:e0ce91683851e673'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontPickerViewController](../../uifontpickerviewcontroller.md) · [Configuration](../configuration-swift.class.md)

# filteredLanguagesPredicate

<sub>Instance Property</sub>

A predicate to filter fonts based on the languages they support.

> [!warning] Deprecated
> Use [languageFilter](languagefilter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var filteredLanguagesPredicate: NSPredicate? { get set }
```

## Discussion

By default, the font picker shows all available fonts, regardless of the languages they support. You may prefer to offer only fonts that support certain languages. To restrict the list, set this property to an [NSPredicate](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_206) defining the logic the font picker should apply to the fonts’ supported languages metadata.

Use language specifiers in the same format [CFLocale](../../../corefoundation/cflocale.md) uses to specify languages in a filter predicate. You can use [+ filterPredicateForFilteredLanguages:](<filterpredicate(forfilteredlanguages_).md>) to construct a simple predicate that excludes fonts which don’t support any of a collection of languages you specify.

## See Also

### Filtering available fonts

- [includeFaces](includefaces.md) — A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [filteredTraits](filteredtraits.md) — A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [+ filterPredicateForFilteredLanguages:](<filterpredicate(forfilteredlanguages_).md>) — Creates a font picker filter based on language support. _(deprecated)_
