---
title: Shape
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape
source_url: 'https://developer.apple.com/documentation/swiftui/shape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape.json'
content_hash: 'sha256:0968820bf2743178'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Shape

<sub>Protocol</sub>

A 2D shape that you can use when drawing a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated protocol Shape : Sendable, Animatable, View
```

## Overview

Shapes without an explicit fill or stroke get a default fill based on the foreground color.

You can define shapes in relation to an implicit frame of reference, such as the natural size of the view that contains it. Alternatively, you can define shapes in terms of absolute coordinates.

## Relationships

- **Inherits From**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](view.md)

- **Inherited By**: [InsettableShape](insettableshape.md), [RoundedRectangularShape](roundedrectangularshape.md)

- **Conforming Types**: [AnyShape](anyshape.md), [ButtonBorderShape](buttonbordershape.md), [Capsule](capsule.md), [Circle](circle.md), [ConcentricRectangle](concentricrectangle.md), [ContainerRelativeShape](containerrelativeshape.md), [DefaultGlassEffectShape](defaultglasseffectshape.md), [Ellipse](ellipse.md), [OffsetShape](offsetshape.md), [Path](path.md), [Rectangle](rectangle.md), [RotatedShape](rotatedshape.md), [RoundedRectangle](roundedrectangle.md), [ScaledShape](scaledshape.md), [TextInputBorderShape](textinputbordershape.md), [TransformedShape](transformedshape.md), [UnevenRoundedRectangle](unevenroundedrectangle.md)

## Topics

### Getting standard shapes

- [buttonBorder](shape/buttonborder.md) — A shape that defers to the environment to determine the resolved button border shape.
- [capsule](shape/capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [capsule(style:)](<shape/capsule(style_).md>) — A capsule shape aligned inside the frame of the view containing it.
- [circle](shape/circle.md) — A circle centered on the frame of the view containing it.
- [containerRelative](shape/containerrelative.md) — A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [ellipse](shape/ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [textInputBorder](shape/textinputborder.md) — A shape that defers to the environment to determine the resolved text input border shape. _(beta)_

### Getting rectangles

- [rect](shape/rect.md) — A rectangular shape aligned inside the frame of the view containing it.
- [rect(cornerRadii:style:)](<shape/rect(cornerradii_style_).md>) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [rect(cornerRadius:style:)](<shape/rect(cornerradius_style_).md>) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [rect(corners:isUniform:)](<shape/rect(corners_isuniform_).md>) — Creates a rectangle with the same corner style set on four corners.
- [rect(cornerSize:style:)](<shape/rect(cornersize_style_).md>) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [rect(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](<shape/rect(topleadingcorner_toptrailingcorner_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with individual styles for each corner.
- [rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)](<shape/rect(topleadingradius_bottomleadingradius_bottomtrailingradius_toptrailingradius_style_).md>) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](<shape/rect(uniformbottomcorners_topleadingcorner_toptrailingcorner_).md>) — Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
- [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](<shape/rect(uniformleadingcorners_toptrailingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
- [rect(uniformLeadingCorners:uniformTrailingCorners:)](<shape/rect(uniformleadingcorners_uniformtrailingcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
- [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](<shape/rect(uniformtopcorners_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
- [rect(uniformTopCorners:uniformBottomCorners:)](<shape/rect(uniformtopcorners_uniformbottomcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
- [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](<shape/rect(uniformtrailingcorners_topleadingcorner_bottomleadingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.

### Defining a shape’s size and path

- [sizeThatFits(_:)](<shape/sizethatfits(__).md>) — Returns the size of the view that will render the shape, given a proposed size.
- [path(in:)](<shape/path(in_).md>) — Describes this shape as a path within a rectangular frame of reference.

### Transforming a shape

- [trim(from:to:)](<shape/trim(from_to_).md>) — Trims this shape by a fractional amount based on its representation as a path.
- [transform(_:)](<shape/transform(__).md>) — Applies an affine transform to this shape.
- [size(_:)](<shape/size(__).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(_:anchor:)](<shape/size(__anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [size(width:height:)](<shape/size(width_height_).md>) — Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [size(width:height:anchor:)](<shape/size(width_height_anchor_).md>) — Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [scale(_:anchor:)](<shape/scale(__anchor_).md>) — Scales this shape without changing its bounding frame.
- [scale(x:y:anchor:)](<shape/scale(x_y_anchor_).md>) — Scales this shape without changing its bounding frame.
- [rotation(_:anchor:)](<shape/rotation(__anchor_).md>) — Rotates this shape around an anchor point at the angle you specify.
- [offset(_:)](<shape/offset(__).md>) — Changes the relative position of this shape using the specified point.
- [offset(x:y:)](<shape/offset(x_y_).md>) — Changes the relative position of this shape using the specified point.

### Setting the stroke characteristics

- [stroke(_:lineWidth:)](<shape/stroke(__linewidth_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:lineWidth:antialiased:)](<shape/stroke(__linewidth_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(lineWidth:)](<shape/stroke(linewidth_).md>) — Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [stroke(_:style:)](<shape/stroke(__style_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(_:style:antialiased:)](<shape/stroke(__style_antialiased_).md>) — Traces the outline of this shape with a color or gradient.
- [stroke(style:)](<shape/stroke(style_).md>) — Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.

### Filling a shape

- [fill(_:style:)](<shape/fill(__style_).md>) — Fills this shape with a color or gradient.
- [fill(style:)](<shape/fill(style_).md>) — Fills this shape with the foreground color.

### Setting the role

- [role](shape/role.md) — An indication of how to style a shape.

### Indicating a layout direction

- [layoutDirectionBehavior](shape/layoutdirectionbehavior.md) — Returns the behavior this shape should use for different layout directions.

### Performing operations on a shape

- [intersection(_:eoFill:)](<shape/intersection(__eofill_).md>) — Returns a new shape with filled regions common to both shapes.
- [lineIntersection(_:eoFill:)](<shape/lineintersection(__eofill_).md>) — Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [lineSubtraction(_:eoFill:)](<shape/linesubtraction(__eofill_).md>) — Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [subtracting(_:eoFill:)](<shape/subtracting(__eofill_).md>) — Returns a new shape with filled regions from this shape that are not in the given shape.
- [symmetricDifference(_:eoFill:)](<shape/symmetricdifference(__eofill_).md>) — Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [union(_:eoFill:)](<shape/union(__eofill_).md>) — Returns a new shape with filled regions in either this shape or the given shape.

## See Also

### Defining shape behavior

- [ShapeView](shapeview.md) — A view that provides a shape that you can use for drawing operations.
- [AnyShape](anyshape.md) — A type-erased shape value.
- [ShapeRole](shaperole.md) — Ways of styling a shape.
- [StrokeStyle](strokestyle.md) — The characteristics of a stroke that traces a path.
- [StrokeShapeView](strokeshapeview.md) — A shape provider that strokes its shape.
- [StrokeBorderShapeView](strokebordershapeview.md) — A shape provider that strokes the border of its shape.
- [FillStyle](fillstyle.md) — A style for rasterizing vector shapes.
- [FillShapeView](fillshapeview.md) — A shape provider that fills its shape.
