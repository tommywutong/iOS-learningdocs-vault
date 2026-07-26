---
title: 'init(image:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimageview/init(image:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/init(image:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/init%28image%3A%29.json'
content_hash: 'sha256:c65fbcad65096d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# init(image:)

<sub>Initializer</sub>

Returns an image view initialized with the specified image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(image: UIImage?)
```

## Parameters

- `image` — The initial image to display in the image view. You may specify an image object that contains an animated sequence of images.

## Return Value

An initialized image view object.

## Discussion

The image you specified is used to configure the initial size of the image view itself. Use constraints and the image view’s content mode to adjust the image view’s final size onscreen. This method disables user interactions for the image view by setting the [userInteractionEnabled](isuserinteractionenabled.md) property to [false](../../swift/false.md).

If you specify an animated image whose duration is greater than `0`, the image view automatically starts playing the animation.

## See Also

### Creating an image view

- [- initWithImage:highlightedImage:](<init(image_highlightedimage_).md>) — Returns an image view initialized with the specified regular and highlighted images.
