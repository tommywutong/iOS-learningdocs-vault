---
title: managingTabGroup
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitab/managingtabgroup
source_url: 'https://developer.apple.com/documentation/uikit/uitab/managingtabgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitab/managingtabgroup.json'
content_hash: 'sha256:3a17a6b49db587d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITab](../uitab.md)

# managingTabGroup

<sub>Instance Property</sub>

The managing tab group for the tab. This returns the root-most `UITabGroup` in the tab’s parent hierarchy with an active `managingNavigationController`. This can be different to `parent` if the tab is nested in multiple levels of tab groups. If the tab does not belong to a hierarchy with a managing navigation controller, then this will return nil. Default is nil.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var managingTabGroup: UITabGroup? { get }
```
