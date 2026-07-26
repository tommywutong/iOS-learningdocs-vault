---
title: attributedString
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-attributedstring
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-attributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-attributedstring.json'
content_hash: 'sha256:9b44b0eedf1c089a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md) · [Deprecated symbols](nslayoutmanager-deprecated-symbols.md)

# attributedString

<sub>Article</sub>

The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.

## Overview

**Swift**

```swift
var attributedString: NSAttributedString? { get }
```

**Objective-C**

```objc
@property(readonly, strong) NSAttributedString *attributedString
```

This property is part of the `NSGlyphStorage` protocol, for use by the glyph generator. For `NSLayoutManager` the attributed string is equivalent to the text storage.

## See Also

### Properties

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — The threshold controlling when hyphenation is done. _(deprecated)_
- [layoutOptions](nslayoutmanager-layoutoptions.md) — The layout manager’s current layout options.
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — A Boolean that controls using screen fonts to calculate layout and display text. _(deprecated)_
