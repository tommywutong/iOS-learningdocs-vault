---
title: splitBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/splitbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.property.json'
content_hash: 'sha256:8119567f140efa19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# splitBehavior

<sub>Instance Property</sub>

The current behavior that determines how the child view controllers appear in relation to each other.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var splitBehavior: UISplitViewController.SplitBehavior { get }
```

## Discussion

This property controls how a split view controller’s secondary view controller appears in relation to the other child view controllers. To change the current split behavior, change the value of the [preferredSplitBehavior](preferredsplitbehavior.md) property.

The value of this property affects which display modes are available for the split view interface. For possible configurations, see [SplitBehavior](splitbehavior-swift.enum.md).

## See Also

### Managing the split behavior

- [preferredSplitBehavior](preferredsplitbehavior.md) — The preferred behavior that determines how the child view controllers appear in relation to each other.
- [SplitBehavior](splitbehavior-swift.enum.md) — Constants that describe the possible ways that the child view controllers appear in relation to each other.
