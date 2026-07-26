---
title: 'updateTarget(_:context:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartscrolltargetbehavior/updatetarget(_:context:)-8j5z4'
source_url: 'https://developer.apple.com/documentation/charts/chartscrolltargetbehavior/updatetarget(_:context:)-8j5z4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartscrolltargetbehavior/updatetarget%28_%3Acontext%3A%29-8j5z4.json'
content_hash: 'sha256:82abfb0fd68fa95b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartScrollTargetBehavior](../chartscrolltargetbehavior.md)

# updateTarget(_:context:)

<sub>Instance Method</sub>

Updates the proposed target that a scrollable view should scroll to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateTarget(_ target: inout ScrollTarget, context: ScrollTargetBehaviorContext)
```

## Discussion

The system calls this method in two main cases:

- When a scroll gesture ends, it calculates where it would naturally scroll to using its deceleration rate. The system provides this calculated value as the target of this method.
- When a scrollable view’s size changes, it calculates where it should be scrolled given the new size and provides this calculates value as the target of this method.

You can implement this method to override the calculated target which will have the scrollable view scroll to a different position than it would otherwise.
