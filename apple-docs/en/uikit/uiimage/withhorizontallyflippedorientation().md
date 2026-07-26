---
title: withHorizontallyFlippedOrientation()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/withhorizontallyflippedorientation()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/withhorizontallyflippedorientation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/withhorizontallyflippedorientation%28%29.json'
content_hash: 'sha256:8310546eea42b058'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# withHorizontallyFlippedOrientation()

<sub>Instance Method</sub>

Returns a new version of the image that’s a mirror of the original image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withHorizontallyFlippedOrientation() -> UIImage
```

## Return Value

The new [UIImage](../uiimage.md) object.

## Discussion

The returned image’s [imageOrientation](imageorientation.md) property contains the mirrored version of the original image’s orientation. For example, if the original orientation is [UIImageOrientationLeft](orientation/left.md), the new orientation is [UIImageOrientationLeftMirrored](orientation/leftmirrored.md). This method does not affect the value of the [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) property.

## See Also

### Changing the image attributes

- [- imageWithConfiguration:](<withconfiguration(__).md>) — Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [- imageByApplyingSymbolConfiguration:](<applyingsymbolconfiguration(__).md>) — Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [- imageFlippedForRightToLeftLayoutDirection](<imageflippedforrighttoleftlayoutdirection().md>) — Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [- imageWithRenderingMode:](<withrenderingmode(__).md>) — Returns a new version of the image that uses the specified rendering mode.
- [- imageWithAlignmentRectInsets:](<withalignmentrectinsets(__).md>) — Returns a new version of the image that uses the specified alignment insets.
- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.
- [- imageWithoutBaseline](<imagewithoutbaseline().md>) — Creates a copy of the current image object without any baseline information.
- [- imageWithBaselineOffsetFromBottom:](<withbaselineoffset(frombottom_).md>) — Creates a new image with a baseline at the specified offset from the bottom of the image.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
