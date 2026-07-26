---
title: 'init(container:center:transform:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewtarget/init(container:center:transform:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewtarget/init(container:center:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewtarget/init%28container%3Acenter%3Atransform%3A%29.json'
content_hash: 'sha256:02a84595820a9c03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewTarget](../uipreviewtarget.md)

# init(container:center:transform:)

<sub>Initializer</sub>

Creates a preview target object using the specified container view and configuration details.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(container: UIView, center: CGPoint, transform: CGAffineTransform)
```

## Parameters

- `container` — The container for the view being animated. This view must be in a window.

- `center` — The point in `container` at which to place the center of the view being animated. Specify this point in the coordinate system of `container`.

- `transform` — An affine transform to apply to the view being animated. You might use this transform to scale or rotate the view.

## Return Value

A new preview target object with the specified container and configuration data.

## See Also

### Creating a preview target object

- [- initWithContainer:center:](<init(container_center_).md>) — Creates a preview target object using the specified container view and center point.
