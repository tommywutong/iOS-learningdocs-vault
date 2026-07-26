---
title: UIBezierPath
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath.json'
content_hash: 'sha256:69ca0af424db6fb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBezierPath

<sub>Class</sub>

A path that consists of straight and curved line segments that you can render in your custom views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class UIBezierPath
```

## Overview

You use this class initially to specify just the geometry for your path. Paths can define simple shapes such as rectangles, ovals, and arcs or they can define complex polygons that incorporate a mixture of straight and curved line segments. After defining the shape, you can use additional methods of this class to render the path in the current drawing context.

A [UIBezierPath](uibezierpath.md) object combines the geometry of a path with attributes that describe the path during rendering. You set the geometry and attributes separately and can change them independent of one another. After you have the object configured the way you want it, you can tell it to draw itself in the current context. Because the creation, configuration, and rendering process are all distinct steps, Bézier path objects can be reused easily in your code. You can even use the same object to render the same shape multiple times, perhaps changing the rendering options between successive drawing calls.

You set the geometry of a path by manipulating the path’s current point. When you create a new empty path object, the current point is undefined and must be set explicitly. To move the current point without drawing a segment, you use the [- moveToPoint:](<uibezierpath/move(to_).md>) method. All other methods result in the addition of either a line or curve segments to the path. The methods for adding new segments always assume you are starting at the current point and ending at some new point that you specify. After adding the segment, the end point of the new segment automatically becomes the current point.

A single Bézier path object can contain any number of open or closed subpaths, where each subpath represents a connected series of path segments. Calling the [- closePath](<uibezierpath/close().md>) method closes a subpath by adding a straight line segment from the current point to the first point in the subpath. Calling the [- moveToPoint:](<uibezierpath/move(to_).md>) method ends the current subpath (without closing it) and sets the starting point of the next subpath. The subpaths of a Bézier path object share the same drawing attributes and must be manipulated as a group. To draw subpaths with different attributes, you must put each subpath in its own [UIBezierPath](uibezierpath.md) object.

After configuring the geometry and attributes of a Bézier path, you draw the path in the current graphics context using the [- stroke](<uibezierpath/stroke().md>) and [- fill](<uibezierpath/fill().md>) methods. The [- stroke](<uibezierpath/stroke().md>) method traces the outline of the path using the current stroke color and the attributes of the Bézier path object. Similarly, the [- fill](<uibezierpath/fill().md>) method fills in the area enclosed by the path using the current fill color. (You set the stroke and fill color using the [UIColor](uicolor.md) class.)

In addition to using a Bézier path object to draw shapes, you can also use it to define a new clipping region. The [- addClip](<uibezierpath/addclip().md>) method intersects the shape represented by the path object with the current clipping region of the graphics context. During subsequent drawing, only content that lies within the new intersection region is actually rendered to the graphics context.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a Bézier path

- [+ bezierPathWithRect:](<uibezierpath/init(rect_).md>) — Creates and returns a new Bézier path object with a rectangular path.
- [+ bezierPathWithOvalInRect:](<uibezierpath/init(ovalin_).md>) — Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [+ bezierPathWithRoundedRect:cornerRadius:](<uibezierpath/init(roundedrect_cornerradius_).md>) — Creates and returns a new Bézier path object with a rounded rectangular path.
- [+ bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:](<uibezierpath/init(roundedrect_byroundingcorners_cornerradii_).md>) — Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [+ bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:](<uibezierpath/init(arccenter_radius_startangle_endangle_clockwise_).md>) — Creates and returns a new Bézier path object with an arc of a circle.
- [+ bezierPathWithCGPath:](<uibezierpath/init(cgpath_)-833n8.md>) — Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [- bezierPathByReversingPath](<uibezierpath/reversing().md>) — Creates and returns a new Bézier path object with the reversed contents of the current path.
- [- init](<uibezierpath/init().md>) — Creates and returns an empty path object.
- [- initWithCoder:](<uibezierpath/init(coder_).md>) — Creates a Bézier path object from data in an unarchiver.

### Constructing a path

- [- moveToPoint:](<uibezierpath/move(to_).md>) — Moves the path’s current point to the specified location.
- [- addLineToPoint:](<uibezierpath/addline(to_).md>) — Appends a straight line to the path.
- [- addArcWithCenter:radius:startAngle:endAngle:clockwise:](<uibezierpath/addarc(withcenter_radius_startangle_endangle_clockwise_).md>) — Appends an arc to the path.
- [- addCurveToPoint:controlPoint1:controlPoint2:](<uibezierpath/addcurve(to_controlpoint1_controlpoint2_).md>) — Appends a cubic Bézier curve to the path.
- [- addQuadCurveToPoint:controlPoint:](<uibezierpath/addquadcurve(to_controlpoint_).md>) — Appends a quadratic Bézier curve to the path.
- [- closePath](<uibezierpath/close().md>) — Closes the most recent subpath.
- [- removeAllPoints](<uibezierpath/removeallpoints().md>) — Removes all points from the path, effectively deleting all subpaths.
- [- appendPath:](<uibezierpath/append(__).md>) — Appends the contents of the specified path object to the path.
- [CGPath](uibezierpath/cgpath.md) — The Core Graphics representation of the path.
- [currentPoint](uibezierpath/currentpoint.md) — The current point in the graphics path.

### Accessing drawing properties

- [lineWidth](uibezierpath/linewidth.md) — The line width of the path.
- [lineCapStyle](uibezierpath/linecapstyle.md) — The shape of the endpoints of a stroked path.
- [lineJoinStyle](uibezierpath/linejoinstyle.md) — The shape of the joints between connected segments of a stroked path.
- [miterLimit](uibezierpath/miterlimit.md) — The limiting value that helps avoid spikes at junctions between connected line segments.
- [flatness](uibezierpath/flatness.md) — The factor that determines the rendering accuracy for curved path segments.
- [usesEvenOddFillRule](uibezierpath/usesevenoddfillrule.md) — A Boolean value that indicates whether the even-odd winding rule is in use for drawing paths.
- [- setLineDash:count:phase:](<uibezierpath/setlinedash(__count_phase_).md>) — Sets the line-stroking pattern for the path.
- [- getLineDash:count:phase:](<uibezierpath/getlinedash(__count_phase_).md>) — Retrieves the line-stroking pattern for the path.

### Drawing paths

- [- fill](<uibezierpath/fill().md>) — Uses the current drawing properties to paint the region that the path encloses.
- [- fillWithBlendMode:alpha:](<uibezierpath/fill(with_alpha_).md>) — Uses the specified blend mode and transparency values to paint the region that the path encloses.
- [- stroke](<uibezierpath/stroke().md>) — Draws a line along the path using the current drawing properties.
- [- strokeWithBlendMode:alpha:](<uibezierpath/stroke(with_alpha_).md>) — Draws a line along the path using the specified blend mode and transparency values.

### Specifying clipping paths

- [- addClip](<uibezierpath/addclip().md>) — Uses the clipping path of the current graphics context to intersect the region that the path encloses, and makes the resulting shape the current clipping path.

### Performing hit-testing

- [- containsPoint:](<uibezierpath/contains(__).md>) — Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [empty](uibezierpath/isempty.md) — A Boolean value that indicates whether the path has any valid elements.
- [bounds](uibezierpath/bounds.md) — The bounding rectangle of the path.

### Applying transformations

- [- applyTransform:](<uibezierpath/apply(__).md>) — Transforms all points in the path using the specified affine transform matrix.

### Constants

- [UIRectCorner](uirectcorner.md) — The corners of a rectangle.

### Initializers

- [init(CGPath:)](<uibezierpath/init(cgpath_)-7bop1.md>)
- [init(ovalInRect:)](<uibezierpath/init(ovalinrect_).md>)

## See Also

### Paths

- [UIRectFill](<uirectfill(__).md>) — Fills the specified rectangle with the current color.
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — Fills a rectangle with the current fill color using the specified blend mode.
- [UIRectFrame](<uirectframe(__).md>) — Draws a frame around the inside of the specified rectangle.
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — Draws a frame around the inside of a rectangle using the specified blend mode.
