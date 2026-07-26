---
title: CGMutablePath
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgmutablepath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmutablepath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmutablepath.json'
content_hash: 'sha256:3d99642f90eaf641'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGMutablePath

<sub>Class</sub>

A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGMutablePath
```

## Overview

Neither `CGPath` nor [CGMutablePath](cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [CGContextAddPath](<cgcontext/addpath(__).md>) and then call one of the context’s drawing functions—see [CGContext](cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a _subpath_. A subpath has an ordered set of _path elements_ that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a _starting point_, which is the first point in the subpath. The path also maintains a _current point_, which is the last point in the last subpath.

To append a new subpath onto a mutable path, your application typically calls [CGPathMoveToPoint](cgpathmovetopoint.md) to set the subpath’s starting point and initial current point, followed by a series of “add” calls (such as [CGPathAddLineToPoint](cgpathaddlinetopoint.md)) to add line segments and curves to the subpath. As segments or curves are added to the subpath, the subpath’s current point is updated to point to the end of the last segment or curve to be added. The lines and curves of a subpath are always connected, but they are not required to form a closed set of lines. Your application explicitly closes a subpath by calling [CGPathCloseSubpath](<cgmutablepath/closesubpath().md>). Closing the subpath adds a line segment that terminates at the subpath’s starting point, and also changes how those lines are rendered—for more information see [Paths](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Relationships

- **Inherits From**: [CGPath](cgpath.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Graphics Paths

- [CGPathCreateMutable](<cgmutablepath/init().md>) — Creates a mutable graphics path.

### Copying a Graphics Path

- [CGPathCreateMutableCopy](<cgpath/mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
- [CGPathCreateMutableCopyByTransformingPath](<cgpath/mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.

### Constructing a Graphics Path

- [move(to:transform:)](<cgmutablepath/move(to_transform_).md>) — Begins a new subpath at the specified point.
- [addLine(to:transform:)](<cgmutablepath/addline(to_transform_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(between:transform:)](<cgmutablepath/addlines(between_transform_).md>) — Adds a sequence of connected straight-line segments to the path.
- [addRect(_:transform:)](<cgmutablepath/addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<cgmutablepath/addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addEllipse(in:transform:)](<cgmutablepath/addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle.
- [addRoundedRect(in:cornerWidth:cornerHeight:transform:)](<cgmutablepath/addroundedrect(in_cornerwidth_cornerheight_transform_).md>) — Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<cgmutablepath/addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](<cgmutablepath/addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<cgmutablepath/addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addCurve(to:control1:control2:transform:)](<cgmutablepath/addcurve(to_control1_control2_transform_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addQuadCurve(to:control:transform:)](<cgmutablepath/addquadcurve(to_control_transform_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addPath(_:transform:)](<cgmutablepath/addpath(__transform_).md>) — Appends another path object to the path.
- [CGPathCloseSubpath](<cgmutablepath/closesubpath().md>) — Closes and completes a subpath in a mutable graphics path.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### 2D Drawing

- [CGContext](cgcontext.md) — A Quartz 2D drawing environment.
- [CGImage](cgimage.md) — A bitmap image or image mask.
- [CGPath](cgpath.md) — An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGLayer](cglayer.md) — An offscreen context for reusing content drawn with Core Graphics.
