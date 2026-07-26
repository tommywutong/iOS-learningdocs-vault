---
title: 'titleRect(forContentRect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uibutton/titlerect(forcontentrect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/titlerect(forcontentrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/titlerect%28forcontentrect%3A%29.json'
content_hash: 'sha256:15e4324fdda3027a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# titleRect(forContentRect:)

<sub>Instance Method</sub>

Returns the rectangle in which the receiver draws its title.

> [!warning] Deprecated
> Use [- layoutSubviews](<../uiview/layoutsubviews().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titleRect(forContentRect contentRect: CGRect) -> CGRect
```

## Parameters

- `contentRect` — The content rectangle for the receiver.

## Return Value

The rectangle in which the receiver draws its title.

## See Also

### Dimensions

- [- backgroundRectForBounds:](<backgroundrect(forbounds_).md>) — Returns the rectangle in which the receiver draws its background. _(deprecated)_
- [- contentRectForBounds:](<contentrect(forbounds_).md>) — Returns the rectangle in which the receiver draws its entire content. _(deprecated)_
- [- imageRectForContentRect:](<imagerect(forcontentrect_).md>) — Returns the rectangle in which the receiver draws its image. _(deprecated)_
