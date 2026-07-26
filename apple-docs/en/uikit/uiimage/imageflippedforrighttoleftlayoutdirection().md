---
title: imageFlippedForRightToLeftLayoutDirection()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/imageflippedforrighttoleftlayoutdirection()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/imageflippedforrighttoleftlayoutdirection()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/imageflippedforrighttoleftlayoutdirection%28%29.json'
content_hash: 'sha256:4bf310f7913bc21a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# imageFlippedForRightToLeftLayoutDirection()

<sub>Instance Method</sub>

Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func imageFlippedForRightToLeftLayoutDirection() -> UIImage
```

## Return Value

The current image, prepared to flip horizontally if it’s in a right-to-left layout.

## Discussion

Use this method to specify an image that should flip in a right-to-left layout. Note that most images do not need to flip in a right-to-left layout.

This method returns the current [UIImage](../uiimage.md) object with the [flipsForRightToLeftLayoutDirection](flipsforrighttoleftlayoutdirection.md) property set to [true](../../swift/true.md); it does _not_ return a flipped image. When the returned image is displayed in a [UIImageView](../uiimageview.md) object in a right-to-left layout direction (whether the layout direction is set by the system language, or because the image view’s [semanticContentAttribute](../uiview/semanticcontentattribute.md) property is set to [UISemanticContentAttributeForceRightToLeft](../uisemanticcontentattribute/forcerighttoleft.md)), the image appears flipped. When the returned image is displayed in a left-to-right context, it appears unflipped.

## See Also

### Changing the image attributes

- [- imageWithConfiguration:](<withconfiguration(__).md>) — Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [- imageByApplyingSymbolConfiguration:](<applyingsymbolconfiguration(__).md>) — Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [- imageWithHorizontallyFlippedOrientation](<withhorizontallyflippedorientation().md>) — Returns a new version of the image that’s a mirror of the original image.
- [- imageWithRenderingMode:](<withrenderingmode(__).md>) — Returns a new version of the image that uses the specified rendering mode.
- [- imageWithAlignmentRectInsets:](<withalignmentrectinsets(__).md>) — Returns a new version of the image that uses the specified alignment insets.
- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.
- [- imageWithoutBaseline](<imagewithoutbaseline().md>) — Creates a copy of the current image object without any baseline information.
- [- imageWithBaselineOffsetFromBottom:](<withbaselineoffset(frombottom_).md>) — Creates a new image with a baseline at the specified offset from the bottom of the image.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
