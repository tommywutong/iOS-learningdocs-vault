---
title: ChartScrollTargetBehavior
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartscrolltargetbehavior
source_url: 'https://developer.apple.com/documentation/charts/chartscrolltargetbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartscrolltargetbehavior.json'
content_hash: 'sha256:228a50b564123a54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ChartScrollTargetBehavior

<sub>Protocol</sub>

A type that configures the scroll behavior of charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ChartScrollTargetBehavior : ScrollTargetBehavior
```

## Relationships

- **Inherits From**: [ScrollTargetBehavior](../swiftui/scrolltargetbehavior.md)

- **Conforming Types**: [ValueAlignedChartScrollTargetBehavior](valuealignedchartscrolltargetbehavior.md)

## Topics

### Supporting types

- [MajorValueAlignment](majorvaluealignment.md) — A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.
- [ValueAlignedLimitBehavior](valuealignedlimitbehavior.md) — A type that defines the amount of marks that can be scrolled at a time.
- [ValueAlignedChartScrollTargetBehavior](valuealignedchartscrolltargetbehavior.md) — A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

### Instance Methods

- [updateTarget(_:context:)](<chartscrolltargetbehavior/updatetarget(__context_).md>)

### Type Methods

- [valueAligned(matching:majorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(matching_majoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [valueAligned(unit:majorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(unit_majoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [valueAligned(xMatching:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(xmatching_ymatching_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [valueAligned(xMatching:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(xmatching_yunit_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [valueAligned(xUnit:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(xunit_ymatching_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [valueAligned(xUnit:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)](<chartscrolltargetbehavior/valuealigned(xunit_yunit_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

### Default Implementations

- [ScrollTargetBehavior Implementations](chartscrolltargetbehavior/scrolltargetbehavior-implementations.md)

## See Also

### Scrolling

- [ChartScrollTargetBehaviorContext](chartscrolltargetbehaviorcontext.md) — Contextual information that you can use to determine how to best adjust how charts scroll.
