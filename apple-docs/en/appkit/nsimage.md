---
title: NSImage
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsimage
source_url: 'https://developer.apple.com/documentation/appkit/nsimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsimage.json'
content_hash: 'sha256:f33cfc9cc989074e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSImage

<sub>Class</sub>

A high-level interface for manipulating image data.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSImage
```

## Overview

You use instances of [NSImage](nsimage.md) to load existing images, create new images, and draw the resulting image data into your views. Although you use this class predominantly for image-related operations, the class itself knows little about the underlying image data. Instead, it works in conjunction with one or more image representation objects (subclasses of [NSImageRep](nsimagerep.md)) to manage and render the image data. For the most part, these interactions are transparent.

The  class serves many purposes, providing support for the following tasks:

- Loading images stored on disk or at a specified URL.
- Drawing images into a view or graphics context.
- Providing the contents of a [CALayer](../quartzcore/calayer.md) object.
- Creating new images based on a series of captured drawing commands.
- Producing versions of the image in a different format.

The `NSImage` class itself is capable of managing image data in a variety of formats. The specific list of formats is dependent on the version of the operating system but includes many standard formats such as TIFF, JPEG, GIF, PNG, and PDF among others. AppKit manages each format using a specific type of image representation object, whose job is to manage the actual image data. You can get a list of supported formats using the methods described in Determining Supported Types of Images.

### Using Images with Core Animation Layers

Although you can assign an `NSImage` object directly to the [contents](../quartzcore/calayer/contents.md) property of a [CALayer](../quartzcore/calayer.md) object, doing so may not always yield the best results. Instead of using your image object, you can use the [- layerContentsForContentsScale:](<nsimage/layercontents(forcontentsscale_).md>) method to obtain an object that you can use for your layer’s contents. The image created by that method serves as the contents of a layer, which also supports all of the layer’s gravity modes. By contrast, the `NSImage` class supports only the [resize](../quartzcore/calayercontentsgravity/resize.md), [resizeAspect](../quartzcore/calayercontentsgravity/resizeaspect.md), and [resizeAspectFill](../quartzcore/calayercontentsgravity/resizeaspectfill.md) modes.

Before calling the [- layerContentsForContentsScale:](<nsimage/layercontents(forcontentsscale_).md>) method, use the [- recommendedLayerContentsScale:](<nsimage/recommendedlayercontentsscale(__).md>) method to get the recommended scale factor for the resulting image. The code listing below shows a typical example that uses the scale factor of a window’s backing store as the desired scale factor. From that scale factor, the code gets the scale factor for the specified image object and creates an object that you assign to the layer. You might use this code for images that fit the layer bounds precisely or for which you rely on the [contentsGravity](../quartzcore/calayer/contentsgravity.md) property of the layer to position or scale the image.

Listing 1. Assigning an image to a layer

```objc
static void updateLayerWithImageInWindow1(NSImage *image, CALayer *layer, NSWindow *window) {
   CGFloat desiredScaleFactor = [window backingScaleFactor];
   CGFloat actualScaleFactor = [image recommendedLayerContentsScale:desiredScaleFactor];
 
   id layerContents = [image layerContentsForContentsScale:actualScaleFactor];
 
   [layer setContents:layerContents];
   [layer setContentsScale:actualScaleFactor];
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [AttachableAsImage](../testing/attachableasimage.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSPasteboardReading](nspasteboardreading.md), [NSPasteboardWriting](nspasteboardwriting.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Transferable](../coretransferable/transferable.md)

## Topics

### Creating Images by Name

- [Configuring and displaying symbol images in your UI](../uikit/configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [+ imageNamed:](<nsimage/init(named_).md>) — Returns the image object associated with the specified name.
- [+ imageWithSystemSymbolName:accessibilityDescription:](<nsimage/init(systemsymbolname_accessibilitydescription_).md>) — Creates a symbol image with the system symbol name and accessibility description you specify.
- [+ imageWithSystemSymbolName:variableValue:accessibilityDescription:](<nsimage/init(systemsymbolname_variablevalue_accessibilitydescription_).md>) — Creates a symbol image with the system symbol name and variable value you specify.
- [+ imageWithSymbolName:variableValue:](<nsimage/init(symbolname_variablevalue_).md>) — Creates a symbol image with the symbol name and variable value you specify.
- [+ imageWithSymbolName:bundle:variableValue:](<nsimage/init(symbolname_bundle_variablevalue_).md>) — Creates a symbol image with the specified symbol name and variable value.
- [init(resource:)](<nsimage/init(resource_).md>) — Initialize a `NSImage` with an image resource.
- [- setName:](<nsimage/setname(__).md>) — Registers the image object under the specified name.
- [- name](<nsimage/name().md>) — Returns the name associated with the image, if any.
- [Name](nsimage/name-swift.typealias.md) — Named images, defined by the system or you, for use in your app.
- [init(imageLiteralResourceName:)](<nsimage/init(imageliteralresourcename_).md>) — Creates an image initialized with the specified resource name.

### Creating Dynamically Drawn Images

- [+ imageWithSize:flipped:drawingHandler:](<nsimage/init(size_flipped_drawinghandler_).md>) — Creates and returns an image object whose contents are drawn using the specified block.

### Creating Images from Resource Files

- [- initByReferencingFile:](<nsimage/init(byreferencingfile_).md>) — Initializes and returns an image object using the specified file.
- [- initByReferencingURL:](<nsimage/init(byreferencing_).md>) — Initializes and returns an image object using the specified URL.
- [- initWithContentsOfFile:](<nsimage/init(contentsoffile_).md>) — Initializes and returns an image object with the contents of the specified file.
- [- initWithContentsOfURL:](<nsimage/init(contentsof_).md>) — Initializes and returns an image object with the contents of the specified URL.

### Creating Images from Existing Data

- [- initWithData:](<nsimage/init(data_).md>) — Initializes and returns an image object using the provided image data.
- [- initWithDataIgnoringOrientation:](<nsimage/init(dataignoringorientation_).md>) — Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [- initWithCGImage:size:](<nsimage/init(cgimage_size_)-8oznv.md>) — Creates a new image using the contents of the provided image.
- [- initWithPasteboard:](<nsimage/init(pasteboard_).md>) — Initializes and returns an image object with data from the specified pasteboard.
- [- initWithCoder:](<nsimage/init(coder_).md>) — Initializes and returns an image object from data in an unarchiver.

### Creating Empty Images

- [- initWithSize:](<nsimage/init(size_).md>) — Initializes and returns an image object with the specified dimensions.

### Creating Symbol Images

- [- imageWithSymbolConfiguration:](<nsimage/withsymbolconfiguration(__).md>) — Creates a new symbol image with the specified configuration.
- [SymbolConfiguration](nsimage/symbolconfiguration-swift.class.md) — An object that contains the specific font, style, and weight attributes to apply to a symbol image.

### Getting the Symbol Image Configuration

- [symbolConfiguration](nsimage/symbolconfiguration-swift.property.md) — The configuration details for a symbol image.

### Managing Loading and Drawing of Images

- [delegate](nsimage/delegate.md) — The image’s delegate object.
- [NSImageDelegate](nsimagedelegate.md) — A set of optional methods that you can use to respond to drawing failures and manage incremental loads.

### Setting Attributes of Images

- [size](nsimage/size.md) — The size of the image.
- [template](nsimage/istemplate.md) — A Boolean value that determines whether the image represents a template image.
- [template](nsimage/istemplate.md) — A Boolean value that determines whether the image represents a template image.

### Determining Supported Types of Images

- [+ canInitWithPasteboard:](<nsimage/caninit(with_).md>) — Tests whether the image can create an instance of itself using pasteboard data.
- [imageTypes](nsimage/imagetypes.md) — Returns an array of UTI strings identifying the image types supported by the registered image representation objects, either directly or through a user-installed filter service.
- [imageUnfilteredTypes](nsimage/imageunfilteredtypes.md) — Returns an array of UTI strings identifying the image types supported directly by the registered image representation objects.

### Working with Representations of Images

- [- addRepresentation:](<nsimage/addrepresentation(__).md>) — Adds the specified image representation object to the image.
- [- addRepresentations:](<nsimage/addrepresentations(__).md>) — Adds an array of image representation objects to the image.
- [representations](nsimage/representations.md) — An array containing all of the image object’s image representations.
- [- removeRepresentation:](<nsimage/removerepresentation(__).md>) — Removes and releases the specified image representation.
- [- bestRepresentationForRect:context:hints:](<nsimage/bestrepresentation(for_context_hints_).md>) — Returns the best representation of the image for the specified rectangle using the provided hints.
- [HintKey](nsimagerep/hintkey.md) — Constants for the keys to include in a hints dictionary when drawing the image.
- [LayoutDirection](nsimage/layoutdirection.md) — Constants that describe the layout direction for the image.

### Setting the Representation Selection Criteria for Images

- [prefersColorMatch](nsimage/preferscolormatch.md) — A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [usesEPSOnResolutionMismatch](nsimage/usesepsonresolutionmismatch.md) — A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.
- [matchesOnMultipleResolution](nsimage/matchesonmultipleresolution.md) — A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.

### Drawing Images

- [- drawInRect:](<nsimage/draw(in_).md>) — Draws the image in the specified rectangle.
- [- drawAtPoint:fromRect:operation:fraction:](<nsimage/draw(at_from_operation_fraction_).md>) — Draws all or part of the image at the specified point in the current coordinate system.
- [- drawInRect:fromRect:operation:fraction:](<nsimage/draw(in_from_operation_fraction_).md>) — Draws all or part of the image in the specified rectangle in the current coordinate system.
- [- drawInRect:fromRect:operation:fraction:respectFlipped:hints:](<nsimage/draw(in_from_operation_fraction_respectflipped_hints_).md>) — Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.
- [- drawRepresentation:inRect:](<nsimage/drawrepresentation(__in_).md>) — Draws the image using the specified image representation object.
- [NSCompositingOperation](nscompositingoperation.md) — Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.

### Managing Drawing Options

- [valid](nsimage/isvalid.md) — A Boolean value that indicates whether it is possible to draw an image representation.
- [backgroundColor](nsimage/backgroundcolor.md) — The background color for the image.
- [capInsets](nsimage/capinsets.md) — The cap insets for the image.
- [resizingMode](nsimage/resizingmode-swift.property.md) — The resizing mode for the image.
- [ResizingMode](nsimage/resizingmode-swift.enum.md) — Constants that describe the resizing mode for the image.

### Working with Alignment Metadata

- [alignmentRect](nsimage/alignmentrect.md) — A rectangle that you can use to position the image during layout.

### Managing Caching Options

- [cacheMode](nsimage/cachemode-swift.property.md) — The image’s caching mode.
- [- recache](<nsimage/recache().md>) — Invalidates and frees offscreen caches of all image representations.
- [CacheMode](nsimage/cachemode-swift.enum.md) — Constants that specify the caching policy on a per-image basis.

### Producing TIFF Data for Images

- [TIFFRepresentation](nsimage/tiffrepresentation.md) — A data object containing TIFF data for all of the image representations in the image.
- [- TIFFRepresentationUsingCompression:factor:](<nsimage/tiffrepresentation(using_factor_).md>) — Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.

### Producing Core Graphics Images

- [- CGImageForProposedRect:context:hints:](<nsimage/cgimage(forproposedrect_context_hints_).md>) — Returns a Core Graphics image based on the contents of the current image object.

### Hit-Testing Images

- [- hitTestRect:withImageDestinationRect:context:hints:flipped:](<nsimage/hittest(__withdestinationrect_context_hints_flipped_).md>) — Returns whether the destination rectangle would intersect a non-transparent portion of the image.

### Managing Image Accessibility

- [accessibilityDescription](nsimage/accessibilitydescription.md) — The image’s accessibility description.

### Using Images with Core Animation

- [- layerContentsForContentsScale:](<nsimage/layercontents(forcontentsscale_).md>) — Returns an object that may be used as the contents of a layer.
- [- recommendedLayerContentsScale:](<nsimage/recommendedlayercontentsscale(__).md>) — Returns the recommended layer contents scale for this image.

### Managing Axis Matching

- [matchesOnlyOnBestFittingAxis](nsimage/matchesonlyonbestfittingaxis.md) — A Boolean value that indicates whether the image matches only on the best fitting axis.

### Localizing Images

- [- imageWithLocale:](<nsimage/withlocale(__).md>) — Creates and returns a new image with the specified locale.
- [locale](nsimage/locale.md) — The image’s preferred locale for resolving representations, if one has been specified using `-imageWithLocale:`. Otherwise, `nil`.

### Deprecated

- [Deprecated Symbols](nsimage-deprecated-symbols.md) — Review symbols that are no longer supported, and find the replacements to use instead.

### Enumerations

- [DynamicRange](nsimage/dynamicrange.md) — Describes how High Dynamic Range (HDR) image content displays.

### Initializers

- [init(CGImage:size:)](<nsimage/init(cgimage_size_)-15zeh.md>)
- [init(byReferencingURL:)](<nsimage/init(byreferencingurl_).md>)
- [init(contentsOfURL:)](<nsimage/init(contentsofurl_).md>)

### Default Implementations

- [NSPasteboardReading Implementations](nsimage/nspasteboardreading-implementations.md)

## See Also

### Images

- [Providing images for different appearances](../uikit/providing-images-for-different-appearances.md) — Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../uikit/supporting-hdr-images-in-your-app.md) — ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [Applying Apple HDR effect to your photos](applying-apple-hdr-effect-to-your-photos.md) — You can decode and apply Apple’s HDR gain map to your own images.
- [NSImageDelegate](nsimagedelegate.md) — A set of optional methods that you can use to respond to drawing failures and manage incremental loads.
- [NSImageRep](nsimagerep.md) — A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.
