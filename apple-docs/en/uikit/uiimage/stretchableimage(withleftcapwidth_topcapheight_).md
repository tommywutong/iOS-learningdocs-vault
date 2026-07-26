---
title: 'stretchableImage(withLeftCapWidth:topCapHeight:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiimage/stretchableimage(withleftcapwidth:topcapheight:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/stretchableimage(withleftcapwidth:topcapheight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/stretchableimage%28withleftcapwidth%3Atopcapheight%3A%29.json'
content_hash: 'sha256:e1a8a4839ede8e0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# stretchableImage(withLeftCapWidth:topCapHeight:)

<sub>Instance Method</sub>

Creates and returns a new image object with the specified cap values.

> [!warning] Deprecated
> Use the [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) instead, specifying cap insets such that the interior is a `1x1` area.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
func stretchableImage(withLeftCapWidth leftCapWidth: Int, topCapHeight: Int) -> UIImage
```

## Parameters

- `leftCapWidth` — The value to use for the left cap width. Specify `0` if you want the entire image to be horizontally stretchable. For a discussion of how a non-zero value affects the image, see the [leftCapWidth](leftcapwidth.md) property.

- `topCapHeight` — The value to use for the top cap height. Specify `0` if you want the entire image to be vertically stretchable. For a discussion of how a non-zero value affects the image, see the [topCapHeight](topcapheight.md) property.

## Return Value

A new image object with the specified cap values.

## Discussion

During scaling or resizing of the image, areas covered by a cap are not scaled or resized. Instead, the 1-pixel wide area not covered by the cap in each direction is what is scaled or resized. This technique is often used to create variable-width buttons, which retain the same rounded corners but whose center region grows or shrinks as needed.

You use this method to add cap values to an image or to change the existing cap values of an image. In both cases, you get back a new image and the original image remains untouched.

## See Also

### Deprecated

- [leftCapWidth](leftcapwidth.md) — The horizontal end-cap size. _(deprecated)_
- [topCapHeight](topcapheight.md) — The vertical end-cap size. _(deprecated)_
