---
title: preferredSplitBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/preferredsplitbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredsplitbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/preferredsplitbehavior.json'
content_hash: 'sha256:b29730e3e57d6135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# preferredSplitBehavior

<sub>Instance Property</sub>

The preferred behavior that determines how the child view controllers appear in relation to each other.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredSplitBehavior: UISplitViewController.SplitBehavior { get set }
```

## Discussion

Use this property to specify the split behavior that you prefer to use. The split view controller makes every effort to adopt the behavior you specify, but may use a different type of interface if there isn’t enough space to support your preferred choice. If changing the value of this property leads to an actual change in the current split behavior, the split view controller reflects the actual split behavior in the [splitBehavior](splitbehavior-swift.property.md) property. This change takes effect after the next layout occurs.

You do not set the split behavior directly; instead, you set a preferred split behavior by using the [preferredSplitBehavior](preferredsplitbehavior.md) property. This change takes effect after the next layout occurs. The split view controller reflects the actual split behavior in the [splitBehavior](splitbehavior-swift.property.md) property. The value of the [splitBehavior](splitbehavior-swift.property.md) property affects which display modes are available for the split view controller. For possible configurations, see [SplitBehavior](splitbehavior-swift.enum.md).

Setting the value of this property to [UISplitViewControllerSplitBehaviorAutomatic](splitbehavior-swift.enum/automatic.md) causes the split view controller to choose the most appropriate display mode for the currently available space. The default value of this property is [UISplitViewControllerSplitBehaviorAutomatic](splitbehavior-swift.enum/automatic.md).

## See Also

### Managing the split behavior

- [splitBehavior](splitbehavior-swift.property.md) — The current behavior that determines how the child view controllers appear in relation to each other.
- [SplitBehavior](splitbehavior-swift.enum.md) — Constants that describe the possible ways that the child view controllers appear in relation to each other.
