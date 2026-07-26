---
title: MajorValueAlignment
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/majorvaluealignment
source_url: 'https://developer.apple.com/documentation/charts/majorvaluealignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/majorvaluealignment.json'
content_hash: 'sha256:3549ed2d66faa557'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# MajorValueAlignment

<sub>Structure</sub>

A type that defines how the valigned aligned chart scroll target behavior aligns to major values on swipe.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MajorValueAlignment<Value> where Value : Plottable
```

## Topics

### Type Properties

- [page](majorvaluealignment/page.md) — Automatically set the major aligment unit to be the size of the visible domain which is equivalent to a page.

### Type Methods

- [matching(_:)](<majorvaluealignment/matching(__).md>) — Align to calendar components.
- [unit(_:)](<majorvaluealignment/unit(__).md>) — Align to units.

## See Also

### Supporting types

- [ValueAlignedLimitBehavior](valuealignedlimitbehavior.md) — A type that defines the amount of marks that can be scrolled at a time.
- [ValueAlignedChartScrollTargetBehavior](valuealignedchartscrolltargetbehavior.md) — A scroll target behavior that aligns to values spaced at regular intervals along the scrollable axes.
