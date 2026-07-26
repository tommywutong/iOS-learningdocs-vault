---
title: showsControlCharacters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/showscontrolcharacters
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/showscontrolcharacters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/showscontrolcharacters.json'
content_hash: 'sha256:93c81cf666f0e96b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# showsControlCharacters

<sub>Instance Property</sub>

A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsControlCharacters: Bool { get set }
```

## See Also

### Configuring the global layout manager options

- [allowsNonContiguousLayout](allowsnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [hasNonContiguousLayout](hasnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [showsInvisibleCharacters](showsinvisiblecharacters.md) — A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [usesFontLeading](usesfontleading.md) — A Boolean value that indicates whether the layout manager uses the leading of the font.
- [backgroundLayoutEnabled](../../appkit/nslayoutmanager/backgroundlayoutenabled.md) — A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [limitsLayoutForSuspiciousContents](limitslayoutforsuspiciouscontents.md) — A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.
