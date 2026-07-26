---
title: ChartProxy
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartproxy
source_url: 'https://developer.apple.com/documentation/charts/chartproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartproxy.json'
content_hash: 'sha256:b25a021768f9181a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ChartProxy

<sub>Structure</sub>

A proxy that you use to access the scales and plot area of a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ChartProxy
```

## Overview

You get a chart proxy from the [chartOverlay(alignment:content:)](<../swiftui/view/chartoverlay(alignment_content_).md>) and [chartBackground(alignment:content:)](<../swiftui/view/chartbackground(alignment_content_).md>) modifiers. You can use the chart proxy to convert data values to screen coordinates or vice-versa.

Below is an example where we convert the screen coordinates from a drag gesture to data values.

```swift
Chart(data) {
    LineMark(
        x: .value("date", $0.date),
        y: .value("price", $0.price)
    )
}
.chartOverlay { proxy in
    GeometryReader { geometry in
        Rectangle().fill(.clear).contentShape(Rectangle())
            .gesture(
                DragGesture()
                    .onChanged { value in
                        // Convert the gesture location to the coordinate space of the plot area.
                        let origin = geometry[proxy.plotAreaFrame].origin
                        let location = CGPoint(
                            x: value.location.x - origin.x,
                            y: value.location.y - origin.y
                        )
                        // Get the x (date) and y (price) value from the location.
                        let (date, price) = proxy.value(at: location, as: (Date, Double).self)
                        print("Location: \(date), \(price)")
                    }
            )
    }
}
```

## Topics

### Instance Properties

- [plotAreaFrame](chartproxy/plotareaframe.md) — An anchor to the frame of the chart’s plot.
- [plotAreaSize](chartproxy/plotareasize.md) — The size of the plot in the chart.
- [plotContainerFrame](chartproxy/plotcontainerframe.md) — An anchor to the frame of the chart’s plot container, or `nil` if there is no chart in the context of the chart proxy.
- [plotFrame](chartproxy/plotframe.md) — An anchor to the frame of the chart’s plot, or `nil` if there is no chart in the context of the chart proxy.
- [plotSize](chartproxy/plotsize.md) — The size of the plot in the chart.

### Instance Methods

- [angle(at:)](<chartproxy/angle(at_).md>) — Returns the angle relative to the plot area center, where the 12 o’clock position is interpreted as zero degrees, increasing clockwise.
- [foregroundStyle(for:)](<chartproxy/foregroundstyle(for_).md>) — Returns the foreground style for the given data value. Returns `nil` if the foreground style scale is unavailable, or the value is invalid.
- [foregroundStyleDomain(dataType:)](<chartproxy/foregroundstyledomain(datatype_).md>)
- [lineStyle(for:)](<chartproxy/linestyle(for_).md>) — Returns the line style for the given data value. Returns `nil` if the line style scale is unavailable, or the value is invalid.
- [lineStyleDomain(dataType:)](<chartproxy/linestyledomain(datatype_).md>)
- [position(for:)](<chartproxy/position(for_).md>) — Returns the x and y positions as a `CGPoint` for the given data values, or `nil` if either the X or the y scale is unavailable or if any data value is invalid. The returned position is relative to the plot.
- [position(forX:)](<chartproxy/position(forx_).md>) — Returns the x position for the given data value, or `nil` if the x scale is unavailable or if the data value is invalid. The returned position is relative to the plot.
- [position(forY:)](<chartproxy/position(fory_).md>) — Returns the y position for the given data value, or `nil` if the y scale is unavailable or if the data value is invalid. The returned position is relative to the plot.
- [positionRange(for:)](<chartproxy/positionrange(for_).md>) — Returns the range of x and y positions for the given pair of data values, or `nil` if the y scale is unavailable or if the value is invalid.
- [positionRange(forX:)](<chartproxy/positionrange(forx_).md>) — Returns the range of x position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.
- [positionRange(forY:)](<chartproxy/positionrange(fory_).md>) — Returns the range of y position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.
- [selectAngleValue(at:)](<chartproxy/selectanglevalue(at_).md>)
- [selectXRange(from:to:)](<chartproxy/selectxrange(from_to_).md>)
- [selectXValue(at:)](<chartproxy/selectxvalue(at_).md>)
- [selectYRange(from:to:)](<chartproxy/selectyrange(from_to_).md>)
- [selectYValue(at:)](<chartproxy/selectyvalue(at_).md>)
- [symbol(for:)](<chartproxy/symbol(for_).md>) — Returns the symbol for the given data value. Returns `nil` if the symbol scale is unavailable, or the value is invalid.
- [symbolDomain(dataType:)](<chartproxy/symboldomain(datatype_).md>)
- [symbolSize(for:)](<chartproxy/symbolsize(for_).md>) — Returns the symbol size for the given data value. Returns `nil` if the symbol size scale is unavailable, or the value is invalid.
- [symbolSizeDomain(dataType:)](<chartproxy/symbolsizedomain(datatype_).md>)
- [value(at:as:)](<chartproxy/value(at_as_).md>) — Returns the data values at the given position, or `nil` if the position does not correspond to a valid Y value.
- [value(atAngle:as:)](<chartproxy/value(atangle_as_).md>) — Returns the data value at the given angle, or `nil` if the angle does not correspond to a valid data value.
- [value(atX:as:)](<chartproxy/value(atx_as_).md>) — Returns the data value at the given x position, or `nil` if the position does not correspond to a valid X value.
- [value(atY:as:)](<chartproxy/value(aty_as_).md>) — Returns the data value at the given y position, or `nil` if the position does not correspond to a valid Y value.
- [xDomain(dataType:)](<chartproxy/xdomain(datatype_).md>)
- [yDomain(dataType:)](<chartproxy/ydomain(datatype_).md>)

## See Also

### Chart management

- [ChartPlotContent](chartplotcontent.md) — A view that represents a chart’s plot area.
