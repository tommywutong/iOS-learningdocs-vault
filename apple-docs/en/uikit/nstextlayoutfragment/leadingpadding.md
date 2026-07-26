---
title: leadingPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/leadingpadding
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/leadingpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/leadingpadding.json'
content_hash: 'sha256:962b4d1f511634c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# leadingPadding

<sub>Instance Property</sub>

The amount of margin space reserved during paragraph layout between the leading edge of the text layout fragment and the start of the lines in the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leadingPadding: CGFloat { get }
```

## Discussion

This is with respect to according to the primary writing direction of the paragraph and the start of the lines in the paragraph.

## See Also

### Defining margins and padding

- [bottomMargin](bottommargin.md) — The amount of space reserved during paragraph layout between the bottom of the last line in the paragraph and the bottom of the text layout fragment.
- [topMargin](topmargin.md) — The amount of space reserved during paragraph layout between the top of the text layout fragment and the top of the first line in the paragraph.
- [trailingPadding](trailingpadding.md) — The amount of margin space reserved during paragraph layout between the end of the lines in the paragraph and the trailing edge of the text layout fragment.
