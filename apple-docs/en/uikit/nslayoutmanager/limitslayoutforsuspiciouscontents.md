---
title: limitsLayoutForSuspiciousContents
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/limitslayoutforsuspiciouscontents
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/limitslayoutforsuspiciouscontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/limitslayoutforsuspiciouscontents.json'
content_hash: 'sha256:9f6e9d4e15ed9113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# limitsLayoutForSuspiciousContents

<sub>Instance Property</sub>

A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var limitsLayoutForSuspiciousContents: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md), which causes the layout manager to lay out whatever text you give it. Changing the value to [true](../../swift/true.md) causes the layout manager to generate invalid layout information when it detects potentially suspicious content.

## See Also

### Configuring the global layout manager options

- [allowsNonContiguousLayout](allowsnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [hasNonContiguousLayout](hasnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [showsInvisibleCharacters](showsinvisiblecharacters.md) — A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [showsControlCharacters](showscontrolcharacters.md) — A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [usesFontLeading](usesfontleading.md) — A Boolean value that indicates whether the layout manager uses the leading of the font.
- [backgroundLayoutEnabled](../../appkit/nslayoutmanager/backgroundlayoutenabled.md) — A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [usesDefaultHyphenation](usesdefaulthyphenation.md) — A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.
