---
title: isDisplayingRepresentativeItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemgroup/isdisplayingrepresentativeitem
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/isdisplayingrepresentativeitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/isdisplayingrepresentativeitem.json'
content_hash: 'sha256:1e2876f00e77c38d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# isDisplayingRepresentativeItem

<sub>Instance Property</sub>

A Boolean value indicating whether the representative item is showing in place of the group’s items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isDisplayingRepresentativeItem: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the representative item is being displayed in the shortcuts bar. The value is [false](../../swift/false.md) when the individual bar button items are being displayed in the shortcuts bar.

## See Also

### Determining the group’s appearance

- [hidden](ishidden.md) — A Boolean that determines the visibility of the group.
