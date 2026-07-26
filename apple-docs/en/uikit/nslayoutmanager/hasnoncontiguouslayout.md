---
title: hasNonContiguousLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/hasnoncontiguouslayout
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/hasnoncontiguouslayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/hasnoncontiguouslayout.json'
content_hash: 'sha256:c60c674d64de624e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# hasNonContiguousLayout

<sub>Instance Property</sub>

A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hasNonContiguousLayout: Bool { get }
```

## Discussion

There may be times at which there is no noncontiguous layout, such as when layout is complete; this method enables the layout manager to report that to clients.

For more information about noncontiguous layout, see [Noncontiguous Layout](../nslayoutmanager.md#Noncontiguous-Layout).

## See Also

### Configuring the global layout manager options

- [allowsNonContiguousLayout](allowsnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [showsInvisibleCharacters](showsinvisiblecharacters.md) — A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [showsControlCharacters](showscontrolcharacters.md) — A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [usesFontLeading](usesfontleading.md) — A Boolean value that indicates whether the layout manager uses the leading of the font.
- [backgroundLayoutEnabled](../../appkit/nslayoutmanager/backgroundlayoutenabled.md) — A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [limitsLayoutForSuspiciousContents](limitslayoutforsuspiciouscontents.md) — A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.
