---
title: 'withTintColor(_:renderingMode:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/withtintcolor(_:renderingmode:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/withtintcolor(_:renderingmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/withtintcolor%28_%3Arenderingmode%3A%29.json'
content_hash: 'sha256:a9d9085f750412ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# withTintColor(_:renderingMode:)

<sub>Instance Method</sub>

Returns a new version of the image with a tint color that uses the specified rendering mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withTintColor(_ color: UIColor, renderingMode: UIImage.RenderingMode) -> UIImage
```

## Parameters

- `color` — The tint color to apply to the image.

- `renderingMode` — The rendering mode to assign to the returned image.

## Return Value

A new version of the image that incorporates the specified tint color.

## Discussion

For bitmap images, this method draws the background tint color followed by the image contents using the [CGBlendMode.destinationIn](../../coregraphics/cgblendmode/destinationin.md) mode. For symbol images, this method returns an image that always uses the specified tint color.

## See Also

### Tinting the image

- [- imageWithTintColor:](<withtintcolor(__).md>) — Returns a new version of the current image with the specified tint color.
