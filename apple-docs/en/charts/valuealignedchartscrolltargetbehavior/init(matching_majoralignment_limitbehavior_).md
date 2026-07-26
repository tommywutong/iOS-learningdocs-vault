---
title: 'init(matching:majorAlignment:limitBehavior:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/valuealignedchartscrolltargetbehavior/init(matching:majoralignment:limitbehavior:)'
source_url: 'https://developer.apple.com/documentation/charts/valuealignedchartscrolltargetbehavior/init(matching:majoralignment:limitbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/valuealignedchartscrolltargetbehavior/init%28matching%3Amajoralignment%3Alimitbehavior%3A%29.json'
content_hash: 'sha256:70ca4a60f40049b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ValueAlignedChartScrollTargetBehavior](../valuealignedchartscrolltargetbehavior.md)

# init(matching:majorAlignment:limitBehavior:)

<sub>Initializer</sub>

Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(matching components: DateComponents, majorAlignment: MajorValueAlignment<Date>? = nil, limitBehavior: ValueAlignedLimitBehavior = .automatic)
```

## Parameters

- `components` — The components to search for when aligning after the user finishes scrolling.

- `majorAlignment` — The behavior for aligning to major values. When the user swipes on the chart, the chart will snap to the next or previous major unit depending on the swipe direction. When enabled, the default major unit is a page.

- `limitBehavior` — The scroll limit behavior.
