---
title: 'valueAligned(matching:majorAlignment:limitBehavior:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartscrolltargetbehavior/valuealigned(matching:majoralignment:limitbehavior:)'
source_url: 'https://developer.apple.com/documentation/charts/chartscrolltargetbehavior/valuealigned(matching:majoralignment:limitbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartscrolltargetbehavior/valuealigned%28matching%3Amajoralignment%3Alimitbehavior%3A%29.json'
content_hash: 'sha256:ad5fda1afe3e6da7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartScrollTargetBehavior](../chartscrolltargetbehavior.md)

# valueAligned(matching:majorAlignment:limitBehavior:)

<sub>Type Method</sub>

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func valueAligned(matching components: DateComponents, majorAlignment: MajorValueAlignment<Date>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic) -> ValueAlignedChartScrollTargetBehavior where Self == ValueAlignedChartScrollTargetBehavior
```

## Parameters

- `components` — The components to search for when aligning after the user finishes scrolling.

- `majorAlignment` — The behavior for aligning to major values. When the user swipes on the chart, the chart will snap to the next or previous major unit depending on the swipe direction. When enabled, the default major unit is a page.

- `limitBehavior` — The scroll limit behavior.
