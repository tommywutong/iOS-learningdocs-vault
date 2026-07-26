---
title: 'withTintColor(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/withtintcolor(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/withtintcolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/withtintcolor%28_%3A%29.json'
content_hash: 'sha256:d053359d2e7f93b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# withTintColor(_:)

<sub>Instance Method</sub>

Returns a new version of the current image with the specified tint color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withTintColor(_ color: UIColor) -> UIImage
```

## Parameters

- `color` — The tint color to apply to the image.

## Return Value

A new version of the image that incorporates the specified tint color.

## Discussion

For bitmap images, this method draws the background tint color followed by the image contents using the [CGBlendMode.destinationIn](../../coregraphics/cgblendmode/destinationin.md) mode. For symbol images, this method returns an image that always uses the specified tint color.

The new image uses the same rendering mode as the original image.

## See Also

### Tinting the image

- [- imageWithTintColor:renderingMode:](<withtintcolor(__renderingmode_).md>) — Returns a new version of the image with a tint color that uses the specified rendering mode.
