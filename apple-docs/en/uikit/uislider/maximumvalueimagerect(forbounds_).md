---
title: 'maximumValueImageRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/maximumvalueimagerect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/maximumvalueimagerect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/maximumvalueimagerect%28forbounds%3A%29.json'
content_hash: 'sha256:884d4a41175dee11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# maximumValueImageRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the maximum value image.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func maximumValueImageRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the slider.

## Return Value

The computed drawing rectangle for the image.

## Discussion

You do not call this method directly. Instead, you override it when you want to customize the rectangle in which the maximum value image is drawn, returning a different rectangle. If you make x-axis adjustments, be sure to take into account the automatic flipping of [maximumValueImage](maximumvalueimage.md) in a right-to-left user interface; the maximum image is always shown at the trailing end of the slider’s track. See the [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for further information about supporting right-to-left languages.

## See Also

### Overrides for subclasses

- [- minimumValueImageRectForBounds:](<minimumvalueimagerect(forbounds_).md>) — Returns the drawing rectangle for the minimum value image.
- [- trackRectForBounds:](<trackrect(forbounds_).md>) — Returns the drawing rectangle for the slider’s track.
- [- thumbRectForBounds:trackRect:value:](<thumbrect(forbounds_trackrect_value_).md>) — Returns the drawing rectangle for the slider’s thumb image.
