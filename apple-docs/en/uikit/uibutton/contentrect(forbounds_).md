---
title: 'contentRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uibutton/contentrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/contentrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/contentrect%28forbounds%3A%29.json'
content_hash: 'sha256:c057d3e70efe5902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# contentRect(forBounds:)

<sub>Instance Method</sub>

Returns the rectangle in which the receiver draws its entire content.

> [!warning] Deprecated
> Use [- layoutSubviews](<../uiview/layoutsubviews().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func contentRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle for the receiver.

## Return Value

The rectangle in which the receiver draws its entire content.

## Discussion

The content rectangle is the area needed to display the image and title including any padding and adjustments for alignment and other settings.

## See Also

### Related Documentation

- [contentEdgeInsets](contentedgeinsets.md) — The inset or outset margins for the rectangle surrounding all of the button’s content. _(deprecated)_

### Dimensions

- [- backgroundRectForBounds:](<backgroundrect(forbounds_).md>) — Returns the rectangle in which the receiver draws its background. _(deprecated)_
- [- titleRectForContentRect:](<titlerect(forcontentrect_).md>) — Returns the rectangle in which the receiver draws its title. _(deprecated)_
- [- imageRectForContentRect:](<imagerect(forcontentrect_).md>) — Returns the rectangle in which the receiver draws its image. _(deprecated)_
