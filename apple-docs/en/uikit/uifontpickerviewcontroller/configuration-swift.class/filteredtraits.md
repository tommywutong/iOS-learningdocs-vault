---
title: filteredTraits
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredtraits
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredtraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/filteredtraits.json'
content_hash: 'sha256:150aa73d86d452ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontPickerViewController](../../uifontpickerviewcontroller.md) · [Configuration](../configuration-swift.class.md)

# filteredTraits

<sub>Instance Property</sub>

A predicate to filter fonts based on their traits, like bold, italic, or monospace.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var filteredTraits: UIFontDescriptor.SymbolicTraits { get set }
```

## See Also

### Filtering available fonts

- [includeFaces](includefaces.md) — A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [filteredLanguagesPredicate](filteredlanguagespredicate.md) — A predicate to filter fonts based on the languages they support. _(deprecated)_
- [+ filterPredicateForFilteredLanguages:](<filterpredicate(forfilteredlanguages_).md>) — Creates a font picker filter based on language support. _(deprecated)_
