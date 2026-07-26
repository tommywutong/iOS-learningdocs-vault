---
title: 'init(x:y:domain:function:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/lineplot/init(x:y:domain:function:)-6gv5v'
source_url: 'https://developer.apple.com/documentation/charts/lineplot/init(x:y:domain:function:)-6gv5v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/lineplot/init%28x%3Ay%3Adomain%3Afunction%3A%29-6gv5v.json'
content_hash: 'sha256:716cb2b5b3db679f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [LinePlot](../lineplot.md)

# init(x:y:domain:function:)

<sub>Initializer</sub>

Creates a mark that graphs a function y = f(x).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>? = nil, function: @escaping @Sendable (Double) -> Double) where S1 : StringProtocol, S2 : StringProtocol
```

## Discussion

Parameters:

- x: The x label.
- y: The y label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph.

> [!note] Note
> For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

### Plotting functions

- [init(x:y:domain:function:)](<init(x_y_domain_function_)-6m9gg.md>) — Creates a mark that graphs a function y = f(x).
- [init(x:y:domain:function:)](<init(x_y_domain_function_)-1135f.md>) — Creates a mark that graphs a function y = f(x).
- [init(x:y:domain:function:)](<init(x_y_domain_function_)-17i43.md>) — Creates a mark that graphs a function y = f(x).
