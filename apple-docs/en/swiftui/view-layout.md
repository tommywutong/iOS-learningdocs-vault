---
title: Layout modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-layout
source_url: 'https://developer.apple.com/documentation/swiftui/view-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-layout.json'
content_hash: 'sha256:e679cabe1b42139f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Layout modifiers

<sub>API Collection</sub>

Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.

## Overview

Use layout modifiers to fine tune the placement of views in a view hierarchy. You can adjust or constrain the size, position, and alignment of a view. You can also add padding around a view, and indicate how the view interacts with system-defined safe areas.

To get started arranging views, see [Layout fundamentals](layout-fundamentals.md). To make adjustments to a basic layout, see [Layout adjustments](layout-adjustments.md).

## Topics

### Size

- [frame(width:height:alignment:)](<view/frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(depth:alignment:)](<view/frame(depth_alignment_).md>) — Positions this view within an invisible frame with the specified depth.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<view/frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<view/frame(mindepth_idealdepth_maxdepth_alignment_).md>) — Positions this view within an invisible frame having the specified depth constraints.
- [containerRelativeFrame(_:alignment:)](<view/containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:alignment:_:)](<view/containerrelativeframe(__alignment___).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<view/containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<view/fixedsize().md>) — Fixes this view at its ideal size.
- [fixedSize(horizontal:vertical:)](<view/fixedsize(horizontal_vertical_).md>) — Fixes this view at its ideal size in the specified dimensions.
- [layoutPriority(_:)](<view/layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
- [containerCornerOffset(_:sizeToFit:)](<view/containercorneroffset(__sizetofit_).md>) — Adjusts the view’s layout to avoid the container view’s corner insets for the specified edges.

### Position

- [position(_:)](<view/position(__).md>) — Positions the center of this view at the specified point in its parent’s coordinate space.
- [position(x:y:)](<view/position(x_y_).md>) — Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [offset(_:)](<view/offset(__).md>) — Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](<view/offset(x_y_).md>) — Offset this view by the specified horizontal and vertical distances.
- [offset(z:)](<view/offset(z_).md>) — Brings a view forward in Z by the provided distance in points.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.

### Alignment

- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — Sets the view’s horizontal alignment.

### Padding and spacing

- [padding(_:)](<view/padding(__).md>) — Adds a different padding amount to each edge of this view.
- [padding(_:_:)](<view/padding(____).md>) — Adds an equal padding amount to specific edges of this view.
- [padding3D(_:)](<view/padding3d(__).md>) — Pads this view using the edge insets you specify.
- [padding3D(_:_:)](<view/padding3d(____).md>) — Pads this view using the edge insets you specify.
- [listRowInsets(_:)](<view/listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<view/listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [scenePadding(_:)](<view/scenepadding(__).md>) — Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [scenePadding(_:edges:)](<view/scenepadding(__edges_).md>) — Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [listRowSpacing(_:)](<view/listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<view/listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](list.md) to a custom value.
- [listSectionMargins(_:_:)](<view/listsectionmargins(____).md>) — Set the section margins for the specific edges.

### Grid configuration

- [gridCellColumns(_:)](<view/gridcellcolumns(__).md>) — Tells a view that acts as a cell in a grid to span the specified number of columns.
- [gridCellAnchor(_:)](<view/gridcellanchor(__).md>) — Specifies a custom alignment anchor for a view that acts as a grid cell.
- [gridCellUnsizedAxes(_:)](<view/gridcellunsizedaxes(__).md>) — Asks grid layouts not to offer the view extra size in the specified axes.
- [gridColumnAlignment(_:)](<view/gridcolumnalignment(__).md>) — Overrides the default horizontal alignment of the grid column that the view appears in.

### Safe area and margins

- [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) — Expands the safe area of a view.
- [ignoresSafeArea(_:edges:alignment:)](<view/ignoressafearea(__edges_alignment_).md>) — Expands the safe area of a view aligning content within the new bounds using the provided alignment. _(beta)_
- [safeAreaInset(edge:alignment:spacing:content:)](<view/safeareainset(edge_alignment_spacing_content_).md>) — Shows the specified content beside the modified view.
- [safeAreaBar(edge:alignment:spacing:content:)](<view/safeareabar(edge_alignment_spacing_content_).md>) — Shows the specified content as a custom bar beside the modified view.
- [safeAreaPadding(_:)](<view/safeareapadding(__).md>) — Adds the provided insets into the safe area of this view.
- [safeAreaPadding(_:_:)](<view/safeareapadding(____).md>) — Adds the provided insets into the safe area of this view.
- [contentMargins(_:for:)](<view/contentmargins(__for_).md>) — Configures the content margin for a provided placement.
- [contentMargins(_:_:for:)](<view/contentmargins(____for_).md>) — Configures the content margin for a provided placement.

### Layer order

- [zIndex(_:)](<view/zindex(__).md>) — Controls the display order of overlapping views.

### Layout direction

- [layoutDirectionBehavior(_:)](<view/layoutdirectionbehavior(__).md>) — Sets the behavior of this view for different layout directions.

### Custom layout characteristics

- [layoutValue(key:value:)](<view/layoutvalue(key_value_).md>) — Associates a value with a custom layout property.
- [containerValue(_:_:)](<view/containervalue(____).md>) — Sets a particular container value of a view.

## See Also

### Drawing views

- [Style modifiers](view-style-modifiers.md) — Apply built-in styles to different types of views.
- [Graphics and rendering modifiers](view-graphics-and-rendering.md) — Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.
