---
title: backgroundLayoutEnabled
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/backgroundlayoutenabled
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/backgroundlayoutenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/backgroundlayoutenabled.json'
content_hash: 'sha256:6d21cbf9328c5c44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# backgroundLayoutEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.

<sub>macOS</sub>

```swift
var backgroundLayoutEnabled: Bool { get set }
```

## See Also

### Configuring the global layout manager options

- [allowsNonContiguousLayout](allowsnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [hasNonContiguousLayout](hasnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [showsInvisibleCharacters](showsinvisiblecharacters.md) — A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [showsControlCharacters](showscontrolcharacters.md) — A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [usesFontLeading](usesfontleading.md) — A Boolean value that indicates whether the layout manager uses the leading of the font.
- [limitsLayoutForSuspiciousContents](limitslayoutforsuspiciouscontents.md) — A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.
