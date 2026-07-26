---
title: 'withConfiguration(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/withconfiguration(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/withconfiguration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/withconfiguration%28_%3A%29.json'
content_hash: 'sha256:3285b58432a87b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# withConfiguration(_:)

<sub>Instance Method</sub>

Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withConfiguration(_ configuration: UIImage.Configuration) -> UIImage
```

## Parameters

- `configuration` — The new configuration attributes to associate with the image.

## Return Value

A new version of the image object that contains the specified configuration details.

## Discussion

This method creates a new image object, replacing the image’s current configuration with the values specified in the `configuration` parameter.

## See Also

### Changing the image attributes

- [- imageByApplyingSymbolConfiguration:](<applyingsymbolconfiguration(__).md>) — Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [- imageFlippedForRightToLeftLayoutDirection](<imageflippedforrighttoleftlayoutdirection().md>) — Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [- imageWithHorizontallyFlippedOrientation](<withhorizontallyflippedorientation().md>) — Returns a new version of the image that’s a mirror of the original image.
- [- imageWithRenderingMode:](<withrenderingmode(__).md>) — Returns a new version of the image that uses the specified rendering mode.
- [- imageWithAlignmentRectInsets:](<withalignmentrectinsets(__).md>) — Returns a new version of the image that uses the specified alignment insets.
- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.
- [- imageWithoutBaseline](<imagewithoutbaseline().md>) — Creates a copy of the current image object without any baseline information.
- [- imageWithBaselineOffsetFromBottom:](<withbaselineoffset(frombottom_).md>) — Creates a new image with a baseline at the specified offset from the bottom of the image.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
