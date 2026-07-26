---
title: UIImageView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview.json'
content_hash: 'sha256:88d40f6d3e656cc9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImageView

<sub>Class</sub>

A view that displays a single image or a sequence of animated images in your interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIImageView
```

## Overview

Image views let you efficiently draw any image that can be specified using a [UIImage](uiimage.md) object. For example, you can use the [UIImageView](uiimageview.md) class to display the contents of many standard image files, such as JPEG and PNG files. You can configure image views programmatically or in your storyboard file and change the images they display at runtime. For animated images, you can also use the methods of this class to start and stop the animation and specify other animation parameters.

![An image view](../../../attachments/707440cc50954c46cf2c38fbab7cd76b/media-2923882@2x.png)

### Understand how images are scaled

An image view uses its [contentMode](uiview/contentmode-swift.property.md) property and the configuration of the image itself to determine how to display the image. It’s best to specify images whose dimensions match the dimensions of the image view exactly, but image views can scale your images to fit all or some of the available space. If the size of the image view itself changes, it automatically scales the image as needed.

For an image without cap insets, the presentation of the image is determined solely by the image view’s [contentMode](uiview/contentmode-swift.property.md) property. The [UIViewContentModeScaleAspectFit](uiview/contentmode-swift.enum/scaleaspectfit.md) and [UIViewContentModeScaleAspectFill](uiview/contentmode-swift.enum/scaleaspectfill.md) modes scale the image to fit or fill the space while maintaining the image’s original aspect ratio. The [UIViewContentModeScaleToFill](uiview/contentmode-swift.enum/scaletofill.md) value scales the image without regard to the original aspect ratio, which can cause the image to appear distorted. Other content modes place the image at the appropriate location in the image view’s bounds without scaling it.

For a resizable image with cap insets, those insets affect the final appearance of the image. Specifically, cap insets define which parts of the image may be scaled and in which directions. You can create a resizable image that stretches using the [- resizableImageWithCapInsets:resizingMode:](<uiimage/resizableimage(withcapinsets_resizingmode_).md>) method of [UIImage](uiimage.md). When using an image of this type, you typically set the image view’s content mode to [UIViewContentModeScaleToFill](uiview/contentmode-swift.enum/scaletofill.md) so that the image stretches in the appropriate places and fills the image view’s bounds.

For tips on how to prepare images, see [Debug issues with your image view](uiimageview.md#Debug-issues-with-your-image-view). For more information on creating resizable images with cap insets, see [UIImage](uiimage.md).

### Determine the final transparency of the image

Images are composited onto the image view’s background and are then composited into the rest of the window. Any transparency in the image allows the image view’s background to show through. Similarly, any further transparency in the background of the image is dependent on the transparency of the image view and the transparency of the [UIImage](uiimage.md) object it displays. When the image view and its image both have transparency, the image view uses alpha blending to combine the two.

- The image is composited onto the image view’s background.
- If the image view’s [opaque](uiview/isopaque.md) property is [true](../swift/true.md), the image’s pixels are composited on top of the image view’s background color and the [alpha](uiview/alpha.md) property of the image view is ignored.
- If the image view’s [opaque](uiview/isopaque.md) property is [false](../swift/false.md), the alpha value of each pixel is multiplied by the image view’s [alpha](uiview/alpha.md) value, with the resulting value becoming the actual transparency value for that pixel. If the image doesn’t have an alpha channel, the alpha value of each pixel is assumed to be `1.0`.

> [!important] Important
> It’s computationally expensive to composite the alpha channel of an image with the alpha channel of a non-opaque image view. The performance impact is further magnified if you use Core Animation shadows, because the shape of the shadow is then based on the contents of the view and must be dynamically computed. If you aren’t intentionally using the alpha channel of the image or the alpha channel of the image view, set the [opaque](uiview/isopaque.md) property to [true](../swift/true.md) to improve performance. For additional optimization tips, see [Improve performance](uiimageview.md#Improve-performance).

### Animate a sequence of images

An image view can store an animated image sequence and play all or part of that sequence. You specify an image sequence as an array of [UIImage](uiimage.md) objects and assign them to the [animationImages](uiimageview/animationimages.md) property. Once assigned, you can use the methods and properties of this class to configure the animation timing and to start and stop the animation.

> [!note] Note
> You can also construct a single [UIImage](uiimage.md) object from a sequence of individual images using the [+ animatedImageWithImages:duration:](<uiimage/animatedimage(with_duration_).md>) method. Doing so yields the same results as assigning the individual images to the [animationImages](uiimageview/animationimages.md) property.

Consider the following tips when displaying a sequence of animated images:

- **All images in the sequence should have the same size.** When scaling is required, the image view scales each image in the sequence separately. If the images are different sizes, scaling may not yield the results you want.
- **All images in the sequence should use the same content scale factor.** Make sure the [scale](uiimage/scale.md) property of each image contains the same value.

### Respond to touch events

Image views ignore user events by default. Normally, you use image views only to present visual content in your interface. If you want an image view to handle user interactions as well, change the value of its [userInteractionEnabled](uiimageview/isuserinteractionenabled.md) property to [true](../swift/true.md). After doing that, you can attach gesture recognizers or use any other event handling techniques to respond to touch events or other user-initiated events.

For more information about handling events, see [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

### Improve performance

Image scaling and alpha blending are two relatively expensive operations that can impact your app’s performance. To maximize performance of your image view code, consider the following tips:

- **Cache scaled versions of frequently used images.** If you expect certain large images to be displayed frequently in a scaled-down thumbnail view, consider creating the scaled-down images in advance and storing them in a thumbnail cache. Doing so alleviates the need for each image view to scale them separately.
- **Use images whose size is close to the size of the image view.** Rather than assigning a large image to an image view, created a scaled version that matches the current size of the image view. You can also create a resizable image object using the [UIImageResizingModeTile](uiimage/resizingmode-swift.enum/tile.md) option, which tiles the image instead of scaling it.
- **Make your image view opaque whenever possible.** Unless you’re intentionally working with images that contain transparency (drawing UI elements, for example), make sure the [opaque](uiview/isopaque.md) property of your image view is set to [true](../swift/true.md). For more information about how transparency is determined, see [Determine the final transparency of the image](uiimageview.md#Determine-the-final-transparency-of-the-image).

### Debug issues with your image view

If your image view isn’t displaying what you expected, use the following tips to help diagnose the problem:

- **Load images using the correct method.** Use the [+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) method of [UIImage](uiimage.md) to load images from asset catalogs or your app’s bundle. For images outside of your app’s bundle, use the [imageWithContentsOfFile:](uiimage/imagewithcontentsoffile_.md) method.
- **Don’t use image views for custom drawing.** The [UIImageView](uiimageview.md) class doesn’t draw its content using the [- drawRect:](<uiview/draw(__).md>) method. Use image views only to present images. To do custom drawing involving images, subclass [UIView](uiview.md) directly and draw your image there.

### Interface Builder attributes

The following table lists the attributes that you configure for image views in Interface Builder.

| Attribute | Discussion |
|---|---|
| Image | The image to display. You can specify any image in your Xcode project, including standalone images and those in image assets. To set this attribute programmatically, use the [image](uiimageview/image.md) or [animationImages](uiimageview/animationimages.md) property. |
| Highlighted | The image to display when the image view is highlighted. To set this attribute programmatically, use the [highlightedImage](uiimageview/highlightedimage.md) or [highlightedAnimationImages](uiimageview/highlightedanimationimages.md) property. |
| State | The initial state of the image. Use this attribute to mark the image as highlighted. To set this attribute programmatically, use the [highlighted](uiimageview/ishighlighted.md) property. |

### Internationalization

Internationalization of image views is automatic if your view displays only static images loaded from your app bundle. If you’re loading images programmatically, you’re at least partially responsible for loading the correct image.

- For resources in your app bundle, you do this by specifying the name in the attributes inspector or by calling the [+ imageNamed:](<uiimage/init(named_).md>) class method on [UIImage](uiimage.md) to obtain the localized version of each image.
- For images that aren’t in your app bundle, your code must do the following:

1. Determine which image to load in a manner specific to your app, such as providing a localized string that contains the URL.
2. Load that image by passing the URL or data for the correct image to an appropriate [UIImage](uiimage.md) class method, such as [imageWithData:](uiimage/imagewithdata_.md) or [imageWithContentsOfFile:](uiimage/imagewithcontentsoffile_.md).

> [!note] Note
> Screen metrics and layout may also change depending on the language and locale, particularly if the internationalized versions of your images have different dimensions. Where possible, you should try to make minimize dimension differences in internationalized versions of image resources.

For more information, see [Localization](../xcode/localization.md).

### Accessibility

Image views are accessible by default. The default accessibility traits for an image view are Image and User Interaction Enabled.

For more information about making iOS controls accessible, see the accessibility information in [UIControl](uicontrol.md). For general information about making your interface accessible, see [Accessibility for UIKit](accessibility-for-uikit.md).

### State preservation

When you assign a value to an image view’s [restorationIdentifier](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve the frame of the displayed image. Specifically, the class preserves the values of the [bounds](uiview/bounds.md), [center](uiview/center.md), and [transform](uiview/transform.md) properties of the view and the [anchorPoint](../quartzcore/calayer/anchorpoint.md) property of the underlying layer. During restoration, the image view restores these values so that the image appears exactly as before. For more information about how state preservation and restoration works, see [Restoring your app’s state](restoring-your-app-s-state.md).

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating an image view

- [- initWithImage:](<uiimageview/init(image_).md>) — Returns an image view initialized with the specified image.
- [- initWithImage:highlightedImage:](<uiimageview/init(image_highlightedimage_).md>) — Returns an image view initialized with the specified regular and highlighted images.

### Accessing the displayed images

- [image](uiimageview/image.md) — The image displayed in the image view.
- [highlightedImage](uiimageview/highlightedimage.md) — The highlighted image displayed in the image view.

### Animating a sequence of images

- [animationImages](uiimageview/animationimages.md) — An array of [UIImage](uiimage.md) objects to use for an animation.
- [highlightedAnimationImages](uiimageview/highlightedanimationimages.md) — An array of [UIImage](uiimage.md) objects to use for an animation when the view is highlighted.
- [animationDuration](uiimageview/animationduration.md) — The amount of time it takes to go through one cycle of the images.
- [animationRepeatCount](uiimageview/animationrepeatcount.md) — Specifies the number of times to repeat the animation.
- [- startAnimating](<uiimageview/startanimating().md>) — Starts animating the images in the receiver.
- [- stopAnimating](<uiimageview/stopanimating().md>) — Stops animating the images in the receiver.
- [animating](uiimageview/isanimating.md) — Returns a Boolean value indicating whether the animation is running.

### Configuring the image view

- [userInteractionEnabled](uiimageview/isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [highlighted](uiimageview/ishighlighted.md) — A Boolean value that determines whether the image is highlighted.
- [tintColor](uiimageview/tintcolor.md) — A color used to tint template images in the view hierarchy.

### Configuring the appearance of symbol images

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [preferredSymbolConfiguration](uiimageview/preferredsymbolconfiguration.md) — The configuration values to use when rendering the image.

### Configuring symbol effects

- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-18jqj.md>) — Adds a discrete symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-2ixnm.md>) — Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [addSymbolEffect(_:options:animated:completion:)](<uiimageview/addsymboleffect(__options_animated_completion_)-896qd.md>) — Adds an indefinite symbol effect to the image view with the specified options and animation.
- [setSymbolImage(_:contentTransition:options:completion:)](<uiimageview/setsymbolimage(__contenttransition_options_completion_).md>) — Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-218lh.md>) — Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-31zec.md>) — Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [removeSymbolEffect(ofType:options:animated:completion:)](<uiimageview/removesymboleffect(oftype_options_animated_completion_)-2boi2.md>) — Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [removeAllSymbolEffects(options:animated:)](<uiimageview/removeallsymboleffects(options_animated_).md>) — Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletion](uisymboleffectcompletion-7qt7g.md) — A completion handler for adding and removing symbol effects and transitions.
- [UISymbolEffectCompletionContext](uisymboleffectcompletioncontext-swift.struct.md) — Information about a symbol effect’s addition or removal.

### Transitioning between symbol effects

- [UISymbolContentTransition](uisymbolcontenttransition.md) — Represents a symbol content transition and options.

### Managing focus-related behaviors

- [adjustsImageWhenAncestorFocused](uiimageview/adjustsimagewhenancestorfocused.md) — A Boolean value that determines whether the image view responds when an ancestor gains focus.
- [focusedFrameGuide](uiimageview/focusedframeguide.md) — The layout guide to use when the image view is focused.
- [masksFocusEffectToContents](uiimageview/masksfocuseffecttocontents.md) — A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.

### Layering content on top of the image view

- [overlayContentView](uiimageview/overlaycontentview.md) — A view for hosting layered content on top of the image view.

### Specifying the dynamic range

- [imageDynamicRange](uiimageview/imagedynamicrange.md) — The resolved treatment to use for HDR images.
- [preferredImageDynamicRange](uiimageview/preferredimagedynamicrange.md) — The preferred treatment to use for HDR images. By default the image view will defer to the value from its traitCollection.
- [DynamicRange](uiimage/dynamicrange.md)

## See Also

### Content views

- [UIActivityIndicatorView](uiactivityindicatorview.md) — A view that shows that a task is in progress.
- [UICalendarView](uicalendarview.md) — A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [UIContentUnavailableView](uicontentunavailableview.md) — A view that indicates there’s no content to display.
- [UIPickerView](uipickerview.md) — A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [UIProgressView](uiprogressview.md) — A view that depicts the progress of a task over time.
