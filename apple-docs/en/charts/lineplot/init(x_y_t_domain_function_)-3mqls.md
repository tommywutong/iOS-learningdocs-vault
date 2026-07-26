---
title: 'init(x:y:t:domain:function:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/lineplot/init(x:y:t:domain:function:)-3mqls'
source_url: 'https://developer.apple.com/documentation/charts/lineplot/init(x:y:t:domain:function:)-3mqls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/lineplot/init%28x%3Ay%3At%3Adomain%3Afunction%3A%29-3mqls.json'
content_hash: 'sha256:3cf553f28483e0ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [LinePlot](../lineplot.md)

# init(x:y:t:domain:function:)

<sub>Initializer</sub>

Creates a mark that graphs a parametric function (x, y) = f(t).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<S1, S2, S3>(x: S1, y: S2, t: S3, domain: ClosedRange<Double>, function: @escaping @Sendable (Double) -> (x: Double, y: Double)) where S1 : StringProtocol, S2 : StringProtocol, S3 : StringProtocol
```

## Discussion

Parameters:

- x: The localized string key for the x label.
- y: The localized string key for the y label.
- t: The localized string key for the t label.
- domain: The domain of t. Must be a finite domain.
- function: The function to graph. Returns a tuple of (x, y) for a value of t.

> [!note] Note
> For t values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

### Plotting parametric functions

- [init(x:y:t:domain:function:)](<init(x_y_t_domain_function_)-5c4bo.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x:y:t:domain:function:)](<init(x_y_t_domain_function_)-7bvyi.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x:y:t:domain:function:)](<init(x_y_t_domain_function_)-610ta.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
