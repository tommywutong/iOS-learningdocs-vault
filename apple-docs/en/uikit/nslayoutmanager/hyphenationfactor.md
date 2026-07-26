---
title: hyphenationFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nslayoutmanager/hyphenationfactor
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/hyphenationfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/hyphenationfactor.json'
content_hash: 'sha256:55a57e231d219755'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# hyphenationFactor

<sub>Instance Property</sub>

The threshold controlling when hyphenation is done.

> [!warning] Deprecated
> Use [usesDefaultHyphenation](usesdefaulthyphenation.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var hyphenationFactor: CGFloat { get set }
```

## Discussion

Whenever (width of the real contents of the line) / (the line fragment width) is below `factor`, hyphenation is attempted when laying out the line. Hyphenation slows down text layout and increases memory usage, so it should be used sparingly.

## See Also

### Properties

- [attributedString](../nslayoutmanager-attributedstring.md) — The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
- [layoutOptions](../nslayoutmanager-layoutoptions.md) — The layout manager’s current layout options.
- [usesScreenFonts](../../appkit/nslayoutmanager/usesscreenfonts.md) — A Boolean that controls using screen fonts to calculate layout and display text. _(deprecated)_
