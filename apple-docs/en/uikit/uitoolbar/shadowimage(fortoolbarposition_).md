---
title: 'shadowImage(forToolbarPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitoolbar/shadowimage(fortoolbarposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/shadowimage(fortoolbarposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/shadowimage%28fortoolbarposition%3A%29.json'
content_hash: 'sha256:12f5e4801be3ad8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# shadowImage(forToolbarPosition:)

<sub>Instance Method</sub>

Returns the image to use for the toolbar shadow in a given position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func shadowImage(forToolbarPosition topOrBottom: UIBarPosition) -> UIImage?
```

## Parameters

- `topOrBottom` — A toolbar position constant. You can use this parameter to indicate whether the shadow image returned is intended for use in a toolbar at the top or bottom of the view.

## Return Value

The image to use for the toolbar shadow in the position specified by `topOrBottom`.

## Discussion

The default value is `nil`, which corresponds to the default shadow image being used. When non-`nil`, the return value represents the shadow that is used on the toolbar in the position specified by the `topOrBottom` parameter.

## See Also

### Adding a shadow

- [- setShadowImage:forToolbarPosition:](<setshadowimage(__fortoolbarposition_).md>) — Sets the image to use for the toolbar shadow in a given position.
