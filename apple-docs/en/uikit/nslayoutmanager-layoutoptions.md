---
title: layoutOptions
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-layoutoptions
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-layoutoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-layoutoptions.json'
content_hash: 'sha256:4637384f3b0bf0c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md) · [Deprecated symbols](nslayoutmanager-deprecated-symbols.md)

# layoutOptions

<sub>Article</sub>

The layout manager’s current layout options.

## Overview

**Swift**

```swift
var layoutOptions: Int { get }
```

**Objective-C**

```objc
@property(readonly) NSUInteger layoutOptions
```

This property is part of the `NSGlyphStorage` protocol, for use by the glyph generator. It enables the glyph generator to ask which options the layout manager requests.

## See Also

### Properties

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — The threshold controlling when hyphenation is done. _(deprecated)_
- [attributedString](nslayoutmanager-attributedstring.md) — The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — A Boolean that controls using screen fonts to calculate layout and display text. _(deprecated)_
