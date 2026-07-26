---
title: SwiftUI views for widgets
framework: WidgetKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/swiftui-views
source_url: 'https://developer.apple.com/documentation/widgetkit/swiftui-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/swiftui-views.json'
content_hash: 'sha256:eefedd7670483c34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# SwiftUI views for widgets

Present your app’s content in widgets with SwiftUI views.

## Overview

Widgets can use many, but not all, SwiftUI views to present content. Use the views listed below to implement your widget’s view.

> [!note] Note
> Widgets can’t use UIKit or AppKit views wrapped with [UIViewRepresentable](../swiftui/uiviewrepresentable.md) or [NSViewRepresentable](../swiftui/nsviewrepresentable.md).

## Topics

### Displaying text

- [Displaying dynamic dates in widgets](displaying-dynamic-dates.md) — Show up-to-date, time-based information in your widget even when it isn’t running.
- [Text](../swiftui/text.md) — A view that displays one or more lines of read-only text.

### Showing images

- [Image](../swiftui/image.md) — A view that displays an image.

### Adding interaction

- [Adding interactivity to widgets and Live Activities](adding-interactivity-to-widgets-and-live-activities.md) — Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [Button](../swiftui/button.md) — A control that initiates an action.
- [Toggle](../swiftui/toggle.md) — A control that toggles between on and off states.

### Adding labels and links

- [Label](../swiftui/label.md) — A standard label for user interface items, consisting of an icon with a title.
- [Link](../swiftui/link.md) — A control for navigating to a URL.

### Stacking views

- [HStack](../swiftui/hstack.md) — A view that arranges its subviews in a horizontal line.
- [VStack](../swiftui/vstack.md) — A view that arranges its subviews in a vertical line.
- [ZStack](../swiftui/zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [LazyHStack](../swiftui/lazyhstack.md) — A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [LazyVStack](../swiftui/lazyvstack.md) — A view that arranges its children in a line that grows vertically, creating items only as needed.

### Arranging views in grids

- [LazyHGrid](../swiftui/lazyhgrid.md) — A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [LazyVGrid](../swiftui/lazyvgrid.md) — A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
- [GridItem](../swiftui/griditem.md) — A description of a row or a column in a lazy grid.

### Enumerating lists

- [ForEach](../swiftui/foreach.md) — A structure that computes views on demand from an underlying collection of identified data.

### Grouping views

- [Group](../swiftui/group.md) — A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [GroupBox](../swiftui/groupbox.md) — A stylized view, with an optional label, that visually collects a logical grouping of content.
- [Section](../swiftui/section.md) — A container view that you can use to add hierarchy within certain views.

### Representing hierarchies

- [OutlineGroup](../swiftui/outlinegroup.md) — A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.

### Adding spacers and dividers

- [Spacer](../swiftui/spacer.md) — A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
- [Divider](../swiftui/divider.md) — A visual element that can be used to separate other content.

### Handling conditional views

- [EmptyView](../swiftui/emptyview.md) — A view that doesn’t contain any content.
- [EquatableView](../swiftui/equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.

### Displaying shapes

- [Rectangle](../swiftui/rectangle.md) — A rectangular shape aligned inside the frame of the view containing it.
- [RoundedRectangle](../swiftui/roundedrectangle.md) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [Circle](../swiftui/circle.md) — A circle centered on the frame of the view containing it.
- [Ellipse](../swiftui/ellipse.md) — An ellipse aligned inside the frame of the view containing it.
- [Capsule](../swiftui/capsule.md) — A capsule shape aligned inside the frame of the view containing it.
- [Path](../swiftui/path.md) — The outline of a 2D shape.

### Transforming views

- [ScaledShape](../swiftui/scaledshape.md) — A shape with a scale transform applied to it.
- [RotatedShape](../swiftui/rotatedshape.md) — A shape with a rotation transform applied to it.
- [OffsetShape](../swiftui/offsetshape.md) — A shape with a translation offset transform applied to it.
- [TransformedShape](../swiftui/transformedshape.md) — A shape with an affine transform applied to it.
- [ContainerRelativeShape](../swiftui/containerrelativeshape.md) — A shape whose dimensions the system calculates from an inset version of the current container shape.

### Styling views

- [Color](../swiftui/color.md) — A representation of a color that adapts to a given context.
- [ImagePaint](../swiftui/imagepaint.md) — A shape style that fills a shape by repeating a region of an image.
- [Gradient](../swiftui/gradient.md) — A color gradient represented as an array of color stops, each having a parametric location value.
- [LinearGradient](../swiftui/lineargradient.md) — A linear gradient.
- [AngularGradient](../swiftui/angulargradient.md) — An angular gradient.
- [RadialGradient](../swiftui/radialgradient.md) — A radial gradient.
- [ForegroundStyle](../swiftui/foregroundstyle.md) — The foreground style in the current context.
- [FillStyle](../swiftui/fillstyle.md) — A style for rasterizing vector shapes.
- [BackgroundStyle](../swiftui/backgroundstyle.md) — The background style in the current context.
- [SelectionShapeStyle](../swiftui/selectionshapestyle.md) — A style used to visually indicate selection following platform conventional colors and behaviors.
- [SeparatorShapeStyle](../swiftui/separatorshapestyle.md) — A style appropriate for foreground separator or border lines.
- [StrokeStyle](../swiftui/strokestyle.md) — The characteristics of a stroke that traces a path.

### Creating 2D graphics

- [Canvas](../swiftui/canvas.md) — A view type that supports immediate mode drawing.

### Managing view geometry

- [GeometryProxy](../swiftui/geometryproxy.md) — A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryReader](../swiftui/geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [ProjectionTransform](../swiftui/projectiontransform.md)

### Substituting views

- [AnyView](../swiftui/anyview.md) — A type-erased view.
- [TupleView](../swiftui/tupleview.md) — A View created from a swift tuple of View values.

## See Also

### Presentation

- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md) — Implement glanceable views with WidgetKit and SwiftUI.
