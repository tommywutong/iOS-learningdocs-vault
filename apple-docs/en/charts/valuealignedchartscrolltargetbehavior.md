---
title: ValueAlignedChartScrollTargetBehavior
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/valuealignedchartscrolltargetbehavior
source_url: 'https://developer.apple.com/documentation/charts/valuealignedchartscrolltargetbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/valuealignedchartscrolltargetbehavior.json'
content_hash: 'sha256:d6faaabb31aad5c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ValueAlignedChartScrollTargetBehavior

<sub>Structure</sub>

A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ValueAlignedChartScrollTargetBehavior
```

## Relationships

- **Conforms To**: [ChartScrollTargetBehavior](chartscrolltargetbehavior.md), [ScrollTargetBehavior](../swiftui/scrolltargetbehavior.md)

## Topics

### Initializers

- [init(matching:majorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(matching_majoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(unit:majorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(unit_majoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(xMatching:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(xmatching_ymatching_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(xMatching:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(xmatching_yunit_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(xUnit:yMatching:xMajorAlignment:yMajorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(xunit_ymatching_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
- [init(xUnit:yUnit:xMajorAlignment:yMajorAlignment:limitBehavior:)](<valuealignedchartscrolltargetbehavior/init(xunit_yunit_xmajoralignment_ymajoralignment_limitbehavior_).md>) — Creates a scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.

## See Also

### Supporting types

- [MajorValueAlignment](majorvaluealignment.md) — A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.
- [ValueAlignedLimitBehavior](valuealignedlimitbehavior.md) — A type that defines the amount of marks that can be scrolled at a time.
