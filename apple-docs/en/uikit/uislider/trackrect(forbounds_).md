---
title: 'trackRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/trackrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/trackrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/trackrect%28forbounds%3A%29.json'
content_hash: 'sha256:3207e25ebaee40a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# trackRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the slider’s track.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func trackRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the slider.

## Return Value

The computed drawing rectangle for the track. This rectangle corresponds to the entire length of the track between the minimum and maximum value images.

## Discussion

You do not call this method directly. Instead, you override it when you want to customize the track rectangle, returning a different rectangle. The returned rectangle is used to scale the track and thumb images during drawing.

## See Also

### Overrides for subclasses

- [- maximumValueImageRectForBounds:](<maximumvalueimagerect(forbounds_).md>) — Returns the drawing rectangle for the maximum value image.
- [- minimumValueImageRectForBounds:](<minimumvalueimagerect(forbounds_).md>) — Returns the drawing rectangle for the minimum value image.
- [- thumbRectForBounds:trackRect:value:](<thumbrect(forbounds_trackrect_value_).md>) — Returns the drawing rectangle for the slider’s thumb image.
