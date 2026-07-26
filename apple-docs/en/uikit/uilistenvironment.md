---
title: UIListEnvironment
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistenvironment
source_url: 'https://developer.apple.com/documentation/uikit/uilistenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistenvironment.json'
content_hash: 'sha256:0bd7c371cfafddec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIListEnvironment

<sub>Enumeration</sub>

Constants that indicate the style of the containing list in a collection view or table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIListEnvironment
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIListEnvironmentUnspecified](uilistenvironment/unspecified.md) — A constant that indicates the absence of information about a containing list.
- [UIListEnvironmentNone](uilistenvironment/none.md) — A constant that indicates there isn’t a containing list.
- [UIListEnvironmentPlain](uilistenvironment/plain.md) — A constant that indicates the containing list is a plain-style list.
- [UIListEnvironmentGrouped](uilistenvironment/grouped.md) — A constant that indicates the containing list is a grouped-style list.
- [UIListEnvironmentInsetGrouped](uilistenvironment/insetgrouped.md) — A constant that indicates the containing list is an inset-grouped-style list.
- [UIListEnvironmentSidebar](uilistenvironment/sidebar.md) — A constant that indicates the containing list is a sidebar-style list.
- [UIListEnvironmentSidebarPlain](uilistenvironment/sidebarplain.md) — A constant that indicates the containing list is a sidebar-plain-style list.

### Initializers

- [init(rawValue:)](<uilistenvironment/init(rawvalue_).md>)

## See Also

### Retrieving layout environment traits

- [listEnvironment](uitraitcollection/listenvironment.md) — The list environment represents whether a given trait collection is from a view in a UITableView or a UICollectionView list section.
- [splitViewControllerLayoutEnvironment](uitraitcollection/splitviewcontrollerlayoutenvironment.md) — The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.
- [LayoutEnvironment](uisplitviewcontroller/layoutenvironment.md) — Constants that indicate the current layout of the containing split view controller.
- [tabAccessoryEnvironment](uitraitcollection/tabaccessoryenvironment.md) — The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [Environment](uitabaccessory/environment.md)
