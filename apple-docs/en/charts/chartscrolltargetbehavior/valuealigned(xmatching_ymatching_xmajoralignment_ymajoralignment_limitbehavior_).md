---
title: 'valueAligned(xMatching:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartscrolltargetbehavior/valuealigned(xmatching:ymatching:xmajoralignment:ymajoralignment:limitbehavior:)'
source_url: 'https://developer.apple.com/documentation/charts/chartscrolltargetbehavior/valuealigned(xmatching:ymatching:xmajoralignment:ymajoralignment:limitbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartscrolltargetbehavior/valuealigned%28xmatching%3Aymatching%3Axmajoralignment%3Aymajoralignment%3Alimitbehavior%3A%29.json'
content_hash: 'sha256:e2199c1491bfd90c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartScrollTargetBehavior](../chartscrolltargetbehavior.md)

# valueAligned(xMatching:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)

<sub>Type Method</sub>

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func valueAligned(xMatching xComponents: DateComponents, yMatching yComponents: DateComponents, xMajorAlignment: MajorValueAlignment<Date>? = nil, yMajorAlignment: MajorValueAlignment<Date>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) -> ValueAlignedChartScrollTargetBehavior where Self == ValueAlignedChartScrollTargetBehavior
```

## Parameters

- `xComponents` — The alignment components for the x-axis.

- `yComponents` — The alignment components for the y-axis.

- `xMajorAlignment` — The behavior for aligning to major values along the x-axis.

- `yMajorAlignment` — The behavior for aligning to major values along the y-axis.

- `limitBehavior` — The scroll limit behavior.
