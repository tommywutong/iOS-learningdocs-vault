---
title: 'init(xUnit:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/valuealignedchartscrolltargetbehavior/init(xunit:yunit:xmajoralignment:ymajoralignment:limitbehavior:)'
source_url: 'https://developer.apple.com/documentation/charts/valuealignedchartscrolltargetbehavior/init(xunit:yunit:xmajoralignment:ymajoralignment:limitbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/valuealignedchartscrolltargetbehavior/init%28xunit%3Ayunit%3Axmajoralignment%3Aymajoralignment%3Alimitbehavior%3A%29.json'
content_hash: 'sha256:922fa99a887ea701'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ValueAlignedChartScrollTargetBehavior](../valuealignedchartscrolltargetbehavior.md)

# init(xUnit:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)

<sub>Initializer</sub>

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(xUnit: X, yUnit: Y, xMajorAlignment: MajorValueAlignment<X>? = nil, yMajorAlignment: MajorValueAlignment<Y>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) where X : Plottable, X : Numeric, Y : Plottable, Y : Numeric
```

## Parameters

- `xUnit` — The alignment unit for the x-axis.

- `yUnit` — The alignment unit for the y-axis.

- `xMajorAlignment` — The behavior for aligning to major values along the x-axis.

- `yMajorAlignment` — The behavior for aligning to major values along the y-axis.

- `limitBehavior` — The scroll limit behavior.
