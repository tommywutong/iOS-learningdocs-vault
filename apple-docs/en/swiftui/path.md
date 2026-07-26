---
title: Path
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/path
source_url: 'https://developer.apple.com/documentation/swiftui/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path.json'
content_hash: 'sha256:f2c91c8da0d759a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Path

<sub>Structure</sub>

The outline of a 2D shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Path
```

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [LosslessStringConvertible](../swift/losslessstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Shape](shape.md), [View](view.md)

## Topics

### Creating a path

- [init()](<path/init().md>) — Creates an empty path.
- [init(_:)](<path/init(__).md>) — Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn:)](<path/init(ellipsein_).md>) — Creates a path as an ellipse within the given rectangle.
- [init(roundedRect:cornerRadius:style:)](<path/init(roundedrect_cornerradius_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerSize:style:)](<path/init(roundedrect_cornersize_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerRadii:style:)](<path/init(roundedrect_cornerradii_style_).md>) — Creates a path as the given rounded rectangle, which may have uneven corner radii.

### Getting the path’s characteristics

- [boundingRect](path/boundingrect.md) — A rectangle containing all path segments.
- [cgPath](path/cgpath.md) — An immutable path representing the elements in the path.
- [contains(_:eoFill:)](<path/contains(__eofill_).md>) — Returns true if the path contains a specified point.
- [currentPoint](path/currentpoint.md) — Returns the last point in the path, or nil if the path contains no points.
- [description](path/description.md) — A description of the path that may be used to recreate the path via `init?(_:)`.
- [isEmpty](path/isempty.md) — A Boolean value indicating whether the path contains zero elements.

### Drawing a path

- [move(to:)](<path/move(to_).md>) — Begins a new subpath at the specified point.
- [addArc(center:radius:startAngle:endAngle:clockwise:transform:)](<path/addarc(center_radius_startangle_endangle_clockwise_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and angles.
- [addArc(tangent1End:tangent2End:radius:transform:)](<path/addarc(tangent1end_tangent2end_radius_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [addCurve(to:control1:control2:)](<path/addcurve(to_control1_control2_).md>) — Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [addEllipse(in:transform:)](<path/addellipse(in_transform_).md>) — Adds an ellipse that fits inside the specified rectangle to the path.
- [addLine(to:)](<path/addline(to_).md>) — Appends a straight line segment from the current point to the specified point.
- [addLines(_:)](<path/addlines(__).md>) — Adds a sequence of connected straight-line segments to the path.
- [addPath(_:transform:)](<path/addpath(__transform_).md>) — Appends another path value to this path.
- [addQuadCurve(to:control:)](<path/addquadcurve(to_control_).md>) — Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [addRect(_:transform:)](<path/addrect(__transform_).md>) — Adds a rectangular subpath to the path.
- [addRects(_:transform:)](<path/addrects(__transform_).md>) — Adds a set of rectangular subpaths to the path.
- [addRelativeArc(center:radius:startAngle:delta:transform:)](<path/addrelativearc(center_radius_startangle_delta_transform_).md>) — Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [addRoundedRect(in:cornerSize:style:transform:)](<path/addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [closeSubpath()](<path/closesubpath().md>) — Closes and completes the current subpath.

### Transforming the path

- [applying(_:)](<path/applying(__).md>) — Returns a path constructed by applying the transform to all points of the path.
- [offsetBy(dx:dy:)](<path/offsetby(dx_dy_).md>) — Returns a path constructed by translating all its points.
- [trimmedPath(from:to:)](<path/trimmedpath(from_to_).md>) — Returns a partial copy of the path.

### Performing operations on the path

- [addRoundedRect(in:cornerSize:style:transform:)](<path/addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [intersection(_:eoFill:)](<path/intersection(__eofill_).md>) — Returns a new path with filled regions common to both paths.
- [lineIntersection(_:eoFill:)](<path/lineintersection(__eofill_).md>) — Returns a new path with a line from this path that overlaps the filled regions of the given path.
- [lineSubtraction(_:eoFill:)](<path/linesubtraction(__eofill_).md>) — Returns a new path with a line from this path that does not overlap the filled region of the given path.
- [normalized(eoFill:)](<path/normalized(eofill_).md>) — Returns a new weakly-simple copy of this path.
- [subtracting(_:eoFill:)](<path/subtracting(__eofill_).md>) — Returns a new path with filled regions from this path that are not in the given path.
- [symmetricDifference(_:eoFill:)](<path/symmetricdifference(__eofill_).md>) — Returns a new path with filled regions either from this path or the given path, but not in both.
- [union(_:eoFill:)](<path/union(__eofill_).md>) — Returns a new path with filled regions in either this path or the given path.

### Operating over path elements

- [forEach(_:)](<path/foreach(__).md>) — Calls `body` with each element in the path.
- [Element](path/element.md) — An element of a path.

### Applying a style

- [strokedPath(_:)](<path/strokedpath(__).md>) — Returns a stroked copy of the path using `style` to define how the stroked outline is created.

### Instance Methods

- [addRoundedRect(in:cornerRadii:style:transform:)](<path/addroundedrect(in_cornerradii_style_transform_).md>) — Adds a rounded rectangle with uneven corners to the path.
