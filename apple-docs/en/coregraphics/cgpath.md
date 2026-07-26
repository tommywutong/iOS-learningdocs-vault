---
title: CGPath
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath.json'
content_hash: 'sha256:39eff9f60a2c77dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPath

<sub>Class</sub>

An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGPath
```

## Overview

Neither `CGPath` nor [CGMutablePath](cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [CGContextAddPath](<cgcontext/addpath(__).md>) and then call one of the context’s drawing functions—see [CGContext](cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a _subpath_. A subpath has an ordered set of _path elements_ that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a _starting point_, which is the first point in the subpath. The path also maintains a _current point_, which is the last point in the last subpath.

## Relationships

- **Inherited By**: [CGMutablePath](cgmutablepath.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Graphics Paths

- [CGPathCreateWithRect](<cgpath/init(rect_transform_).md>) — Create an immutable path of a rectangle.
- [CGPathCreateWithEllipseInRect](<cgpath/init(ellipsein_transform_).md>) — Create an immutable path of an ellipse.
- [CGPathCreateWithRoundedRect](<cgpath/init(roundedrect_cornerwidth_cornerheight_transform_).md>) — Create an immutable path of a rounded rectangle.

### Copying a Graphics Path

- [CGPathCreateCopy](<cgpath/copy().md>) — Creates an immutable copy of a graphics path.
- [CGPathCreateCopyByTransformingPath](<cgpath/copy(using_).md>) — Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [copy(dashingWithPhase:lengths:transform:)](<cgpath/copy(dashingwithphase_lengths_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [copy(strokingWithWidth:lineCap:lineJoin:miterLimit:transform:)](<cgpath/copy(strokingwithwidth_linecap_linejoin_miterlimit_transform_).md>) — Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [CGPathCreateMutableCopy](<cgpath/mutablecopy().md>) — Creates a mutable copy of an existing graphics path.
- [CGPathCreateMutableCopyByTransformingPath](<cgpath/mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.

### Examining a Graphics Path

- [CGPathGetBoundingBox](cgpath/boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](cgpath/boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](cgpath/currentpoint.md) — Returns the current point in a graphics path.
- [contains(_:using:transform:)](<cgpath/contains(__using_transform_).md>) — Returns whether the specified point is interior to the path.
- [CGPathIsEmpty](cgpath/isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<cgpath/isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.

### Applying a Function to the Elements of a Path

- [CGPathApply](<cgpath/apply(info_function_).md>) — For each element in a graphics path, calls a custom applier function.
- [CGPathApplierFunction](cgpathapplierfunction.md) — Defines a callback function that can view an element in a graphics path.
- [CGPathElement](cgpathelement.md) — A data structure that provides information about a path element.
- [CGPathElementType](cgpathelementtype.md) — The type of element found in a path.

### Working with Core Foundation Types

- [CGPathGetTypeID](cgpath/typeid.md) — Returns the Core Foundation type identifier for Core Graphics paths.

### Instance Methods

- [CGPathApplyWithBlock](<cgpath/applywithblock(__).md>)
- [componentsSeparated(using:)](<cgpath/componentsseparated(using_).md>)
- [flattened(threshold:)](<cgpath/flattened(threshold_).md>)
- [intersection(_:using:)](<cgpath/intersection(__using_).md>)
- [intersects(_:using:)](<cgpath/intersects(__using_).md>)
- [lineIntersection(_:using:)](<cgpath/lineintersection(__using_).md>)
- [lineSubtracting(_:using:)](<cgpath/linesubtracting(__using_).md>)
- [normalized(using:)](<cgpath/normalized(using_).md>)
- [subtracting(_:using:)](<cgpath/subtracting(__using_).md>)
- [symmetricDifference(_:using:)](<cgpath/symmetricdifference(__using_).md>)
- [union(_:using:)](<cgpath/union(__using_).md>)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### 2D Drawing

- [CGContext](cgcontext.md) — A Quartz 2D drawing environment.
- [CGImage](cgimage.md) — A bitmap image or image mask.
- [CGMutablePath](cgmutablepath.md) — A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [CGLayer](cglayer.md) — An offscreen context for reusing content drawn with Core Graphics.
