---
title: 'withBaselineOffset(fromBottom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/withbaselineoffset(frombottom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/withbaselineoffset(frombottom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/withbaselineoffset%28frombottom%3A%29.json'
content_hash: 'sha256:165f9f224408d454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# withBaselineOffset(fromBottom:)

<sub>Instance Method</sub>

Creates a new image with a baseline at the specified offset from the bottom of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withBaselineOffset(fromBottom baselineOffset: CGFloat) -> UIImage
```

## Parameters

- `baselineOffset` — The position of the baseline, relative to the bottom of the image. Specify this value in points, where positive values move the baseline up from the bottom of the image and negative values move the baseline down.

## Return Value

A new image object containing the baseline information.

## Discussion

Use this method to create an image with the specified baseline information. You might add a baseline to your custom images so that you can incorporate them into text-based layouts. You can also use this method to change the baseline information on an image.

## See Also

### Changing the image attributes

- [- imageWithConfiguration:](<withconfiguration(__).md>) — Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [- imageByApplyingSymbolConfiguration:](<applyingsymbolconfiguration(__).md>) — Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [- imageFlippedForRightToLeftLayoutDirection](<imageflippedforrighttoleftlayoutdirection().md>) — Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [- imageWithHorizontallyFlippedOrientation](<withhorizontallyflippedorientation().md>) — Returns a new version of the image that’s a mirror of the original image.
- [- imageWithRenderingMode:](<withrenderingmode(__).md>) — Returns a new version of the image that uses the specified rendering mode.
- [- imageWithAlignmentRectInsets:](<withalignmentrectinsets(__).md>) — Returns a new version of the image that uses the specified alignment insets.
- [- resizableImageWithCapInsets:](<resizableimage(withcapinsets_).md>) — Returns a new version of the image with the specified cap insets.
- [- resizableImageWithCapInsets:resizingMode:](<resizableimage(withcapinsets_resizingmode_).md>) — Returns a new version of the image with the specified cap insets and options.
- [- imageWithoutBaseline](<imagewithoutbaseline().md>) — Creates a copy of the current image object without any baseline information.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
- [SymbolConfiguration](symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
