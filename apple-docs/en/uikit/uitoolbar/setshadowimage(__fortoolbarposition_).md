---
title: 'setShadowImage(_:forToolbarPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitoolbar/setshadowimage(_:fortoolbarposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/setshadowimage(_:fortoolbarposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/setshadowimage%28_%3Afortoolbarposition%3A%29.json'
content_hash: 'sha256:5a77cae179c51141'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# setShadowImage(_:forToolbarPosition:)

<sub>Instance Method</sub>

Sets the image to use for the toolbar shadow in a given position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setShadowImage(_ shadowImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition)
```

## Parameters

- `shadowImage` — The image to use for the toolbar shadow in the position specified by `topOrBottom`.

- `topOrBottom` — A toolbar position constant. You can use this parameter to indicate whether the `shadowImage` is intended for a toolbar at the top or bottom of the view.

## Discussion

When the `shadowImage` parameter is `nil`, the default shadow will be used. When non-`nil`, the `shadowImage` property is a custom shadow image to show instead of the default. Using the `topOrBottom` parameter, you can set a different shadow for toolbars at the top and bottom of the view. For a custom shadow image to be shown, a custom background image must also be set with the [- setBackgroundImage:forToolbarPosition:barMetrics:](<setbackgroundimage(__fortoolbarposition_barmetrics_).md>) method. If the default background image is used, then the default shadow image will be used regardless of the value of the `shadowImage` parameter.

## See Also

### Adding a shadow

- [- shadowImageForToolbarPosition:](<shadowimage(fortoolbarposition_).md>) — Returns the image to use for the toolbar shadow in a given position.
