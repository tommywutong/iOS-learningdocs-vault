---
title: titleEdgeInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/titleedgeinsets
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/titleedgeinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/titleedgeinsets.json'
content_hash: 'sha256:48ca0d73b1aceb96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# titleEdgeInsets

<sub>Instance Property</sub>

The inset or outset margins for the rectangle around the button’s title text.

> [!warning] Deprecated
> The system ignores this when you use [Configuration](configuration-swift.struct.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titleEdgeInsets: UIEdgeInsets { get set }
```

## Discussion

Use this property to resize and reposition the effective drawing rectangle for the button title. You can specify a different value for each of the four insets (top, left, bottom, right). A positive value shrinks, or insets, that edge—moving it closer to the center of the button. A negative value expands, or outsets, that edge. Use the [UIEdgeInsetsMake](<../uiedgeinsets/init(top_left_bottom_right_)-1s1t9.md>) function to construct a value for this property. The default value is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

The insets you specify are applied to the title rectangle after that rectangle has been sized to fit the button’s text. Thus, positive inset values may actually clip the title text.

This property is used only for positioning the title during layout. The button does not use this property to determine [intrinsicContentSize](../uiview/intrinsiccontentsize.md) and [- sizeThatFits:](<../uiview/sizethatfits(__).md>).

## See Also

### Edge insets

- [contentEdgeInsets](contentedgeinsets.md) — The inset or outset margins for the rectangle surrounding all of the button’s content. _(deprecated)_
- [imageEdgeInsets](imageedgeinsets.md) — The inset or outset margins for the rectangle around the button’s image. _(deprecated)_
