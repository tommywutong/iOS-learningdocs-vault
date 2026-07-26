---
title: primaryEdge
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/primaryedge-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/primaryedge-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/primaryedge-swift.property.json'
content_hash: 'sha256:85fc679f6e383e3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# primaryEdge

<sub>Instance Property</sub>

The side on which the primary view controller sits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var primaryEdge: UISplitViewController.PrimaryEdge { get set }
```

## Discussion

Use this property to change the default arrangement of the child view controllers. The default value of this property is [UISplitViewControllerPrimaryEdgeLeading](primaryedge-swift.enum/leading.md).

## See Also

### Positioning the primary view controller

- [PrimaryEdge](primaryedge-swift.enum.md) — Constants that indicate the side on which the primary view controller sits.
