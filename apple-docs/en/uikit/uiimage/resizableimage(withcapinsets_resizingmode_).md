---
title: 'resizableImage(withCapInsets:resizingMode:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/resizableimage(withcapinsets:resizingmode:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/resizableimage(withcapinsets:resizingmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/resizableimage%28withcapinsets%3Aresizingmode%3A%29.json'
content_hash: 'sha256:53478b0fad5f2d18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# resizableImage(withCapInsets:resizingMode:)

<sub>Instance Method</sub>

Returns a new version of the image with the specified cap insets and options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func resizableImage(withCapInsets capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage
```

## Parameters

- `capInsets` — The values to use for the cap insets.

- `resizingMode` — The mode with which the interior of the image is resized.

## Return Value

A new image object with the specified cap insets and resizing mode.

## Discussion

This method is exactly the same as its counterpart [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) except that the resizing mode of the new image object can be explicitly declared. You should only call this method in place of its counterpart if you specifically want your image to be resized with the [UIImageResizingModeStretch](resizingmode-swift.enum/stretch.md) resizing mode.

## See Also

### Changing the image attributes

- [- imageWithConfiguration:](<withconfiguration(__).md>) — Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [- imageByApplyingSymbolConfiguration:](<applyingsymbolconfiguration(__).md>) — Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [- imageFlippedForRightToLeftLayoutDirection](<imageflippedforrighttoleftlayoutdirection().md>) — Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [- imageWithHorizontallyFlippedOrientation](<withhorizontallyflippedorientation().md>) — Returns a new version of the image that’s a mirror of the original image.
- [- imageWithRenderingMode:](<withrenderingmode(__).md>) — Returns a new version of the image that uses the specified rendering mode.
- [- imageWithAlignmentRectInsets:](<withalignmentrectinsets(__).md>) — Returns a new version of the image that uses the specified alignment insets.
- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- imageWithoutBaseline](<imagewithoutbaseline().md>) — Creates a copy of the current image object without any baseline information.
- [- imageWithBaselineOffsetFromBottom:](<withbaselineoffset(frombottom_).md>) — Creates a new image with a baseline at the specified offset from the bottom of the image.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
