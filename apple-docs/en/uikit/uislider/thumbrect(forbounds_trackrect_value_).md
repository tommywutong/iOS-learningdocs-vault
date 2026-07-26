---
title: 'thumbRect(forBounds:trackRect:value:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/thumbrect(forbounds:trackrect:value:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/thumbrect(forbounds:trackrect:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/thumbrect%28forbounds%3Atrackrect%3Avalue%3A%29.json'
content_hash: 'sha256:495c9c5854359dff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# thumbRect(forBounds:trackRect:value:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the slider’s thumb image.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func thumbRect(forBounds bounds: CGRect, trackRect rect: CGRect, value: Float) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the slider.

- `rect` — The drawing rectangle for the slider’s track, as returned by the [- trackRectForBounds:](<trackrect(forbounds_).md>) method.

- `value` — The current value of the slider.

## Return Value

The computed drawing rectangle for the thumb image.

## Discussion

You do not call this method directly. Instead, you override it when you want to customize the thumb image’s drawing rectangle, returning a different rectangle. The rectangle you return must reflect the size of your thumb image and its current position on the slider’s track.

## See Also

### Overrides for subclasses

- [- maximumValueImageRectForBounds:](<maximumvalueimagerect(forbounds_).md>) — Returns the drawing rectangle for the maximum value image.
- [- minimumValueImageRectForBounds:](<minimumvalueimagerect(forbounds_).md>) — Returns the drawing rectangle for the minimum value image.
- [- trackRectForBounds:](<trackrect(forbounds_).md>) — Returns the drawing rectangle for the slider’s track.
