---
title: Quartz 2D Programming Guide
apple_id: TP30001066
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-03-21'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/glossary/glossary.html
archived_at: '2026-07-15T07:39:19.571454Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz 2D Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Text.md)

# Glossary

- __alpha value__

  The graphics state parameter that Quartz uses to determine how to composite newly painted objects to the existing page. At full intensity (alpha = `1.0`), newly painted objects are opaque. At zero intensity, newly painted objects are invisible (alpha = `0.0`).

- __axial gradient__

  A fill that varies along an axis between two defined end points. All points that lie on a line perpendicular to the axis have the same color value. Also called a _linear gradient_.

- __bitmap__

  A rectangular array (or raster) of pixels, each pixel representing a point in an image. Bitmap images are also called _sampled images_.

- __blend mode__

  Specifies how Quartz combines the foreground painting with the background painting.

- __clipping area__

  A path used to constrain the drawing of other objects within its bounds.

- __color space__

  A one-, two-, three-, or four-dimensional environment whose components (or channels) represent intensity values. For example, RGB space is a three-dimensional color space whose stimuli are the red, green, and blue intensities that make up a given color; and red, green, and blue are color channels.

- __concatenation__

  An operation that combines two matrices by multiplying them together.

- __current graphics state__

  The parameters values that determine how Quartz renders results as it paints.

- __current point__

  The last location Quartz used when painting a path.

- __current transformation matrix__

  An affine transform that Quartz uses to map points from one coordinate space to another.

- __device color space__

  A color space that is tied to the system of color representation for a particular device. This type of color space is not suitable for interchanges of color data between different devices.

- __device-independent color space__

  A color representation that is portable between devices and that is used for the interchanges of color data from the native color space of one device to the native color space of another device. Colors in a device-independent color space appear the same when displayed on different devices, to the extent that the capabilities of the device allow.

- __even-odd rule__

  A fill rule that determines when to paint a pixel. The outcome does not depend on the direction that path segments are drawn. Compare with [nonzero winding number rule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzs).

- __fill__

  An operation that paints the area within a path.

- __generic color space__

  A device-independent color space chosen automatically by Mac OS X to produce the best color for the drawing destination.

- __gradient__

  A fill that varies from one color to another. See also [axial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzu) and [radial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzv).

- __graphics context__

  An opaque data type ([CGContextRef](https://developer.apple.com/documentation/coregraphics/cgcontextref)) that encapsulates the information Quartz uses to draw images to an output device, such as a PDF file, a bitmap, or a window on a display. The information inside a graphics context includes graphics drawing parameters and a device-specific representation of the paint on the page.

- __identity transform__

  An affine transform that, when applied to input coordinates, always returns the input coordinates.

- __image mask__

  A bitmap that specifies an area to paint, but not the color. An image mask acts like a stencil to specify where to place color on the page.

- __inversion__

  An operation that produces original coordinates from transformed ones.

- __layer context__

  An offscreen drawing destination ([CGLayerRef](https://developer.apple.com/documentation/coregraphics/cglayerref)) designed for optimal performance. A a layer context is a much better choice for offscreen drawing than a bitmap graphics context.

- __line cap__

  The style that Quartz uses to draw the endpoint of a line—butt, round, or projecting square.

- __line dash pattern__

  The repeating series of line segments and spaces used to paint a dashed line.

- __line join__

  The style that Quartz uses to draw the junction between connected line segments—miter, round, or bevel.

- __line width__

  The total width of a line, expressed in user space units.

- __linear gradient__

  See [axial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzu).

- __nonzero winding number rule__

  A fill rule that determines when to paint a pixel. The outcome depends on the direction that path segments are drawn. Compare with [even-odd rule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzt).

- __page__

  The virtual canvas that Quartz paints to.

- __painter’s model__

  A drawing model in which each successive drawing operation applies a layer of paint to a [page](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzr).

- __path__

  One or more shapes (known as subpaths) that Quartz paints as a unit. A subpath can consist of straight lines, curves, or both. It can be open or closed.

- __pattern__

  A sequence of drawing operations that Quartz can repeatedly paint to a graphics context.

- __pattern space__

  An abstract space that maps to the default user space by the transformation matrix (the pattern matrix) you specify when you create the pattern. Pattern space is separate from user space. The untransformed pattern space maps to the base (untransformed) user space, regardless of the state of the current transformation matrix.

- __premultiplied alpha__

  A source color whose components are already multiplied by an alpha value. Premultiplying speeds up the rendering of an image by eliminating an extra multiplication operation per color component. See also [alpha value](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrsgewvgvzw).

- __radial gradient__

  A fill that varies radially along an axis between two defined ends, which typically are both circles. Points share the same color value if they lie on the circumference of a circle whose center point falls on the axis. The radius of the circular sections of the gradient are defined by the radii of the end circles; the radius of each intermediate circle varies linearly from one end to the other.

- __rendering intent__

  Specifies how Quartz maps colors from the source color space to those that are within the gamut of the destination color space of a graphics context.

- __rotation__

  An operation that moves the coordinate space the specified angle.

- __scaling__

  An operation that changes the scale of the coordinate space by the specified x and y factors, effectively stretching or shrinking coordinates. The magnitude of the x and y factors governs whether the new coordinates are larger or smaller than the original. A negative factor flips the corresponding axis.

- __shadow__

  An image painted underneath, and offset from, a graphics object such that the shadow mimics the effect of a light source cast on the graphics object.

- __stroke__

  An operation that paints a line that straddles a path.

- __tiling__

  The process of rendering pattern cells to a portion of a page. Quartz has three tiling options—no distortion, constant spacing with minimal distortion, and constant spacing.

- __translation__

  An operation that moves the origin of the coordinate space by the number of units specified for the x and y axes.

- __transparency layer__

  A composite of two or more objects that Quartz treats as a single object when applying effects, such as shadows.

- __user space__

  The device-independent coordinate system that you use when drawing using Quartz 2D.

[Next](Document%20Revision%20History.md)[Previous](Text.md)

