---
title: Chart view modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-chart-view
source_url: 'https://developer.apple.com/documentation/swiftui/view-chart-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-chart-view.json'
content_hash: 'sha256:0e487fe8c76f7ece'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Chart view modifiers

<sub>API Collection</sub>

Configure charts that you declare with Swift Charts.

## Overview

Use these modifiers to configure a [Chart](../charts/chart.md) view that you add to your SwiftUI app.

## Topics

### Styles

- [chartBackground(alignment:content:)](<view/chartbackground(alignment_content_).md>) — Adds a background to a view that contains a chart.
- [chartForegroundStyleScale(_:)](<view/chartforegroundstylescale(__).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:range:type:)](<view/chartforegroundstylescale(domain_range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:type:)](<view/chartforegroundstylescale(domain_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:mapping:)](<view/chartforegroundstylescale(domain_mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(mapping:)](<view/chartforegroundstylescale(mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(range:type:)](<view/chartforegroundstylescale(range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(type:)](<view/chartforegroundstylescale(type_).md>) — Configures the foreground style scale for charts.
- [chartPlotStyle(content:)](<view/chartplotstyle(content_).md>) — Configures the plot area of charts.

### 3D configuration

- [chart3DCameraProjection(_:)](<view/chart3dcameraprojection(__).md>)
- [chart3DPose(_:)](<view/chart3dpose(__).md>) — Associates a binding to be updated when the 3D chart’s pose is changed by an interaction.
- [chart3DRenderingStyle(_:)](<view/chart3drenderingstyle(__).md>)

### Legends

- [chartLegend(_:)](<view/chartlegend(__).md>) — Configures the legend for charts.
- [chartLegend(position:alignment:spacing:)](<view/chartlegend(position_alignment_spacing_).md>) — Configures the legend for charts.
- [chartLegend(position:alignment:spacing:content:)](<view/chartlegend(position_alignment_spacing_content_).md>) — Configures the legend for charts.

### Overlays

- [chartOverlay(alignment:content:)](<view/chartoverlay(alignment_content_).md>) — Adds an overlay to a view that contains a chart.

### Axes

- [chartXAxis(_:)](<view/chartxaxis(__).md>) — Sets the visibility of the x axis.
- [chartXAxis(content:)](<view/chartxaxis(content_).md>) — Configures the x-axis for charts in the view.
- [chartXAxisStyle(content:)](<view/chartxaxisstyle(content_).md>) — Configures the x axis content of charts.
- [chartYAxis(_:)](<view/chartyaxis(__).md>) — Sets the visibility of the y axis.
- [chartYAxis(content:)](<view/chartyaxis(content_).md>) — Configures the y-axis for charts in the view.
- [chartYAxisStyle(content:)](<view/chartyaxisstyle(content_).md>) — Configures the y axis content of charts.
- [chartZAxis(_:)](<view/chartzaxis(__).md>) — Sets the visibility of the z axis.
- [chartZAxis(content:)](<view/chartzaxis(content_).md>) — Configures the z-axis for 3D charts in the view.

### Axis Labels

- [chartXAxisLabel(_:position:alignment:spacing:)](<view/chartxaxislabel(__position_alignment_spacing_).md>) — Adds x axis label for charts in the view.
- [chartXAxisLabel(position:alignment:spacing:content:)](<view/chartxaxislabel(position_alignment_spacing_content_).md>) — Adds x axis label for charts in the view.
- [chartYAxisLabel(_:position:alignment:spacing:)](<view/chartyaxislabel(__position_alignment_spacing_).md>) — Adds y axis label for charts in the view.
- [chartYAxisLabel(position:alignment:spacing:content:)](<view/chartyaxislabel(position_alignment_spacing_content_).md>) — Adds y axis label for charts in the view.
- [chartZAxisLabel(_:position:alignment:spacing:)](<view/chartzaxislabel(__position_alignment_spacing_).md>) — Adds z axis label for charts in the view. It effects 3D charts only.

### Axis scales

- [chartXScale(domain:range:type:)](<view/chartxscale(domain_range_type_).md>) — Configures the x scale for charts.
- [chartXScale(domain:type:)](<view/chartxscale(domain_type_).md>) — Configures the x scale for charts.
- [chartXScale(range:type:)](<view/chartxscale(range_type_).md>) — Configures the x scale for charts.
- [chartXScale(type:)](<view/chartxscale(type_).md>) — Configures the x scale for charts.
- [chartYScale(domain:range:type:)](<view/chartyscale(domain_range_type_).md>) — Configures the y scale for charts.
- [chartYScale(domain:type:)](<view/chartyscale(domain_type_).md>) — Configures the y scale for charts.
- [chartYScale(range:type:)](<view/chartyscale(range_type_).md>) — Configures the y scale for charts.
- [chartYScale(type:)](<view/chartyscale(type_).md>) — Configures the y scale for charts.
- [chartZScale(domain:range:type:)](<view/chartzscale(domain_range_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(domain:type:)](<view/chartzscale(domain_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(range:type:)](<view/chartzscale(range_type_).md>) — Configures the z scale for 3D charts.

### Symbol scales

- [chartSymbolScale(_:)](<view/chartsymbolscale(__).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(domain:)](<view/chartsymbolscale(domain_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:range:)](<view/chartsymbolscale(domain_range_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:mapping:)](<view/chartsymbolscale(domain_mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(mapping:)](<view/chartsymbolscale(mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(range:)](<view/chartsymbolscale(range_).md>) — Configures the symbol style scale for charts.

### Symbol size scales

- [chartSymbolSizeScale(_:)](<view/chartsymbolsizescale(__).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:range:type:)](<view/chartsymbolsizescale(domain_range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:type:)](<view/chartsymbolsizescale(domain_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:mapping:)](<view/chartsymbolsizescale(domain_mapping_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(mapping:)](<view/chartsymbolsizescale(mapping_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(range:type:)](<view/chartsymbolsizescale(range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(type:)](<view/chartsymbolsizescale(type_).md>) — Configures the symbol size scale for charts.

### Line style scales

- [chartLineStyleScale(_:)](<view/chartlinestylescale(__).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:)](<view/chartlinestylescale(domain_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:range:)](<view/chartlinestylescale(domain_range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(range:)](<view/chartlinestylescale(range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:mapping:)](<view/chartlinestylescale(domain_mapping_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(mapping:)](<view/chartlinestylescale(mapping_).md>) — Configures the line style scale for charts.

### Scrolling

- [chartScrollPosition(initialX:)](<view/chartscrollposition(initialx_).md>) — Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(initialY:)](<view/chartscrollposition(initialy_).md>) — Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(x:)](<view/chartscrollposition(x_).md>) — Associates a binding to be updated when the chart scrolls along the x-axis.
- [chartScrollPosition(y:)](<view/chartscrollposition(y_).md>) — Associates a binding to be updated when the chart scrolls along the y-axis.
- [chartScrollTargetBehavior(_:)](<view/chartscrolltargetbehavior(__).md>) — Sets the scroll behavior of the scrollable chart.
- [chartScrollableAxes(_:)](<view/chartscrollableaxes(__).md>) — Configures the scrollable behavior of charts in this view.

### Selection

- [chartXSelection(range:)](<view/chartxselection(range_).md>)
- [chartXSelection(value:)](<view/chartxselection(value_).md>)
- [chartYSelection(range:)](<view/chartyselection(range_).md>)
- [chartYSelection(value:)](<view/chartyselection(value_).md>)
- [chartZSelection(range:)](<view/chartzselection(range_).md>)
- [chartZSelection(value:)](<view/chartzselection(value_).md>)
- [chartAngleSelection(value:)](<view/chartangleselection(value_).md>)

### Visible domain

- [chartXVisibleDomain(length:)](<view/chartxvisibledomain(length_).md>) — Sets the length of the visible domain in the X dimension.
- [chartYVisibleDomain(length:)](<view/chartyvisibledomain(length_).md>) — Sets the length of the visible domain in the Y dimension.

### Interaction

- [chartGesture(_:)](<view/chartgesture(__).md>)

## See Also

### Configuring view elements

- [Accessibility modifiers](view-accessibility.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md) — Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md) — Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md) — Add and configure supporting views, like toolbars and context menus.
