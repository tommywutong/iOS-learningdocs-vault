---
title: includeFaces
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/includefaces
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/includefaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class/includefaces.json'
content_hash: 'sha256:a0fa7dee4863046b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontPickerViewController](../../uifontpickerviewcontroller.md) · [Configuration](../configuration-swift.class.md)

# includeFaces

<sub>Instance Property</sub>

A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var includeFaces: Bool { get set }
```

## Discussion

By default, the font picker only lists font families, like Times New Roman or Helvetica. Set [includeFaces](includefaces.md) to [true](../../../swift/true.md) so the user can select a specific font face, such as Times New Roman Bold or Helvetica Light Oblique.

## See Also

### Filtering available fonts

- [filteredTraits](filteredtraits.md) — A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [filteredLanguagesPredicate](filteredlanguagespredicate.md) — A predicate to filter fonts based on the languages they support. _(deprecated)_
- [+ filterPredicateForFilteredLanguages:](<filterpredicate(forfilteredlanguages_).md>) — Creates a font picker filter based on language support. _(deprecated)_
