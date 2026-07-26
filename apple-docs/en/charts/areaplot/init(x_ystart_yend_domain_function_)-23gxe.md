---
title: 'init(x:yStart:yEnd:domain:function:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areaplot/init(x:ystart:yend:domain:function:)-23gxe'
source_url: 'https://developer.apple.com/documentation/charts/areaplot/init(x:ystart:yend:domain:function:)-23gxe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areaplot/init%28x%3Aystart%3Ayend%3Adomain%3Afunction%3A%29-23gxe.json'
content_hash: 'sha256:f90f5f85bc71e0ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaPlot](../areaplot.md)

# init(x:yStart:yEnd:domain:function:)

<sub>Initializer</sub>

Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<S1, S2, S3>(x: S1, yStart: S2, yEnd: S3, domain: ClosedRange<Double>? = nil, function: @escaping @Sendable (Double) -> (yStart: Double, yEnd: Double)) where S1 : StringProtocol, S2 : StringProtocol, S3 : StringProtocol
```

## Discussion

Parameters:

- x: The localized string key for the x label.
- yStart: The localized string key for the start label.
- yEnd: The localized string key for the end label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph. Returns a tuple of (yStart: yStart, yEnd: yEnd).

> [!note] Note
> For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

### Plotting functions

- [init(x:y:domain:function:)](<init(x_y_domain_function_)-2fab1.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<init(x_y_domain_function_)-1jmpp.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<init(x_y_domain_function_)-etud.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<init(x_y_domain_function_)-39eit.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:yStart:yEnd:domain:function:)](<init(x_ystart_yend_domain_function_)-etcn.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x:yStart:yEnd:domain:function:)](<init(x_ystart_yend_domain_function_)-9gui6.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x:yStart:yEnd:domain:function:)](<init(x_ystart_yend_domain_function_)-5akqm.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
