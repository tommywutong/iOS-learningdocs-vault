---
title: PlottableValue
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/plottablevalue
source_url: 'https://developer.apple.com/documentation/charts/plottablevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottablevalue.json'
content_hash: 'sha256:a5a997be09e63f57'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# PlottableValue

<sub>Structure</sub>

Labeled data that you plot in a chart using marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PlottableValue<Value> where Value : Plottable
```

## Overview

Provide a `PlottableValue` to a `Mark` property (e.g., x, y, foregroundStyle) to plot data values with the mark property.

> [!important] Important
> The data type must conform to [Plottable](plottable.md). This is a numeric value like a [Double](../swift/double.md) or [Int16](../swift/int16.md) for quantitative data, [Date](../foundation/date.md) for temporal data, or [String](../swift/string.md) for categorical data.

You can use the `.value("Category", \.category)` shorthand to create a `PlottableValue`. The example below plots category, value, and group with the bar mark’s x, y, and foregroundStyle.

```swift
struct Bar {
    let category: String
    let value: Double
    let group: String
}

let data: [Bar] = [
    Bar(category: "A", value: 20, group: "Group 1"),
    Bar(category: "A", value: 30, group: "Group 2"),
    Bar(category: "A", value: 10, group: "Group 3"),
    Bar(category: "B", value: 40, group: "Group 1"),
    Bar(category: "B", value: 20, group: "Group 2"),
    Bar(category: "B", value: 10, group: "Group 3"),
    //...
]

var body: some View {
    Chart(data) {
        BarMark(
            x: .value("Category", $0.category),
            y: .value("Quantity", $0.value)
        )
        .foregroundStyle(.value("Group", $0.group))
    }
}
```

## Topics

### Type Methods

- [value(_:_:)](<plottablevalue/value(____)-13lvv.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-3sze5.md>) — Creates a parameter value with label key and value.
- [value(_:_:)](<plottablevalue/value(____)-4qa4d.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-6jxfn.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-6p2ls.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-70xhu.md>) — Creates a parameter value with label key and value.
- [value(_:_:)](<plottablevalue/value(____)-7ciwx.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-7ed58.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-7k0m0.md>) — Creates a parameter value with label key and value.
- [value(_:_:)](<plottablevalue/value(____)-8bsvd.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-9bdsw.md>) — Creates a parameter value with label and value.
- [value(_:_:)](<plottablevalue/value(____)-f1kk.md>) — Creates a parameter value with label and value.
- [value(_:_:unit:calendar:)](<plottablevalue/value(____unit_calendar_)-1rtpi.md>) — Creates a parameter value with label and value.
- [value(_:_:unit:calendar:)](<plottablevalue/value(____unit_calendar_)-2r0fo.md>) — Creates a parameter value with label and value.
- [value(_:_:unit:calendar:)](<plottablevalue/value(____unit_calendar_)-8f7fe.md>) — Creates a parameter value with label key and value.
- [value(_:_:unit:calendar:)](<plottablevalue/value(____unit_calendar_)-liyc.md>) — Creates a parameter value with label and value.

## See Also

### Labeled data

- [Plottable](plottable.md) — A type that can serve as data to plot in a chart.
