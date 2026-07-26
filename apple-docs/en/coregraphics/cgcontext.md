---
title: CGContext
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext.json'
content_hash: 'sha256:0ecf91b098032a09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContext

<sub>Class</sub>

A Quartz 2D drawing environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGContext
```

## Overview

A `CGContext` instance represents a Quartz 2D drawing destination. A graphics context contains drawing parameters and all device-specific information needed to render the paint on a page to the destination, whether the destination is a window in an application, a bitmap image, a PDF document, or a printer.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Bitmap Graphics Contexts

- [CGBitmapContextReleaseDataCallback](cgbitmapcontextreleasedatacallback.md) — A callback function used to release data associate with the bitmap context.

### Creating PDF Graphics Contexts

- [CGPDFContextCreateWithURL](<cgcontext/init(__mediabox___).md>) — Creates a URL-based PDF graphics context.
- [CGPDFContextCreate](<cgcontext/init(consumer_mediabox___).md>) — Creates a PDF graphics context.
- [Auxiliary Dictionary Keys](auxiliary-dictionary-keys.md) — Keys for the auxiliary info dictionary you specify when creating a PDF context.

### Converting Between Coordinate Spaces

- [CGContextGetUserSpaceToDeviceSpaceTransform](cgcontext/userspacetodevicespacetransform.md) — Returns an affine transform that maps user space coordinates to device space coordinates.
- [CGContextConvertPointToDeviceSpace](<cgcontext/converttodevicespace(__)-53m7u.md>) — Returns a point that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertPointToUserSpace](<cgcontext/converttouserspace(__)-3mtg3.md>) — Returns a point that is transformed from device space coordinates to user space coordinates.
- [CGContextConvertRectToDeviceSpace](<cgcontext/converttodevicespace(__)-91x5g.md>) — Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [CGContextConvertRectToUserSpace](<cgcontext/converttouserspace(__)-1hk5r.md>) — Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [CGContextConvertSizeToDeviceSpace](<cgcontext/converttodevicespace(__)-224h2.md>) — Returns a size that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertSizeToUserSpace](<cgcontext/converttouserspace(__)-693ur.md>) — Returns a size that is transformed from device space coordinates to user space coordinates.

### Constructing a Current Graphics Path

- [CGContextBeginPath](<cgcontext/beginpath().md>) — Creates a new empty path in a graphics context.
- [move(to:)](<cgcontext/move(to_).md>) — Begins a new subpath at the specified point.
- [addLine(to:)](<cgcontext/addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:)](<cgcontext/addlines(between_).md>) — Adds a sequence of connected straight-line segments to the current path.
- [CGContextAddRect](<cgcontext/addrect(__).md>) — Adds a rectangular path to the current path.
- [addRects(_:)](<cgcontext/addrects(__).md>) — Adds a set of rectangular paths to the current path.
- [CGContextAddEllipseInRect](<cgcontext/addellipse(in_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addArc(center:radius:startAngle:endAngle:clockwise:)](<cgcontext/addarc(center_radius_startangle_endangle_clockwise_).md>) — Adds an arc of a circle to the current path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:)](<cgcontext/addarc(tangent1end_tangent2end_radius_).md>) — Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<cgcontext/addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [addQuadCurve(to:control:)](<cgcontext/addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [CGContextAddPath](<cgcontext/addpath(__).md>) — Adds a previously created path object to the current path in a graphics context.
- [CGContextClosePath](<cgcontext/closepath().md>) — Closes and terminates the current path’s subpath.
- [CGContextCopyPath](cgcontext/path.md) — Returns a path object built from the current path information in a graphics context.
- [CGContextReplacePathWithStrokedPath](<cgcontext/replacepathwithstrokedpath().md>) — Replaces the path in the graphics context with the stroked version of the path.

### Examining the Current Graphics Path

- [CGContextGetPathBoundingBox](cgcontext/boundingboxofpath.md) — Returns the smallest rectangle that contains the current path.
- [CGContextGetPathCurrentPoint](cgcontext/currentpointofpath.md) — Returns the current point in a non-empty path.
- [CGContextIsPathEmpty](cgcontext/ispathempty.md) — Indicates whether the current path contains any subpaths.
- [CGContextPathContainsPoint](<cgcontext/pathcontains(__mode_).md>) — Checks to see whether the specified point is contained in the current path.

### Drawing the Current Graphics Path

- [CGContextDrawPath](<cgcontext/drawpath(using_).md>) — Draws the current path using the provided drawing mode.
- [CGPathDrawingMode](cgpathdrawingmode.md) — Options for rendering a path.
- [fillPath(using:)](<cgcontext/fillpath(using_).md>) — Paints the area within the current path, as determined by the specified fill rule.
- [CGContextStrokePath](<cgcontext/strokepath().md>) — Paints a line along the current path.

### Drawing Shapes

- [CGContextClearRect](<cgcontext/clear(__).md>) — Paints a transparent rectangle.
- [CGContextFillRect](<cgcontext/fill(__)-7a0rk.md>) — Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [fill(_:)](<cgcontext/fill(__)-6jc4y.md>) — Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [CGContextFillEllipseInRect](<cgcontext/fillellipse(in_).md>) — Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [CGContextStrokeRect](<cgcontext/stroke(__).md>) — Paints a rectangular path.
- [CGContextStrokeRectWithWidth](<cgcontext/stroke(__width_).md>) — Paints a rectangular path, using the specified line width.
- [CGContextStrokeEllipseInRect](<cgcontext/strokeellipse(in_).md>) — Strokes an ellipse that fits inside the specified rectangle.
- [strokeLineSegments(between:)](<cgcontext/strokelinesegments(between_).md>) — Strokes a sequence of line segments.

### Drawing Images and PDF Content

- [draw(_:in:byTiling:)](<cgcontext/draw(__in_bytiling_).md>) — Draws an image in the specified area.
- [CGContextDrawPDFPage](<cgcontext/drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGContextGetInterpolationQuality](cgcontext/interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
- [CGInterpolationQuality](cginterpolationquality.md) — Levels of interpolation quality for rendering an image.

### Drawing Gradients and Shadings

- [CGContextDrawLinearGradient](<cgcontext/drawlineargradient(__start_end_options_).md>) — Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [CGContextDrawRadialGradient](<cgcontext/drawradialgradient(__startcenter_startradius_endcenter_endradius_options_).md>) — Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [CGGradientDrawingOptions](cggradientdrawingoptions.md) — Drawing locations for gradients.
- [CGContextDrawShading](<cgcontext/drawshading(__).md>) — Fills the clipping path of a context with the specified shading.

### Drawing Text

- [CGContextGetTextMatrix](cgcontext/textmatrix.md) — Returns the current text matrix.
- [textPosition](cgcontext/textposition.md)
- [CGContextSelectFont](<cgcontext/selectfont(name_size_textencoding_).md>) — Sets the font and font size in a graphics context. _(deprecated)_
- [CGContextSetCharacterSpacing](<cgcontext/setcharacterspacing(__).md>) — Sets the current character spacing.
- [CGContextSetFont](<cgcontext/setfont(__).md>) — Sets the platform font in a graphics context.
- [CGContextSetFontSize](<cgcontext/setfontsize(__).md>) — Sets the current font size.
- [CGContextSetTextDrawingMode](<cgcontext/settextdrawingmode(__).md>) — Sets the current text drawing mode.
- [CGContextSetAllowsFontSmoothing](<cgcontext/setallowsfontsmoothing(__).md>) — Sets whether or not to allow font smoothing for a graphics context.
- [CGContextSetAllowsFontSubpixelPositioning](<cgcontext/setallowsfontsubpixelpositioning(__).md>) — Sets whether or not to allow subpixel positioning for a graphics context.
- [CGContextSetAllowsFontSubpixelQuantization](<cgcontext/setallowsfontsubpixelquantization(__).md>) — Sets whether or not to allow subpixel quantization for a graphics context.
- [CGContextSetShouldSmoothFonts](<cgcontext/setshouldsmoothfonts(__).md>) — Enables or disables font smoothing in a graphics context.
- [CGContextSetShouldSubpixelPositionFonts](<cgcontext/setshouldsubpixelpositionfonts(__).md>) — Enables or disables subpixel positioning in a graphics context.
- [CGContextSetShouldSubpixelQuantizeFonts](<cgcontext/setshouldsubpixelquantizefonts(__).md>) — Enables or disables subpixel quantization in a graphics context.
- [CGContextShowGlyphs](<cgcontext/showglyphs(g_count_).md>) — Displays an array of glyphs at the current text position. _(deprecated)_
- [showGlyphs(_:at:)](<cgcontext/showglyphs(__at_).md>) — Draws a set of glyphs at a set of corresponding positions.
- [CGContextShowGlyphsAtPoint](<cgcontext/showglyphsatpoint(x_y_glyphs_count_).md>) — Displays an array of glyphs at a position you specify. _(deprecated)_
- [CGContextShowGlyphsWithAdvances](<cgcontext/showglyphswithadvances(glyphs_advances_count_).md>) — Draws an array of glyphs with varying offsets. _(deprecated)_
- [CGContextShowText](<cgcontext/showtext(string_length_).md>) — Displays a character array at the current text position, a point specified by the current text matrix. _(deprecated)_
- [CGContextShowTextAtPoint](<cgcontext/showtextatpoint(x_y_string_length_).md>) — Displays a character string at a position you specify. _(deprecated)_
- [CGTextDrawingMode](cgtextdrawingmode.md) — Modes for rendering text.

### Drawing Core Graphics Layers

- [draw(_:at:)](<cgcontext/draw(__at_).md>) — Draws the contents of a layer object at the specified point.
- [draw(_:in:)](<cgcontext/draw(__in_).md>) — Draws the contents of a layer object into the specified rectangle.

### Setting Fill, Stroke, and Shadow Colors

- [CGContextSetFillColorWithColor](<cgcontext/setfillcolor(__)-8lhn8.md>) — Sets the current fill color in a graphics context, using a CGColor.
- [CGContextSetFillColor](<cgcontext/setfillcolor(__)-756dy.md>) — Sets the current fill color.
- [CGContextSetCMYKFillColor](<cgcontext/setfillcolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current fill color to a value in the DeviceCMYK color space.
- [CGContextSetGrayFillColor](<cgcontext/setfillcolor(gray_alpha_).md>) — Sets the current fill color to a value in the DeviceGray color space.
- [CGContextSetRGBFillColor](<cgcontext/setfillcolor(red_green_blue_alpha_).md>) — Sets the current fill color to a value in the DeviceRGB color space.
- [CGContextSetFillColorSpace](<cgcontext/setfillcolorspace(__).md>) — Sets the fill color space in a graphics context.
- [CGContextSetShadow](<cgcontext/setshadow(offset_blur_).md>) — Enables shadowing in a graphics context.
- [CGContextSetShadowWithColor](<cgcontext/setshadow(offset_blur_color_).md>) — Enables shadowing with color a graphics context.
- [CGContextSetStrokeColorWithColor](<cgcontext/setstrokecolor(__)-1sskg.md>) — Sets the current stroke color in a context, using a CGColor.
- [CGContextSetStrokeColor](<cgcontext/setstrokecolor(__)-4pd8p.md>) — Sets the current stroke color.
- [CGContextSetCMYKStrokeColor](<cgcontext/setstrokecolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current stroke color to a value in the DeviceCMYK color space.
- [CGContextSetGrayStrokeColor](<cgcontext/setstrokecolor(gray_alpha_).md>) — Sets the current stroke color to a value in the DeviceGray color space.
- [CGContextSetRGBStrokeColor](<cgcontext/setstrokecolor(red_green_blue_alpha_).md>) — Sets the current stroke color to a value in the DeviceRGB color space.
- [CGContextSetStrokeColorSpace](<cgcontext/setstrokecolorspace(__).md>) — Sets the stroke color space in a graphics context.
- [CGContextSetStrokePattern](<cgcontext/setstrokepattern(__colorcomponents_).md>) — Sets the stroke pattern in the specified graphics context.
- [CGContextSetAlpha](<cgcontext/setalpha(__).md>) — Sets the opacity level for objects drawn in a graphics context.

### Working with the Current Clipping Path

- [clip(using:)](<cgcontext/clip(using_).md>) — Modifies the current clipping path.
- [CGContextClipToRect](<cgcontext/clip(to_)-7cbwq.md>) — Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [clip(to:)](<cgcontext/clip(to_)-2eg0.md>) — Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [CGContextClipToMask](<cgcontext/clip(to_mask_).md>) — Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [CGContextGetClipBoundingBox](cgcontext/boundingboxofclippath.md) — Returns the bounding box of a clipping path.

### Working with Transparency Layers

- [CGContextBeginTransparencyLayerWithRect](<cgcontext/begintransparencylayer(in_auxiliaryinfo_).md>) — Begins a transparency layer whose contents are bounded by the specified rectangle.
- [CGContextBeginTransparencyLayer](<cgcontext/begintransparencylayer(auxiliaryinfo_).md>) — Begins a transparency layer.
- [CGContextEndTransparencyLayer](<cgcontext/endtransparencylayer().md>) — Ends a transparency layer.

### Working with the Current Transformation Matrix

- [CGContextGetCTM](cgcontext/ctm.md) — Returns the current transformation matrix.
- [CGContextRotateCTM](<cgcontext/rotate(by_).md>) — Rotates the user coordinate system in a context.
- [CGContextScaleCTM](<cgcontext/scaleby(x_y_).md>) — Changes the scale of the user coordinate system in a context.
- [CGContextTranslateCTM](<cgcontext/translateby(x_y_).md>) — Changes the origin of the user coordinate system in a context.
- [CGContextConcatCTM](<cgcontext/concatenate(__).md>) — Transforms the user coordinate system in a context using a specified matrix.

### Setting Path Drawing Options

- [CGContextSetAllowsAntialiasing](<cgcontext/setallowsantialiasing(__).md>) — Sets whether or not to allow antialiasing for a graphics context.
- [CGContextSetFlatness](<cgcontext/setflatness(__).md>) — Sets the accuracy of curved paths in a graphics context.
- [CGContextSetLineCap](<cgcontext/setlinecap(__).md>) — Sets the style for the endpoints of lines drawn in a graphics context.
- [setLineDash(phase:lengths:)](<cgcontext/setlinedash(phase_lengths_).md>) — Sets the pattern for drawing dashed lines.
- [CGContextSetLineJoin](<cgcontext/setlinejoin(__).md>) — Sets the style for the joins of connected lines in a graphics context.
- [CGContextSetLineWidth](<cgcontext/setlinewidth(__).md>) — Sets the line width for a graphics context.
- [CGContextSetMiterLimit](<cgcontext/setmiterlimit(__).md>) — Sets the miter limit for the joins of connected lines in a graphics context.
- [CGContextSetPatternPhase](<cgcontext/setpatternphase(__).md>) — Sets the pattern phase of a context.
- [CGContextSetFillPattern](<cgcontext/setfillpattern(__colorcomponents_).md>) — Sets the fill pattern in the specified graphics context.
- [CGContextSetShouldAntialias](<cgcontext/setshouldantialias(__).md>) — Sets antialiasing on or off for a graphics context.

### Saving and Restoring Graphics State

- [CGContextSaveGState](<cgcontext/savegstate().md>) — Pushes a copy of the current graphics state onto the graphics state stack for the context.
- [CGContextRestoreGState](<cgcontext/restoregstate().md>) — Sets the current graphics state to the state most recently saved.

### Managing a Graphics Context

- [CGContextFlush](<cgcontext/flush().md>) — Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [CGContextSynchronize](<cgcontext/synchronize().md>) — Marks a window context for update.
- [CGContextSetBlendMode](<cgcontext/setblendmode(__).md>) — Sets how sample values are composited by a graphics context.
- [CGBlendMode](cgblendmode.md) — Compositing operations for images.
- [CGContextSetRenderingIntent](<cgcontext/setrenderingintent(__).md>) — Sets the rendering intent in the current graphics state.

### Managing a Bitmap Graphics Context

- [CGBitmapContextGetBitmapInfo](cgcontext/bitmapinfo.md) — Obtains the bitmap information associated with a bitmap graphics context.
- [CGBitmapContextGetAlphaInfo](cgcontext/alphainfo.md) — Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [CGBitmapContextGetBitsPerComponent](cgcontext/bitspercomponent.md) — Returns the bits per component of a bitmap context.
- [CGBitmapContextGetBitsPerPixel](cgcontext/bitsperpixel.md) — Returns the bits per pixel of a bitmap context.
- [CGBitmapContextGetBytesPerRow](cgcontext/bytesperrow.md) — Returns the bytes per row of a bitmap context.
- [CGBitmapContextGetColorSpace](cgcontext/colorspace.md) — Returns the color space of a bitmap context.
- [CGBitmapContextGetData](cgcontext/data.md) — Returns a pointer to the image data associated with a bitmap context.
- [CGBitmapContextGetHeight](cgcontext/height.md) — Returns the height in pixels of a bitmap context.
- [CGBitmapContextGetWidth](cgcontext/width.md) — Returns the width in pixels of a bitmap context.
- [CGBitmapContextCreateImage](<cgcontext/makeimage().md>) — Creates and returns a CGImage from the pixel data in a bitmap graphics context.

### Managing a PDF Graphics Context

- [CGPDFContextBeginPage](<cgcontext/beginpdfpage(__).md>) — Begins a new page in a PDF graphics context.
- [CGPDFContextEndPage](<cgcontext/endpdfpage().md>) — Ends the current page in the PDF graphics context.
- [CGPDFContextAddDestinationAtPoint](<cgcontext/adddestination(__at_).md>) — Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [CGPDFContextSetDestinationForRect](<cgcontext/setdestination(__for_).md>) — Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [CGPDFContextSetURLForRect](<cgcontext/seturl(__for_).md>) — Sets the URL associated with a rectangle in a PDF graphics context.
- [CGPDFContextAddDocumentMetadata](<cgcontext/adddocumentmetadata(__).md>) — Associates custom metadata with the PDF document.
- [CGPDFContextClose](<cgcontext/closepdf().md>) — Closes a PDF document.

### Managing a Page-Based Graphics Context

- [CGContextBeginPage](<cgcontext/beginpage(mediabox_).md>) — Starts a new page in a page-based graphics context.
- [CGContextEndPage](<cgcontext/endpage().md>) — Ends the current page in a page-based graphics context.

### Working with Core Foundation Types

- [CGContextGetTypeID](cgcontext/typeid.md) — Returns the type identifier for a graphics context.

### Constants

- [CGPathFillRule](cgpathfillrule.md) — Rules for determining which regions are interior to a path, used by the [fillPath(using:)](<cgcontext/fillpath(using_).md>) and [clip(using:)](<cgcontext/clip(using_).md>) methods.
- [CGTextEncoding](cgtextencoding.md) — Text encodings for fonts.

### Instance Methods

- [draw(_:in:by:options:)](<cgcontext/draw(__in_by_options_).md>)
- [CGContextResetClip](<cgcontext/resetclip().md>)
- [CGContextSetEDRTargetHeadroom](<cgcontext/setedrtargetheadroom(__).md>)
- [CGContextSynchronizeAttributes](<cgcontext/synchronizeattributes().md>)

### Structures

- [AuxiliaryInfo](cgcontext/auxiliaryinfo.md)

### Initializers

- [CGBitmapContextCreate](<cgcontext/init(data_width_height_bitspercomponent_bytesperrow_space_bitmapinfo_)-10b3i.md>)
- [init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:)](<cgcontext/init(data_width_height_bitspercomponent_bytesperrow_space_bitmapinfo_)-4fkaf.md>) _(deprecated)_
- [CGBitmapContextCreateWithData](<cgcontext/init(data_width_height_bitspercomponent_bytesperrow_space_bitmapinfo_releasecallback_releaseinfo_)-4yzt5.md>)
- [init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)](<cgcontext/init(data_width_height_bitspercomponent_bytesperrow_space_bitmapinfo_releasecallback_releaseinfo_)-71ea9.md>) _(deprecated)_

### Instance Properties

- [contentToneMappingInfo](cgcontext/contenttonemappinginfo.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### 2D Drawing

- [CGImage](cgimage.md) — A bitmap image or image mask.
- [CGPath](cgpath.md) — An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGMutablePath](cgmutablepath.md) — A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGLayer](cglayer.md) — An offscreen context for reusing content drawn with Core Graphics.
