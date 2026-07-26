---
title: titleShadowOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/titleshadowoffset
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/titleshadowoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/titleshadowoffset.json'
content_hash: 'sha256:ddf872a87e8a735e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# titleShadowOffset

<sub>Instance Property</sub>

The offset of the shadow used to display the receiver’s title.

> [!warning] Deprecated
> Use the `shadowOffset` property of the [titleLabel](titlelabel.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGSize titleShadowOffset;
```

## Discussion

The horizontal and vertical offset values, specified using the `width` and `height` fields of the `CGSize` data type. Positive values always extend up and to the right from the user’s perspective. The default value is [CGSizeZero](../../coregraphics/cgsizezero.md).

## See Also

### Related Documentation

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.

### Title effects

- [font](font.md) — The font used to display text on the button. _(deprecated)_
- [lineBreakMode](linebreakmode.md) — The line break mode to use when drawing text. _(deprecated)_
- [reversesTitleShadowWhenHighlighted](reversestitleshadowwhenhighlighted.md) — A Boolean value that determines whether the title shadow changes when the button is highlighted. _(deprecated)_
