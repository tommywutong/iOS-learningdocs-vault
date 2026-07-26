---
title: 'backgroundRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uibutton/backgroundrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/backgroundrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/backgroundrect%28forbounds%3A%29.json'
content_hash: 'sha256:36c9368f0e6918d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# backgroundRect(forBounds:)

<sub>Instance Method</sub>

Returns the rectangle in which the receiver draws its background.

> [!warning] Deprecated
> Use [- layoutSubviews](<../uiview/layoutsubviews().md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The bounds rectangle in which to draw any standard button content.

## Discussion

The default implementation of this method returns the value in the `bounds` parameter. This rectangle represents the area in which the button draws its standard background content. Subclasses that provide custom background adornments can override this method and return a modified bounds rectangle to prevent the button from drawing over any custom content.

## See Also

### Dimensions

- [- contentRectForBounds:](<contentrect(forbounds_).md>) — Returns the rectangle in which the receiver draws its entire content. _(deprecated)_
- [- titleRectForContentRect:](<titlerect(forcontentrect_).md>) — Returns the rectangle in which the receiver draws its title. _(deprecated)_
- [- imageRectForContentRect:](<imagerect(forcontentrect_).md>) — Returns the rectangle in which the receiver draws its image. _(deprecated)_
