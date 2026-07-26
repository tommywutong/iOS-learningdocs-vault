---
title: splitViewControllerLayoutEnvironment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/splitviewcontrollerlayoutenvironment
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/splitviewcontrollerlayoutenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/splitviewcontrollerlayoutenvironment.json'
content_hash: 'sha256:bee96ea9dba24b90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# splitViewControllerLayoutEnvironment

<sub>Instance Property</sub>

The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment { get }
```

## See Also

### Retrieving layout environment traits

- [listEnvironment](listenvironment.md) — The list environment represents whether a given trait collection is from a view in a UITableView or a UICollectionView list section.
- [UIListEnvironment](../uilistenvironment.md) — Constants that indicate the style of the containing list in a collection view or table view.
- [LayoutEnvironment](../uisplitviewcontroller/layoutenvironment.md) — Constants that indicate the current layout of the containing split view controller.
- [tabAccessoryEnvironment](tabaccessoryenvironment.md) — The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [Environment](../uitabaccessory/environment.md)
